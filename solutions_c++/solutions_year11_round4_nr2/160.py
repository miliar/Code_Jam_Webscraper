#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>


using namespace std;

const int MAXN = 520;

int mt[MAXN][MAXN];
long long sm[MAXN][MAXN];


inline long long Get(int r1, int c1, int r2, int c2)
{
	return sm[r2][c2] - sm[r1-1][c2] - sm[r2][c1-1] + sm[r1-1][c1-1];
}


bool check(int a, int b, int k)
{
	if (k & 1)
	{
		int mid = k / 2;
		long long sum = 0;
		for (int i = 0; i < mid; i ++)
			sum += Get(a + i, b, a + i, b + k - 1) * (mid - i);
		for (int i = mid + 1; i < k; i ++)
			sum -= Get(a + i, b, a + i, b + k - 1) * (i - mid);
		sum -= (mt[a][b] + mt[a][b+k-1]) * mid;
		sum += (mt[a+k-1][b] + mt[a+k-1][b+k-1]) * mid;
		if (sum != 0)  return false;

		for (int j = 0; j < mid; j ++)
			sum += Get(a, b + j, a + k - 1, b + j) * (mid - j);
		for (int j = mid + 1; j < k; j ++)
			sum -= Get(a, b + j, a + k - 1, b + j) * (j - mid);

		sum -= (mt[a][b] + mt[a+k-1][b]) * mid;
		sum += (mt[a][b+k-1] + mt[a+k-1][b+k-1]) * mid;

		if (sum != 0)  return false;
	} else {
		int mid = k / 2;
		long long sum = 0;
		for (int i = 0; i < mid; i ++)
			sum += Get(a + i, b, a + i, b + k - 1) * ((mid - i) * 2 - 1);
		for (int i = mid; i < k; i ++)
			sum -= Get(a + i, b, a + i, b + k - 1) * ((i - mid) * 2 + 1);
		sum -= (mt[a][b] + mt[a][b+k-1]) * (mid * 2 - 1);
		sum += (mt[a+k-1][b] + mt[a+k-1][b+k-1]) * ((k - 1 - mid) * 2 + 1);
		if (sum != 0)  return false;

		for (int j = 0; j < mid; j ++)
			sum += Get(a, b + j, a + k - 1, b + j) * ((mid - j) * 2 - 1);
		for (int j = mid; j < k; j ++)
			sum -= Get(a, b + j, a + k - 1, b + j) * ((j - mid) * 2 + 1);

		sum -= (mt[a][b] + mt[a+k-1][b]) * (mid * 2 - 1);
		sum += (mt[a][b+k-1] + mt[a+k-1][b+k-1]) * ((k - 1 - mid) * 2 + 1);

		if (sum != 0)  return false;
	}
	return true;
}


int work()
{
	memset(sm, 0, sizeof(sm));
	int R, C, D;
	cin >> R >> C >> D;
	for (int i = 1; i <= R; i ++)
	{
		string ss;	cin >> ss;
		for (int j = 1; j <= C; j ++)
			mt[i][j] = ss[j-1] - 48 + D;
	}

	for (int i = 1; i <= R; i ++)
		for (int j = 1; j <= C; j ++)
			sm[i][j] = sm[i][j-1] + sm[i-1][j] - sm[i-1][j-1] + mt[i][j]; 

	for (int k = min(R, C); k >= 3; k --)
	{
		for (int i = 1; i + k - 1 <= R; i ++)
			for (int j = 1; j + k - 1 <= C; j ++)
				if (check(i, j, k))  return k;
	}
	
	return 0;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, v;
	cin >> T;
	for (int k = 1; k <= T; k ++)
	{
		printf("Case #%d: ", k);
		if ((v = work()) == 0)  cout << "IMPOSSIBLE" << endl;
		else cout << v << endl; 
	}
	return 0;
}