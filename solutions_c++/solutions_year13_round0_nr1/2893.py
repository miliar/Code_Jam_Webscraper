#include <stdio.h>
#include <stdlib.h>

int T;
char map[7][7];

int main()
{
	int i,j,ti;
	#ifndef ONLINE_JUDGE
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	#endif
	scanf("%d",&T);
	for(ti=1;ti<=T;++ti)
	{
		for(i=1;i<=4;++i)
			scanf("%s",map[i]+1);
		// X
		char ans='T',flag;
		for(i=1;i<=4;++i)
		{
			flag='T';
			for(j=1;j<=4;++j)
			{
				if(map[i][j]=='.') break;
				if(map[i][j]!='T')
				{
					if(flag=='T')
						flag=map[i][j];
					if(flag!=map[i][j])
						break;
				}
			}
			if(j>4 && flag!='T')
			{
				ans=flag;
				break;
			}
		}
		if(ans!='T')
		{
			printf("Case #%d: %c won\n",ti,ans);
			continue;
		}
		// Y
		for(j=1;j<=4;++j)
		{
			flag='T';
			for(i=1;i<=4;++i)
			{
				if(map[i][j]=='.') break;
				if(map[i][j]!='T')
				{
					if(flag=='T')
						flag=map[i][j];
					if(flag!=map[i][j])
						break;
				}
			}
			if(i>4 && flag!='T')
			{
				ans=flag;
				break;
			}
		}
		if(ans!='T')
		{
			printf("Case #%d: %c won\n",ti,ans);
			continue;
		}
		// Xie
		flag='T';
		for(i=1;i<=4;++i)
		{
			if(map[i][i]=='.') break;
			if(map[i][i]!='T')
			{
				if(flag=='T')
					flag=map[i][i];
				if(flag!=map[i][i])
					break;
			}
		}
		if(i>4 && flag!='T')
		{
			ans=flag;
		}
		if(ans!='T')
		{
			printf("Case #%d: %c won\n",ti,ans);
			continue;
		}
		// Xie2
		flag='T';
		for(i=1;i<=4;++i)
		{
			if(map[i][5-i]=='.') break;
			if(map[i][5-i]!='T')
			{
				if(flag=='T')
					flag=map[i][5-i];
				if(flag!=map[i][5-i])
					break;
			}
		}
		if(i>4 && flag!='T')
		{
			ans=flag;
		}
		if(ans!='T')
		{
			printf("Case #%d: %c won\n",ti,ans);
			continue;
		}
		int p=0;
		for(i=1;i<=4;++i)
		{
			for(j=1;j<=4;++j)
				if(map[i][j]=='.')
				{
					p=1;
					break;
				}
			if(p==1) break;
		}
		if(p==0)
			printf("Case #%d: Draw\n",ti);
		else
			printf("Case #%d: Game has not completed\n",ti);
	}
	return 0;
}