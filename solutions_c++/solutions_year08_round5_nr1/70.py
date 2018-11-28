#include<stdio.h>
#include<memory>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> my[6020],you[6020];
int kk[4][2]={0,1,1,0,0,-1,-1,0};
bool z[6020][6020];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int c,o,i,j,k,f,n,x,y,ans;
	char str[128];
	scanf("%d",&c);
	for(o=1;o<=c;o++)
	{
		memset(z,0,sizeof(z));
		for(i=0;i<6020;i++)
		{
			my[i].clear();
			you[i].clear();
		}
		scanf("%d",&n);
		x=3010;
		y=3010;
		k=0;
		while(n--)
		{
			scanf("%s%d",str,&f);
			while(f--)
			{
				for(i=0;str[i];i++)
				{
					if(str[i]=='R')
						k=(k+1)%4;
					else if(str[i]=='L')
						k=(k+3)%4;
					else
					{
						if(!k)
							my[y].push_back(x);
						else if(k==1)
							you[x].push_back(y);
						else if(k==2)
							my[y-1].push_back(x);
						else
							you[x-1].push_back(y);
						x+=kk[k][0];
						y+=kk[k][1];
					}
				}
			}
		}
		for(i=0;i<6020;i++)
		{
			if(my[i].size())
				sort(my[i].begin(),my[i].end());
			if(you[i].size())
				sort(you[i].begin(),you[i].end());
		}
		for(i=0;i<6020;i++)
			for(j=1;j+1<my[i].size();j+=2)
				for(x=my[i][j];x<my[i][j+1];x++)
					z[x][i]=true;
		for(i=0;i<6020;i++)
			for(j=1;j+1<you[i].size();j+=2)
				for(y=you[i][j];y<you[i][j+1];y++)
					z[i][y]=true;
		ans=0;
		for(i=0;i<6020;i++)
			for(j=0;j<6020;j++)
				ans+=z[i][j];
		printf("Case #%d: %d\n",o,ans);
	}
	return 0;
}

