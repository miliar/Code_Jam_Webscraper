#include <cstdio>

char mp[60][60];
int r,c;

inline bool inbound(int x,int y)
{
	return x>=0 && x<r && y>=0 && y<c;
}

bool put(int x,int y)
{
	if(!inbound(x,y) || !inbound(x+1,y) || !inbound(x+1,y+1) || !inbound(x,y+1))
		return false;
	if(mp[x][y]!='#' || mp[x+1][y]!='#' || mp[x][y+1]!='#' || mp[x+1][y+1]!='#')
		return false;
	mp[x][y]='/';
	mp[x][y+1]='\\';
	mp[x+1][y]='\\';
	mp[x+1][y+1]='/';
	return true;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,ca=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&r,&c);
		int i,j;
		for(i=0;i<r;i++)
			scanf("%s",mp[i]);
		bool flag=false;
		for(i=0;i<r && !flag;i++)
		{
			for(j=0;j<c && !flag;j++)
			{
				if(mp[i][j]=='#' && !put(i,j)) flag=true;
			}
		}
		printf("Case #%d:\n",ca++);
		if(flag) printf("Impossible\n");
		else
		{
			for(i=0;i<r;i++)
				printf("%s\n",mp[i]);
		}
	}
	return 0;
}