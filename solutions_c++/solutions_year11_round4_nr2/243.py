#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>;

using namespace std;

int T;
int R, C, D;
int a[510][510];
int sum[510][510];
int sumx1[510][510];
int sumy1[510][510];
int sumx2[510][510];
int sumy2[510][510];

void input()
{
	memset(a, 0, sizeof(a));
	memset(sum, 0, sizeof(sum));
	memset(sumx1, 0, sizeof(sumx1));
	memset(sumx2, 0, sizeof(sumx2));
	memset(sumy1, 0, sizeof(sumy1));
	memset(sumy2, 0, sizeof(sumy2));
	cin >> R >> C >> D;
	for (int i=0; i<R; i++)
	{
		string t;
		cin >> t;
		for (int j=0; j<C; j++)
			a[i][j] = t[j] - '0';
	}
	for (int i=0; i<R; i++)
		for (int j=0; j<C; j++)
			if (i==0 && j==0) sum[i][j] = a[i][j];
			else if (i==0) sum[i][j] = sum[i][j-1]+a[i][j];
			else if (j==0) sum[i][j] = sum[i-1][j] + a[i][j];
			else sum[i][j] = sum[i-1][j]+sum[i][j-1] + a[i][j] - sum[i-1][j-1];
	for (int i=0; i<R; i++)
		for (int j=0; j<C; j++)
		{
			if (j>0) sumx1[i][j] = sumx1[i][j-1]+a[i][j]*(j+1);
			else sumx1[i][j] = a[i][j];
			if (i>0) sumy1[i][j] = sumy1[i-1][j]+a[i][j]*(i+1);
			else sumy1[i][j] = a[i][j];

			if (j>0) sumx2[i][j] = sumx2[i][j-1]+a[i][j]*(C-j);
			else sumx2[i][j] = a[i][j] * (C-j);
			if (i>0) sumy2[i][j] = sumy2[i-1][j]+a[i][j]*(R-i);
			else sumy2[i][j] = a[i][j] * (R-i);
		}
	for (int i=0; i<R; i++)
		for (int j=0; j<C; j++)
		{
			if (i>0) sumx1[i][j]+=sumx1[i-1][j];
			if (j>0) sumy1[i][j]+=sumy1[i][j-1];
			if (i>0) sumx2[i][j]+=sumx2[i-1][j];
			if (j>0) sumy2[i][j]+=sumy2[i][j-1];
		}
}

int csum(int x1, int y1, int x2, int y2)
{
	if (x1 == 0 && y1==0)
		return sum[x2][y2];
	else if (x1==0)
		return sum[x2][y2] - sum[x2][y1 - 1];
	else if (y1==0)
		return sum[x2][y2] - sum[x1 - 1][y2];
	else
		return sum[x2][y2] + sum[x1 - 1][y1 - 1] -sum[x1-1][y2] - sum[x2][y1-1];
}

int csumx1(int x1, int y1, int x2, int y2)
{
	if (x1 == 0 && y1==0)
		return sumx1[x2][y2];
	else if (x1==0)
		return sumx1[x2][y2] - sumx1[x2][y1 - 1];
	else if (y1==0)
		return sumx1[x2][y2] - sumx1[x1 - 1][y2];
	else
		return sumx1[x2][y2] + sumx1[x1 - 1][y1 - 1] -sumx1[x1-1][y2] - sumx1[x2][y1-1];
}

int csumy1(int x1, int y1, int x2, int y2)
{
	if (x1 == 0 && y1==0)
		return sumy1[x2][y2];
	else if (x1==0)
		return sumy1[x2][y2] - sumy1[x2][y1 - 1];
	else if (y1==0)
		return sumy1[x2][y2] - sumy1[x1 - 1][y2];
	else
		return sumy1[x2][y2] + sumy1[x1 - 1][y1 - 1] -sumy1[x1-1][y2] - sumy1[x2][y1-1];
}

int csumx2(int x1, int y1, int x2, int y2)
{
	if (x1 == 0 && y1==0)
		return sumx2[x2][y2];
	else if (x1==0)
		return sumx2[x2][y2] - sumx2[x2][y1 - 1];
	else if (y1==0)
		return sumx2[x2][y2] - sumx2[x1 - 1][y2];
	else
		return sumx2[x2][y2] + sumx2[x1 - 1][y1 - 1] -sumx2[x1-1][y2] - sumx2[x2][y1-1];
}

int csumy2(int x1, int y1, int x2, int y2)
{
	if (x1 == 0 && y1==0)
		return sumy2[x2][y2];
	else if (x1==0)
		return sumy2[x2][y2] - sumy2[x2][y1 - 1];
	else if (y1==0)
		return sumy2[x2][y2] - sumy2[x1 - 1][y2];
	else
		return sumy2[x2][y2] + sumy2[x1 - 1][y1 - 1] -sumy2[x1-1][y2] - sumy2[x2][y1-1];
}

