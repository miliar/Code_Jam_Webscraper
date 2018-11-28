#include<iostream>
#include<string.h>
using namespace std;
#define N 105
int n,m,level;
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
int a[N][N];
int r[N][N];
bool vist[N][N];
bool judge(int x,int y)
{
	if(x<0||x>=n||y<0||y>=m)
		return false;
	return true;
}

int dfs(int i,int j)
{
	if(r[i][j]>0)
		return r[i][j];
    int k,pos;
	int max=a[i][j];
	bool flag=false;
	for(k=0;k<4;k++)
    {
        if(judge(i+dx[k],j+dy[k])&&a[i+dx[k]][j+dy[k]]<max)
		{
             flag=true;
			 max=a[i+dx[k]][j+dy[k]];
			 pos=k;
        }
	}
	if(!flag)
	{
		r[i][j]=level;
		level++;
		return r[i][j];
	}
	else
	{
		dfs(i+dx[pos],j+dy[pos]);
	}
}

int main()
{
	int i,j,t,count=0;
	FILE *in,*out;
	in=fopen("inb2.in","r");
	out=fopen("outb2.txt","w");
	fscanf(in,"%d",&t);
	while(t>0)
	{
		t--;
		fscanf(in,"%d%d",&n,&m);
		count++;
		level=1;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				fscanf(in,"%d",&a[i][j]);
				r[i][j]=0;
			}
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				r[i][j]=dfs(i,j);
			}
		}
		fprintf(out,"Case #%d:\n",count);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				fprintf(out,"%c",(char)(r[i][j]+'a'-1));
				if(j==m-1)
					fprintf(out,"\n");
				else
					fprintf(out," ");
			}
		}
	}
	return 0;
}