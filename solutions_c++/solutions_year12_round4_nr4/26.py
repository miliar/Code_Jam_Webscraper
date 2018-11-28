#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;

char m[100][100],m1[100][100];
int a[10000],b[10000],oa[10000],ob[10000];

int go(int a,int b)
{
	if (m1[a][b]!='.') return 0;
	m1[a][b]='x';
	return 1+go(a,b-1)+go(a,b+1)+go(a-1,b);
}

int main()
{
	int _cn,_cc,i,j,r,c,k,ma,nn,n,kk;
	int q[10],w[10];
	scanf("%d\n",&_cn);
	for (_cc=1;_cc<=_cn;++_cc)
	{
		scanf("%d %d\n",&r,&c);
		for (i=0;i<r;++i) gets(m[i]);
		ma=-1;
		for (i=0;i<r;++i) for (j=0;j<c;++j) if (m[i][j]>='0' && m[i][j]<='9')
		{
			if (m[i][j]-'0'>ma) ma=m[i][j]-'0';
			q[m[i][j]-'0']=i;
			w[m[i][j]-'0']=j;
		}
		for (i=0;i<r;++i) for (j=0;j<c;++j) if (m[i][j]>='0' && m[i][j]<='9') m[i][j]='.';
		printf("Case #%d:\n",_cc);
		for (k=0;k<=ma;++k)
		{
			memcpy(m1,m,sizeof(m));
			n=nn=go(q[k],w[k]);
			kk=0;
			for (i=0;i<r;++i) for (j=0;j<c;++j) if (m1[i][j]=='x')
			{
				a[kk]=i;
				b[kk]=j;
				++kk;
			}
			while (1)
			{
				memcpy(oa,a,n*sizeof(int));
				memcpy(ob,b,n*sizeof(int));
				for (j=0;j<c;++j)
				{
					for (i=0;i<n;++i) if (a[i]!=q[k] || b[i]!=w[k]) break;
					if (i==n) break;
					for (i=0;i<n;++i) if (m1[a[i]+1][b[i]]=='.') break;
					if (i==n) for (i=0;i<n;++i) if (m1[a[i]+1][b[i]]!='#') { ++a[i]; }
					for (i=0;i<n;++i) if (m1[a[i]][b[i]-1]=='.') break;
					if (i==n) for (i=0;i<n;++i) if (m1[a[i]][b[i]-1]!='#') { --b[i]; }
				}
				for (j=0;j<c;++j)
				{
					for (i=0;i<n;++i) if (a[i]!=q[k] || b[i]!=w[k]) break;
					if (i==n) break;
					for (i=0;i<n;++i) if (m1[a[i]+1][b[i]]=='.') break;
					if (i==n) for (i=0;i<n;++i) if (m1[a[i]+1][b[i]]!='#') { ++a[i]; }
					for (i=0;i<n;++i) if (m1[a[i]][b[i]+1]=='.') break;
					if (i==n) for (i=0;i<n;++i) if (m1[a[i]][b[i]+1]!='#') { ++b[i]; }
				}
				for (i=0;i<n;++i) if (a[i]!=q[k] || b[i]!=w[k]) break;
				if (i==n) break;
//				printf("> %d %d\n",q[k],w[k]);
				for (i=0;i<n;++i) 
				{
//					printf(">%d %d\n",a[i],b[i]);
					if (a[i]!=oa[i] || b[i]!=ob[i]) break;
				}
//				printf("---\n");
				if (i==n)
				{
					i=0;
					break;
				}
				for (i=0;i<n;++i) for (j=i+1;j<n;++j) if (a[i]==a[j] && b[i]==b[j])
				{
					--n;
					a[j]=a[n];
					b[j]=b[n];
					--j;
				}
			}
			printf("%d: %d %s\n",k,nn,i==n?"Lucky":"Unlucky");
		}
	}
	return 0;
}
