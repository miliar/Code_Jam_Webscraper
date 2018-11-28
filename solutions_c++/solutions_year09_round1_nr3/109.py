//written on C++ (compatible with DevC++ / MS Visual C++ 6)
#include<stdio.h>

#define MAX 1000

double c1[100][100];

double comb(int n,int r)
{
       double i1,res;
       int i;
       res=1.0;
       for(i=1;i<=n;i++)res*=i;
       for(i=1;i<=r;i++)res/=i;
       for(i=1;i<=(n-r);i++)res/=i;
       return res;
}

int main()
{
    double e,p[MAX+1][100],z;
	int c,cnt,i,j,k,n,t;
    freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
    scanf("%d\n",&t);
    for(i=0;i<99;i++)for(j=0;j<99;j++)c1[i][j]=comb(i,j);
	for(cnt=1;cnt<=t;cnt++)
	{
     scanf("%d %d",&c,&n);
     z=comb(n,c);
     p[0][n]=0;p[1][n]=1;for(i=n+1;i<=c;i++)p[1][i]=0;
     for(i=2;i<=MAX;i++)
     {for(j=n;j<=c;j++)
      {p[i][j]=0.0;
       for(k=n;k<=j;k++)p[i][j]+=(p[i-1][k]*c1[k][n-j+k]*c1[c-k][j-k]/c1[c][n]);
      }
     }
     e=0.0;
     for(i=1;i<=MAX;i++)e+=(i*(p[i][c]-p[i-1][c]));
	 printf("Case #%d: %.7f\n",cnt,e);
    }
    return 0;
}
