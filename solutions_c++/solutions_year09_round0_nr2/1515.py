#include <iostream>
#include <vector>

using namespace std;
typedef vector <int> vi;
typedef vector <vi> vvi;

int dx[4] = {0, -1, 1, 0};
int dy[4] = {-1, 0, 0, 1};

vvi data, col;
int H, W;
char cur;

char func(int i, int j)
{
	if (i < 1 || i > H || j < 1 || j > W)
		return -1;

	if (col[i][j] != -1)
		return col[i][j];

	int min = 100000;
	for (int t = 0; t < 4; t++)
	{
		if (data[i+dy[t]][j+dx[t]] < min)
			min = data[i+dy[t]][j+dx[t]];
	}

	if (min >= data[i][j])
	{
		col[i][j] = cur;
		cur ++;
		return col[i][j];
	}

	for (int t = 0; t < 4; t++)
	{
		if (data[i+dy[t]][j+dx[t]] == min)
		{
			col[i][j] = func(i+dy[t], j+dx[t]);
			break;
		}
	}

	return col[i][j];
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int L;
	cin >> L;

	int t = 0;
	while (t < L)
	{
		if (t == 3)
			t = 3;
		cur = 'a';
		data.clear();
		col.clear();

		cin >> H >> W;

		data.resize(H + 2, vi(W + 2, 100000));
		col.resize(H + 2, vi(W + 2, -1));

		int x;
		for (int i = 1; i <= H; i++)
		{
			for (int j = 1; j <= W; j++)
			{
				cin >> x;
				data[i][j] = x;
			}
		}

		cout << "Case #" << t + 1 << ":" << endl;		
		for (int i = 1; i <= H; i++)
		{
			for (int j = 1; j <= W; j++)
			{
				if (col[i][j] == -1)
					func(i, j);
				cout << (char)col[i][j] << " ";
			}
			cout << endl;
		}

		t++;
	}
	return 0;
}