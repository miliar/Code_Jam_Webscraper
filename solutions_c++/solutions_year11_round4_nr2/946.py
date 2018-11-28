#include<cstdio>
#include<cstring>
#include<algorithm>
#include<map>
#include<cmath>

using namespace std;

int w[500][500];
int r, c, d;

bool check(int cr, int cc, int s)
{
	if(cr + s >= r || cr - s < 0)return false;
	if(cc + s >= c || cc - s < 0)return false;
	
	int x = 0, y = 0;
	int i, j;
	
	for(i = cr - s; i <= cr + s; i ++)
	{
		for(j = cc - s; j <= cc + s; j ++)
		{
			x += (i-cr)*(w[i][j]+d);
			y += (j-cc)*(w[i][j]+d);
			//printf("%d %d\n", x, y);
		}
	}
	//printf("%d %d %d %d %d\n", cr, cc, s, x, y);
	
	x -= (0 - s)*(w[cr-s][cc-s]+d);
	x -= (0 - s)*(w[cr-s][cc+s]+d);
	x -= (s)*(w[cr+s][cc-s]+d);
	x -= (s)*(w[cr+s][cc+s]+d);
	
	y -= (0 - s)*(w[cr-s][cc-s]+d);
	y -= (s)*(w[cr-s][cc+s]+d);
	y -= (0 - s)*(w[cr+s][cc-s]+d);
	y -= (s)*(w[cr+s][cc+s]+d);
	
	//printf("%d %d %d %d %d\n", cr, cc, s, x, y);
	if(x == 0 && y == 0)return true;
	return false;
}


bool check2(int cr, int cc, int s)
{
	if(cr + s >= r || cr - s+1 < 0)return false;
	if(cc + s >= c || cc - s+1 < 0)return false;
	
	double x = 0, y = 0;
	int i, j;
	
	for(i = cr - s + 1; i <= cr + s; i ++)
	{
		for(j = cc - s + 1; j <= cc + s; j ++)
		{
			x += (i-cr-0.5)*(w[i][j]+d);
			y += (j-cc-0.5)*(w[i][j]+d);
			//printf("%d %d\n", x, y);
		}
	}
	//printf("%d %d %d %d %d\n", cr, cc, s, x, y);
	
	x -= (0 - s+0.5)*(w[cr-s+1][cc-s+1]+d);
	x -= (0 - s+0.5)*(w[cr-s+1][cc+s]+d);
	x -= (s-0.5)*(w[cr+s][cc-s+1]+d);
	x -= (s-0.5)*(w[cr+s][cc+s]+d);
	
	y -= (0 - s+0.5)*(w[cr-s+1][cc-s+1]+d);
	y -= (s-0.5)*(w[cr-s+1][cc+s]+d);
	y -= (0 - s+0.5)*(w[cr+s][cc-s+1]+d);
	y -= (s-0.5)*(w[cr+s][cc+s]+d);
	
	//printf("%d %d %d %d %d\n", cr, cc, s, x, y);
	if(fabs(x) < 1e-9 && fabs(y) < 1e-9)return true;
	return false;
}

int main()
{
	int cas, T;
	scanf("%d", &T);
	for(cas = 1; cas <= T; cas ++)
	{
		int n, m;
		int i, j, k;
		int mx;
		scanf("%d %d %d", &r, &c, &d);
		for(i = 0; i < r; i ++)
		{
			for(j = 0; j < c; j ++)
			{
				scanf("%1d", &w[i][j]);
			}
		}
		mx = r > c ? r : c;
		int ans = 1;
		for(i = 0; i < r; i ++)	
		{
			for(j = 0; j < c; j ++)
			{
				for(k = 1; k <= mx; k ++)
				{
					if(check(i, j, k))ans >?= k*2+1;
					if(check2(i, j, k))ans >?= k*2;
				}
			}
		}
		if(ans >= 3)
		{
			printf("Case #%d: %d\n", cas, ans);
		}
		else {
			printf("Case #%d: IMPOSSIBLE\n", cas);
		}
	}
	return 0;
}

/*
6 7 2
1111111
1122331
1211521
1329131
1242121
1222211
*/
