//North, West, East, South.
#include<iostream>
using namespace std;

int cx[4]={-1,0,0,1};
int cy[4]={0,-1,1,0};

int mp[110][110];
int ck[110][110];
int tox[110][110];
int toy[110][110];

int t,x,y;

int mark(int i,int j, int be)
{
	if(ck[i][j]!=0)
		return ck[i][j];
	if(tox[i][j]==-1)
	{
		ck[i][j]=be;
		return ck[i][j];
	}
	ck[i][j]=mark(tox[i][j],toy[i][j],be);
	return ck[i][j];
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int i,j,k,cas=1,tx,ty,mi;
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d:\n",cas);
		cas++;
		scanf("%d%d",&x,&y);
		memset(ck,0,sizeof(ck));
		memset(tox,-1,sizeof(tox));
		memset(toy,-1,sizeof(toy));
		for(i=0;i<x;i++)
			for(j=0;j<y;j++)
				scanf("%d",&mp[i][j]);
		for(i=0;i<x;i++)
			for(j=0;j<y;j++)
			{
				tx=-1;ty=-1;mi=100000;
				for(k=0;k<4;k++)
				{
					if(i+cx[k]<x&&i+cx[k]>=0&&j+cy[k]<y&&j+cy[k]>=0)
					{
						if(mp[i+cx[k]][j+cy[k]]<mp[i][j]&&mp[i+cx[k]][j+cy[k]]<mi)
						{
							tx=i+cx[k];ty=j+cy[k];mi=mp[i+cx[k]][j+cy[k]];
						}
					}
				}
				if(tx!=-1)
					tox[i][j]=tx;
				if(ty!=-1)
					toy[i][j]=ty;
			}
		int be='a';
		for(i=0;i<x;i++)
			for(j=0;j<y;j++)
			{
				if(ck[i][j]==0)
				{
					if(mark(i,j,be)==be)
						be++;
				}
			}
		for(i=0;i<x;i++)
		{
			for(j=0;j<y;j++)
				printf("%c ",ck[i][j]);
			printf("\n");
		}
	}
	return 0;
}

				