int check(int i, int j, int k)
{
	if (k % 2 == 0)
	{
		int p1x = i, p2x = i, p3x = i+k-1, p4x = i+k-1;
		int p1y = j+k/2, p2y = j+k-1, p3y = j+k/2, p4y = j+k-1;
		int rweight = csumx1(p1x, p1y, p4x, p4y) - csum(p1x, p1y, p4x, p4y)*p1y;
		rweight -= (a[p2x][p2y] * (k/2));
		rweight -= (a[p4x][p4y] * (k/2));

		p1x = i+k/2, p2x = i+k/2, p3x = i+k-1, p4x=i+k-1;
		p1y = j, p2y = j+k-1, p3y = j, p4y = j+k-1;
		int dweight = csumy1(p1x, p1y, p4x, p4y) - csum(p1x, p1y, p4x, p4y)*p1x;
		dweight -= (a[p3x][p3y]*(k/2));
		dweight -= (a[p4x][p4y]*(k/2));

		p1x = i, p2x = i, p3x = i+k-1, p4x = i+k-1;
		p1y = j, p2y = j+k/2-1, p3y = j, p4y = j+k/2-1;
		int lweight = csumx2(p1x, p1y, p4x, p4y)-csum(p1x, p1y, p4x, p4y)*(C-p4y-1);
		lweight -= (a[p1x][p1y] * (k/2));
		lweight -= (a[p3x][p3y] * (k/2));

		p1x = i, p2x = i, p3x = i+k/2-1, p4x = i+k/2-1;
		p1y = j, p2y = j+k-1, p3y = j, p4y = j+ k -1;
		int uweight = csumy2(p1x, p1y, p4x, p4y) - csum(p1x, p1y, p4x, p4y)*(R-p3x-1);
		uweight -= (a[p1x][p1y]*(k/2));
		uweight -= (a[p2x][p2y]*(k/2));

		if (rweight == lweight && dweight == uweight)
			return 1;
	}
	else if (k % 2 == 1)
	{
		int p1x = i, p2x = i, p3x = i+k-1, p4x = i+k-1;
		int p1y = j+k/2+1, p2y = j+k-1, p3y = j+k/2+1, p4y = j+k-1;
		int rweight = csumx1(p1x, p1y, p4x, p4y) - csum(p1x, p1y, p4x, p4y)*p1y;
		rweight -= (a[p2x][p2y] * (k/2));
		rweight -= (a[p4x][p4y] * (k/2));

		p1x = i+k/2+1, p2x = i+k/2+1, p3x = i+k-1, p4x=i+k-1;
		p1y = j, p2y = j+k-1, p3y = j, p4y = j+k-1;
		int dweight = csumy1(p1x, p1y, p4x, p4y) - csum(p1x, p1y, p4x, p4y)*p1x;
		dweight -= (a[p3x][p3y]*(k/2));
		dweight -= (a[p4x][p4y]*(k/2));

		p1x = i, p2x = i, p3x = i+k-1, p4x = i+k-1;
		p1y = j, p2y = j+k/2-1, p3y = j, p4y = j+k/2-1;
		int lweight = csumx2(p1x, p1y, p4x, p4y)-csum(p1x, p1y, p4x, p4y)*(C-p4y-1);
		lweight -= (a[p1x][p1y] * (k/2));
		lweight -= (a[p3x][p3y] * (k/2));

		p1x = i, p2x = i, p3x = i+k/2-1, p4x = i+k/2-1;
		p1y = j, p2y = j+k-1, p3y = j, p4y = j+ k -1;
		int uweight = csumy2(p1x, p1y, p4x, p4y) - csum(p1x, p1y, p4x, p4y)*(R-p3x-1);
		uweight -= (a[p1x][p1y]*(k/2));
		uweight -= (a[p2x][p2y]*(k/2));

		if (rweight == lweight && dweight == uweight)
			return 1;
	}
	return 0;
}

int solve()
{
	int ret = -1;
	for (int i=0; i<R-2; i++)
		for (int j=0; j<C-2; j++)
			for (int K = max(ret, 3); i+K<=R && j+K<=C; K++)
				if (check(i,j,K))
					ret = K;
	return ret;
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin >> T;
	for (int i=1; i<=T; i++)
	{
		input();
		int ans = solve();
		if (ans > 0) printf("Case #%d: %d\n", i, ans);
		else printf("Case #%d: IMPOSSIBLE\n", i);
	}
}