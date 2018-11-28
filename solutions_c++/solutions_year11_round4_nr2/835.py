#include<stdio.h>
#include<cmath>
using namespace std;

const int MAXN = 510;
const double eps = 1e-8;
char mat[MAXN][MAXN];
int r,c,n;


bool check(int x,int y,int len)
{
	//printf("x is %d %d %d\n",x,y,len);
	if (x + len > r || y + len > c) return false;
	
	double cx = (double)(x + x + len-1) / 2;
	double cy = (double)(y + y + len-1) / 2;
	
	//printf("cx is %.2f %.2f\n",cx,cy);
	double tx = 0;
	double ty = 0;
	for (int i=x;i<x+len;i++)
		for (int j=y;j<y+len;j++)
		if ( !((i==x && j==y) || (i==x && j==y+len-1) || (i==x+len-1 && j==y) || (i==x+len-1 && j==y+len-1)) )
		{
			double tmpx = (double)(i-cx) * mat[i][j];
			double tmpy = (double)(j-cy) * mat[i][j]; 
			tx += tmpx;
			ty += tmpy;
			//printf("here is (%d,%d) norm is (%.2f,%.2f) mat %d \n",i,j,tmpx,tmpy,mat[i][j]);
		}
	//printf("tx is (%.2f,%.2f)\n",tx,ty);
	return fabs(tx) < eps && fabs(ty) < eps;
}
int main()
{
	int test;
	scanf("%d",&test);
	for (int cas=1;cas<=test;cas++)
	{
		scanf("%d%d%d",&r,&c,&n);
		for (int i=0;i<r;i++)
		{
			scanf("%s",mat[i]);
			for (int j=0;j<c;j++)
				mat[i][j] -= '0';
		}			
					
		int ans = 2;
		
		for (int lx=0;lx<r;lx++)
			for (int ly=0;ly<c;ly++)
			{
				for (int i=ans+1;i<=r;i++)
				if (check(lx,ly,i))
				{
					ans = i;
				}
			}
		
		printf("Case #%d: ",cas);
		if (ans < 3)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",ans);
	}
}

