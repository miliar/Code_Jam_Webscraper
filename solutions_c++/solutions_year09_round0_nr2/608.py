#include<iostream>
using namespace std;

int f[101*101+1];
int a[101][101];
char b[101*101+1];
int h,w;


int find(int x)
{
	if (f[x]!=x)
	{
		int t=find(f[x]);
		f[x]=t;
		return t;
	}
	else
		return x;
}

int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int T1=1;T1<=T;T1++)
	{
		char ch='a'-1;
		memset(b,0,sizeof(b));
		scanf("%d%d",&h,&w);
		for (int i=0;i<h;i++)
			for (int j=0;j<w;j++)
				scanf("%d",&a[i][j]);
		for (int i=0;i<h;i++)
			for (int j=0;j<w;j++)
				f[i*w+j]=i*w+j;
		for (int i=0;i<h;i++)
			for (int j=0;j<w;j++)
			{
				int minl=100000000,use=0;
				if (i>0 && minl>a[i-1][j])
				{
					use=(i-1)*w+j;
					minl=a[i-1][j];
				}
				if (j>0 && minl>a[i][j-1])
				{
					use=i*w+j-1;
					minl=a[i][j-1];
				}
				if (j<w-1 && minl>a[i][j+1])
				{
					use=i*w+j+1;
					minl=a[i][j+1];
				}
				if (i<h-1 && minl>a[i+1][j])
				{
					use=(i+1)*w+j;
					minl=a[i+1][j];
				}
				if (minl<a[i][j])
				{
					int f1=find(i*w+j),f2=find(use);
					if (f1!=f2)
						f[f2]=f1;
				}
			}
		printf("Case #%d:\n",T1);
		for (int i=0;i<h;i++)
			for (int j=0;j<w;j++)
			{
				int fa=find(i*w+j);
				if (!b[fa])
					b[fa]=++ch;
				printf("%c",b[fa]);
				if (j==w-1)
					printf("\n");
				else
					printf(" ");
			}
	}
}