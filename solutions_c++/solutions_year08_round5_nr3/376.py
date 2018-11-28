#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

const int maxm = 10;
const int maxn = 10;

int map[maxm];
int m,n;

int data[maxm][1024];

int max(int a, int b)
{
	if (a>b) return a; else return b;
}

int cc(int j)
{
	int ct = 0;
	for (int i=0; i<n; i++)
		if ((j & (1 << i)) != 0)
			ct++;
	return ct;
}

bool valid(int j)
{
	for (int i=0; i<n; i++)
		if ((j &  (1 << i) + (1 << (i+1))) == (1<<i) + (1<<(i+1)))
			return false;
	return true;
}

bool fit(int next, int prev)
{
	for (int i=0; i<n; i++)
		if ((next & (1 << i)) != 0)
		{
			if ((i != 0) && ((prev & (1<<i-1)) != 0))
				return false;
			if ((i != m-1) && ((prev & (1 << i+1)) != 0))
				return false;
		}
	return true;
}

bool suit(int j, int row)
{
	if ((map[row] & j) != 0)
		return false;
	return true;
}

int main()
{
	int N;
	cin >> N;
	for (int tc = 0; tc < N; tc++)
	{
		int maxv = 0;
		cin >> m >> n;
		string str;
		getline(cin, str);
		for (int i=0; i<m; i++)
		{
			string str;
			getline(cin, str);
			int k = 0;
			for (int j=0; j<n; j++)
			{
				k = k * 2;
				if (str[j] == 'x')
					k++;
			}
			map[i] = k;
		}
		for (int i=0; i<m; i++)
		{
			for (int j=0; j< 1024; j++)
			{
				if (valid(j))
					if (suit(j,i))
					{
						data[i][j] = 0;
						if (i!=0)
						for (int k=0; k < 1024; k++)
						{
							if (fit(j,k))
								if (data[i-1][k] != -1)
									data[i][j] = max(data[i][j], data[i-1][k]);
						}
						data[i][j] += cc(j);
						if (data[i][j] > maxv)
							maxv = data[i][j];
					}
					else
						data[i][j] = -1;
				else
					data[i][j] = -1;
			}
		}
		cout << "Case #" << tc+1 << ": " << maxv << endl;

	}
}

