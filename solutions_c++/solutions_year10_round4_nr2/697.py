#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int a[100000];
int b[20][2048];
int c[20][2048][30];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tn,ti=0;
	scanf("%d",&tn);
	while(tn--)
	{
		int P;
		scanf("%d",&P);
		int n = 1<<P;
		for(int i = 0; i < n; ++i)
			scanf("%d",&a[i]);
		int t = n;
		for(int i = 0; i < P; ++i)
		{
			t >>= 1;
			for(int j = 0; j < t; ++j)
				scanf("%d",&b[i][j]);
		}
		memset(c,-1,sizeof(c));
		for(int i = 0; i < (n>>1); i++)
		{
			int t = min(a[i*2],a[i*2+1]);
			c[0][i][t] = b[0][i];
			if(t > 0) 
				while(t--) c[0][i][t] = 0;
		}
		t = n>>1;
		for(int level = 1; level < P; ++level)
		{
			t >>= 1;
			for(int j = 0; j < t; ++j)
			{
				for(int k = P; k >= 0; --k)
				{
					int t1 = -1, t2 = -1;
					if(c[level-1][j<<1][k+1] != -1 && c[level-1][(j<<1)+1][k+1] != -1) t1 = c[level-1][j<<1][k+1] + c[level-1][(j<<1)+1][k+1];
					if(c[level-1][j<<1][k] != -1 && c[level-1][(j<<1)+1][k] != -1) t2 = b[level][j] + c[level-1][j<<1][k] + c[level-1][(j<<1)+1][k];
					if(t1 != -1) c[level][j][k] = t1;
					if(t2 != -1 && (c[level][j][k] == -1 || c[level][j][k] > t2)) c[level][j][k] = t2;
					if(c[level][j][k+1] != -1 && (c[level][j][k] == -1 || c[level][j][k] > c[level][j][k+1])) c[level][j][k] = c[level][j][k+1];
				}
			}
		}
		printf("Case #%d: %d\n", ++ti, c[P-1][0][0]);
	}
}
/*
2 
2 
1 1 0 1 
1 1 
1
*/