#include<stdio.h>
#include<iostream>
#include<math.h>
using namespace std;
long a[300],delet,insert,m,n,cost[300][300],f[300][300];
long abs(int x)
{
	if (x<0) return (-x);
	else return x;
}

int shang(int a,int b)
{
	if (((a%b)==0)&&(a!=0)) return (a/b);
	else return ((a/b)+1);
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
	long testcase;
	scanf("%ld",&testcase);

	for (int ttt=1;ttt<=testcase;ttt++)
	{
		scanf("%ld %ld %ld %ld ",&delet,&insert,&m,&n);
		for (int i=1;i<=n;i++) scanf("%ld",&a[i]);
		if (m==0)
		{
			for (int i=0;i<=255;i++) for (int j=0;j<=255;j++) if (i==j) cost[i][j]=0;
			else cost[i][j]=300000;
		}
		else
		{
		for (int i=0;i<=255;i++)
		   for (int j=0;j<=255;j++)
		      cost[i][j]=insert*(shang(abs(i-j),m)-1);
	    }
	   
		for (int j=0;j<=255;j++){ if (delet<abs(j-a[1])) f[1][j]=delet; else f[1][j]=abs(j-a[1]); }
	
		for (int i=2;i<=n;i++)
		  for (int j=0;j<=255;j++)
		  {
				f[i][j]=f[i-1][j]+delet;
				for (int k=0;k<=255;k++)
				  if (f[i-1][k]+cost[j][k]+abs(j-a[i])<f[i][j]) f[i][j]=f[i-1][k]+cost[j][k]+abs(j-a[i]);
				}
	   long ans=300000;
	   for (int j=0;j<=255;j++) if (f[n][j]<ans) ans=f[n][j];
	   printf("Case #%ld: %ld \n",ttt,ans);
	}
}
