#include<stdio.h>
#include<string.h>

int H,C;
int gr[100][100];
bool visited[100][100];
char name[100][100];

#include<stdio.h>
#include<string.h>

const int SIZE=50001;
int p[SIZE],rank[SIZE];

void makeset(int x)
{
	p[x]=x;
	rank[x]=0;
}

int findset(int x)
{
	if(x!=p[x])
		p[x]=findset(p[x]);
	return p[x];
}

void Union(int x,int y)
{
	int rx=findset(x),ry=findset(y);
	if(rank[rx]>rank[ry])
		p[ry]=rx;
	else
	{
		p[rx]=ry;
		if(rank[rx]=rank[ry])
			rank[ry]++;
	}   
}

inline int ID(int i,int j)
{
	return i*C+j;
}

int dx[4]={-1,0,0,1},dy[4]={0,-1,1,0};

bool valid(int r,int c)
{
	return 0<=r&&r<H&&0<=c&&c<C;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int kase=1;kase<=t;kase++)
	{
		printf("Case #%d:\n",kase);
		scanf("%d%d",&H,&C);
		for(int i=0;i<H;i++)
			for(int j=0;j<C;j++)
				scanf("%d",&gr[i][j]);
		for(int i=0;i<H*C;i++)
			makeset(i);
		for(int i=0;i<H;i++)
			for(int j=0;j<C;j++)
			{
				int minh=gr[i][j],minid;
				for(int k=0;k<4;k++)
				{
					int ni=i+dx[k],nj=j+dy[k];
					if(valid(ni,nj)&&gr[ni][nj]<minh)
						minh=gr[ni][nj],minid=ID(ni,nj);
				}
				if(minh!=gr[i][j])
				{
					//printf("%d %d\n",ID(i,j),minid);
					Union(ID(i,j),minid);
				}
			}
		int cnt=0;
		for(int i=0;i<H*C;i++)
			if(p[i]==i)
				cnt++;
		//printf("%d\n",cnt);
		memset(visited,0,sizeof(visited));
		for(int i=0;i<cnt;i++)
		{
			for(int j=0;j<H;j++)
				for(int k=0;k<C;k++)
					if(!visited[j][k])
					{
						visited[j][k]=true;
						name[j][k]=i+'a';
						for(int ii=0;ii<H;ii++)
							for(int jj=0;jj<C;jj++)
								if(findset(ID(j,k))==findset(ID(ii,jj)))
								{
									name[ii][jj]=name[j][k];
									visited[ii][jj]=true;
								}
						goto end;
					}
end:		;
		}
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<C-1;j++)
				printf("%c ",name[i][j]);
			printf("%c\n",name[i][C-1]);;
		}
	}
	return 0;
}