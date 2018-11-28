#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
char map[4][4];
int cnt[8];
int main()
{
	int n,cas,ans;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	while(~scanf("%d",&n))
	{
		cas=1;
		while(n--)
		{
			for(int i=0;i<4;++i)
			{
				scanf("%s",map[i]);
			}
			ans=-1;
			for(int i=0;i<4;++i)
			{
				memset(cnt,0,sizeof(cnt));
				for(int j=0;j<4;++j)
				{
					if(map[i][j]=='X'||map[i][j]=='T'){++cnt[0];}
					if(map[j][i]=='X'||map[i][j]=='T'){++cnt[1];}
					if(map[i][j]=='O'||map[i][j]=='T'){++cnt[2];}
					if(map[j][i]=='O'||map[i][j]=='T'){++cnt[3];}
				}
				if(cnt[0]==4||cnt[1]==4){ans=0;break;}
				if(cnt[2]==4||cnt[3]==4){ans=1;break;}
			}
			for(int i=0;i<4;++i)
			{
				if(map[i][i]=='X'||map[i][i]=='T'){++cnt[4];}
				if(map[i][3-i]=='X'||map[i][3-i]=='T'){++cnt[5];}

				if(map[i][i]=='O'||map[i][i]=='T'){++cnt[6];}
				if(map[i][3-i]=='O'||map[i][3-i]=='T'){++cnt[7];}
			}
			if(cnt[4]==4||cnt[5]==4){ans=0;}
			if(cnt[6]==4||cnt[7]==4){ans=1;}
			if(ans==-1)
			{
				for(int i=0;i<4;++i)
				{
					for(int j=0;j<4;++j)
					{
						if(map[i][j]=='.'){ans=2;break;}
					}
					if(ans==2){break;}
				}	
			}
			if(ans==-1)printf("Case #%d: Draw\n",cas);
			else if(ans==0)printf("Case #%d: X won\n",cas);
			else if(ans==1)printf("Case #%d: O won\n",cas);
			else printf("Case #%d: Game has not completed\n",cas);
			++cas;
		}
	}
	return 0;
}
