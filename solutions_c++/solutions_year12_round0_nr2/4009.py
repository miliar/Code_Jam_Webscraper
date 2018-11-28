#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
template<class T> inline void gmax(T &a, T b){if (a < b) a = b;}
const int maxn = 100 + 2;
int table1[] = {-1, -1,  2,  2,  2,  3,  3,  3,  4,  4,  4,  5,  5,  5,  6,  6,  6,  7,  7,  7,  8,  8,  8,  9,  9,  9, 10, 10, 10, -1, -1};
int table2[] = { 0,  1,  1,  1,  2,  2,  2,  3,  3,  3,  4,  4,  4,  5,  5,  5,  6,  6,  6,  7,  7,  7,  8,  8,  8,  9,  9,  9, 10, 10, 10};

int n, s, p;
int f[maxn][maxn];
int t[maxn];

int detm(int x)
{
	return x >= p;
}

int work()
{
	cin >> n >> s >> p;
	for (int j = 1; j <= n; j++) cin >> t[j];

	memset(f, 0x8f, sizeof(f));
	f[0][0] = 0;

	for (int i = 1; i <= n; i++)
		for (int j = 0; j <= s && j <= i; j++)
		{
			f[i][j] = f[i-1][j] + detm(table2[t[i]]);
			if (table1[t[i]] != -1 && j != 0)
				gmax(f[i][j], f[i-1][j-1] + detm(table1[t[i]]));
		}

	return f[n][s];
}

int main()
{
	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int T;

	cin >> T;

	for (int i = 1; i <= T; i++)
	{
		cout << "Case #" << i << ": " << work() << endl;
	}

	fclose(stdin); fclose(stdout);
	return 0;
}


/*
	for (int i = 0; i <= 10; i++)
		for (int j = i; j <= 10; j++)
			for (int k = j; k <= 10; k++)
			{
				if (k - i > 2) continue;
				if (!(k - i == 2 || j - i == 2 || k - j == 2)) continue;
				int sum = i + j + k;
				if (kk[sum] <= k) ii[sum] = i, jj[sum] = j, kk[sum] = k;
			}
			
	for (int i = 0; i <= 30; i++)
		cout << i << ' ' << ii[i] << ' ' << jj[i] << ' ' << kk[i] << endl; 
*/
