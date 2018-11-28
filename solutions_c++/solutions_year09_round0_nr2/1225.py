#include<iostream>
#include<string.h>
using namespace std;
int n,m;
int a[200][200];
int uset[40000];
int hash[40000];
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
int init()
{
	for(int i=0;i<n*m;++i)
		uset[i]=i;
	return 0;
}

int root(int k)
{
	if(k==uset[k])return k;
	return uset[k]=root(uset[k]);
}

int main()
{
	int cases,t;
	scanf("%d",&cases);
	for(int t=1;t<=cases;++t)
	{
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
				scanf("%d",&a[i][j]);
		init();
		for(int i=0;i<n;++i)
		{
			for(int j=0;j<m;++j)
			{
				int p=-1;
				int v=-1;
				for(int k=0;k<4;++k)
				{
					int x=i+dx[k];
					int y=j+dy[k];
					if(x>=0&&x<n&&y>=0&&y<m)
					{
						if(a[x][y]<a[i][j])
						{
							if(p==-1||a[x][y]<v)
							{
								p=k;
								v=a[x][y];
							}
						}
					}
				}
				if(p!=-1)
				{
//					printf("%d %d-->%d %d\n",i,j,i+dx[p],j+dy[p]);
					int s1=i*m+j;
					int s2=(i+dx[p])*m+j+dy[p];
					s1=root(s1);
					s2=root(s2);
					if(s1!=s2)
						uset[s1]=s2;
				}
			}
		}
		memset(hash,0,sizeof(hash));
		char c='a';
		printf("Case #%d:\n",t);
		for(int i=0;i<n;++i)
		{
			for(int j=0;j<m;++j)
			{
				if(j)printf(" ");
				int k=root(i*m+j);
				if(hash[k]==0)
					hash[k]=c++;
				printf("%c",hash[k]);
				//printf("%d",k);
			}
			printf("\n");
		}
	}
	return 0;
}
