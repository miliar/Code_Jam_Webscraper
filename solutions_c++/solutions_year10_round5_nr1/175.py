#include <cstdio>
#include <vector>

using namespace std;

vector<int> prime;

void egcd(int a, int b, int &d, int &x, int &y)
{
	if (!b)
	{
		d = a;
		x = 1;
		y = 0;
		return;
	}
	int q, w, e;
	egcd(b, a % b, q, w, e);

	d = q; x = e; y = w - a / b * e;
}

int minverse(int a, int p)
{
	if (!a) return 0; // no inverse
	int d, x, y;
	egcd(a, p, d, x, y);

	return (p + x % p) % p;
}

void get_prime()
{
	prime.push_back(2);
	int i, j;
	for (i = 3;i < 1000000;i += 2)
	{
		int ok = true;
		for (j = 0;j < prime.size() && (long long)prime[j] * prime[j] <= i;j++)
		{
			if (i % prime[j] == 0)
			{
				ok = false;
				break;
			}
		}
		if (!ok)
			continue;
		prime.push_back(i);
	}
}

int matrix[11][3];
int go(vector<int> &data, int p)
{
	if (data.size() == 1)
		return -1;
	int i;
	for (i = 0;i < data.size() - 1;i++)
	{
		if (data[i] >= p)
			return -1;
		if (data[i + 1] >= p)
			return -1;
		matrix[i][0] = data[i];
		matrix[i][1] = 1;
		matrix[i][2] = data[i + 1];
	}

	int R = data.size() - 1;
	int C = 3;

	int col;
	int pivot_cnt = 0;
	for (col = 0;col < C;col++)
	{
		for (i = pivot_cnt;i < R;i++)
		{
			if (matrix[i][col] != 0)
				break;
		}

		int row = i;

		if (row == R)
			continue;

		int j;
		for (j = 0;j < C;j++)
			swap(matrix[pivot_cnt][j], matrix[row][j]);

		row = pivot_cnt;

		int inverse = minverse(matrix[row][col], p);
		for (j = 0;j < C;j++)
			matrix[row][j] = ((long long)matrix[row][j] * inverse) % p;

		int k;
		for (j = 0;j < R;j++)
		{
			if (j == row)
				continue;

			int ratio = matrix[j][col];
			for (k = 0;k < C;k++)
			{
				matrix[j][k] = (matrix[j][k] - ((long long)ratio * matrix[row][k]) % p) % p;
				if (matrix[j][k] < 0)
					matrix[j][k] += p;
			}
		}

		pivot_cnt++;
	}
	if (pivot_cnt > 2)
		return -1;
	if (pivot_cnt == 1)
	{
		int i;
		for (i = 0;i < data.size() - 1;i++)
			if (data[i] == data[data.size() - 1])
				return data[i + 1];
		return -1;
		/*
		if (matrix[0][0] != 0)
		{
			// pivot was a
			return data[data.size() - 1];
		}
		else
		{
			// pivot was b
			// all we know is b = c..
			// but if everything's zero?
			for (i = 0;i < data.size();i++)
				if (data[i] != 0)
					return -1;
			return 0;
		}*/
	}
	if (pivot_cnt == 0)
		return -1;

	int a = matrix[0][2];
	int b = matrix[1][2];

	for (i = 0;i < data.size() - 1;i++)
	{
		int next = (data[i] * (long long)a + b) % p;
		if (next != data[i + 1])
		{
			fprintf(stderr, "???????\n");
		}
	}

	return (data[data.size() - 1] * (long long)a + b) % p;
}

int main()
{
	get_prime();

	int tc;
	scanf("%d", &tc);
	int ti;
	for (ti = 1;ti <= tc;ti++)
	{
		printf("Case #%d: ", ti);
		
		int d, k;

		scanf("%d %d", &d, &k);
		vector<int> data;
		int i;
		for (i = 0;i < k;i++)
		{
			int v;
			scanf("%d", &v);
			data.push_back(v);
		}

		int lim = 1;
		for (;d;d--)
			lim *= 10;

		int ans = -1;
		for (i = 0;i < prime.size();i++)
		{
			if (prime[i] > lim)
				break;
			int cur = go(data, prime[i]);
			if (cur == -1)
				continue;
			if (ans != -1 && ans != cur)
			{
				ans = -2;
				break;
			}
			ans = cur;
		}

		if (ans < 0)
			printf("I don't know.\n");
		else
			printf("%d\n", ans);

		fprintf(stderr, "Case #%d\n", ti);
	}

	return 0;
}
