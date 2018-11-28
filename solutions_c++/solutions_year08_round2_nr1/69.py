#include<stdio.h>
#include<string.h>

const int maxn = 100000;
int n;
__int64 A,B,C,D,x0,y0,M;
struct Point 
{
	int x, y;
} p[maxn];
__int64 c[3][3];

int main() {
	int cs;
	scanf("%d",&cs);
	int step = 1;
	while(cs--)
	{
		int i,j,k;
		scanf("%d",&n);
		scanf("%I64d%I64d%I64d%I64d%I64d%I64d%I64d",&A,&B,&C,&D,&x0,&y0,&M);
		p[0].x = x0, p[0].y = y0;
		for(i=1;i<n;i++){
			p[i].x = (A * p[i-1].x + B) % M;
			p[i].y = (C * p[i-1].y + D) % M;
		}
		memset(c, 0, sizeof(c));
		for(i=0;i<n;i++)
		{
			c[p[i].x%3][p[i].y%3] ++;
		}
		__int64 ans = 0, f1;
		for(i=0;i<9;i++)for(j=i;j<9;j++)for(k=j;k<9;k++)
		{
			int x1 = i/3;
			int y1 = i%3;
			int x2 = j/3;
			int y2 = j%3;
			int x3 = k/3;
			int y3 = k%3;
			x0 = (x1+x2+x3);
			y0 = (y1+y2+y3);
			f1 = 0;
			if((x0%3)==0 && (y0%3)==0 && c[x1][y1] && c[x2][y2] && c[x3][y3]) {
				if(i!=j && j!=k) f1 = c[x1][y1]*c[x2][y2]*c[x3][y3];
				else if(i==j && j==k) f1 = c[x1][y1]*(c[x1][y1]-1)*(c[x1][y1]-2)/6;
				else if(i==j) f1 = c[x1][y1]*(c[x1][y1]-1)/2*c[x3][y3];
				else if(k==j) f1 = c[x2][y2]*(c[x2][y2]-1)/2*c[x1][y1];				
			}
			ans += f1;
		}
		printf("Case #%d: %I64d\n", step++, ans);
	}
	return 0;
}