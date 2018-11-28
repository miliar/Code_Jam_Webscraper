#include<iostream>
using namespace std;
int d[45][45][4];
int v[45][45][4];
int a[45][45];
int b[45][45];
int c[45][45];
int m,n,i,j,k,ki,kj,kk,cur,tmp;
int cn,ci;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&cn);
	for (ci=1;ci<=cn;ci++)
	{
		scanf("%d %d",&m,&n);
		for (i=m;i>=1;i--)
		for (j=1;j<=n;j++) 
		{
			scanf("%d %d %d",&a[i][j],&b[i][j],&c[i][j]);
			b[i][j]+=a[i][j];
		}
		for (i=0;i<=m+1;i++)
		for (j=0;j<=n+1;j++)
		for (k=0;k<4;k++) d[i][j][k]=2100000000;
		d[1][1][0]=0;
		memset(v,0,sizeof(v));
		while (!v[m][n][3])
		{
			ki=-1;
			kj=-1;
			kk=-1;
			for (i=1;i<=m;i++)
			for (j=1;j<=n;j++)
			for (k=0;k<4;k++)
			if (!v[i][j][k] && (ki==-1 || d[i][j][k]<d[ki][kj][kk]) )
			{
				ki=i;
				kj=j;
				kk=k;
			}
//			cout<<ki<<' '<<kj<<' '<<kk<<' '<<d[ki][kj][kk]<<endl;
			v[ki][kj][kk]=1;
			cur=d[ki][kj][kk];
			if (kk==0)
			{
				if (cur+2<d[ki-1][kj][2]) d[ki-1][kj][2]=cur+2;
				if (cur+2<d[ki][kj-1][1]) d[ki][kj-1][1]=cur+2;
				tmp=(cur-c[ki][kj])%b[ki][kj];
				if (tmp<0) tmp+=b[ki][kj];
				if (tmp<a[ki][kj])
				{
					if (cur+1<d[ki][kj][2]) d[ki][kj][2]=cur+1;
					if (cur+a[ki][kj]-tmp+1<d[ki][kj][1]) d[ki][kj][1]=cur+a[ki][kj]-tmp+1;
				}
				else
				{
					if (cur+b[ki][kj]-tmp+1<d[ki][kj][2]) d[ki][kj][2]=cur+b[ki][kj]-tmp+1;
					if (cur+1<d[ki][kj][1]) d[ki][kj][1]=cur+1;
				}				
			}
			else if (kk==1)
			{
				if (cur+2<d[ki-1][kj][3]) d[ki-1][kj][3]=cur+2;
				if (cur+2<d[ki][kj+1][0]) d[ki][kj+1][0]=cur+2;
				tmp=(cur-c[ki][kj])%b[ki][kj];
				if (tmp<0) tmp+=b[ki][kj];
				if (tmp<a[ki][kj])
				{
					if (cur+1<d[ki][kj][3]) d[ki][kj][3]=cur+1;
					if (cur+a[ki][kj]-tmp+1<d[ki][kj][0]) d[ki][kj][0]=cur+a[ki][kj]-tmp+1;
				}
				else
				{
					if (cur+b[ki][kj]-tmp+1<d[ki][kj][3]) d[ki][kj][3]=cur+b[ki][kj]-tmp+1;
					if (cur+1<d[ki][kj][0]) d[ki][kj][0]=cur+1;
				}				
			}
			else if (kk==2)
			{
				if (cur+2<d[ki+1][kj][0]) d[ki+1][kj][0]=cur+2;
				if (cur+2<d[ki][kj-1][3]) d[ki][kj-1][3]=cur+2;
				tmp=(cur-c[ki][kj])%b[ki][kj];
				if (tmp<0) tmp+=b[ki][kj];
				if (tmp<a[ki][kj])
				{
					if (cur+1<d[ki][kj][0]) d[ki][kj][0]=cur+1;
					if (cur+a[ki][kj]-tmp+1<d[ki][kj][3]) d[ki][kj][3]=cur+a[ki][kj]-tmp+1;
				}
				else
				{
					if (cur+b[ki][kj]-tmp+1<d[ki][kj][0]) d[ki][kj][0]=cur+b[ki][kj]-tmp+1;
					if (cur+1<d[ki][kj][3]) d[ki][kj][3]=cur+1;
				}				
			}
			else
			{
				if (cur+2<d[ki+1][kj][1]) d[ki+1][kj][1]=cur+2;
				if (cur+2<d[ki][kj+1][2]) d[ki][kj+1][2]=cur+2;
				tmp=(cur-c[ki][kj])%b[ki][kj];
				if (tmp<0) tmp+=b[ki][kj];
				if (tmp<a[ki][kj])
				{
					if (cur+1<d[ki][kj][1]) d[ki][kj][1]=cur+1;
					if (cur+a[ki][kj]-tmp+1<d[ki][kj][2]) d[ki][kj][2]=cur+a[ki][kj]-tmp+1;
				}
				else
				{
					if (cur+b[ki][kj]-tmp+1<d[ki][kj][1]) d[ki][kj][1]=cur+b[ki][kj]-tmp+1;
					if (cur+1<d[ki][kj][2]) d[ki][kj][2]=cur+1;
				}				
			}
		}
		printf("Case #%d: %d\n",ci,d[m][n][3]);
	}
}
