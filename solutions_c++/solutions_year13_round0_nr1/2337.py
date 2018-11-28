#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;

char bn[5][5];

void solve()
{
	memset(bn,0,sizeof(bn));
	for(int i=0;i<4;i++) scanf("%s",&bn[i]);
	for(int i=0;i<4;i++)
	{
		bool up=true;
		char c=bn[i][0];
		for(int j=1;j<4;j++)
		{
			if(c=='T') c=bn[i][j];
			if(c!=bn[i][j]&&bn[i][j]!='T')
			{
				up=false;
				break;
			}
		}
		if(up&&c!='.')
		{
			printf("%c won\n",c);
			return;
		}
	}
	for(int i=0;i<4;i++)
	{
		bool up=true;
		char c=bn[0][i];
		for(int j=1;j<4;j++)
		{
			if(c=='T') c=bn[j][i];
			if(c!=bn[j][i]&&bn[j][i]!='T')
			{
				up=false;
				break;
			}
		}
		if(up&&c!='.')
		{
			printf("%c won\n",c);
			return;
		}
	}
	for(int i=0;i<4;i++)
	{
		bool up=true;
		char c=bn[0][0];
		for(int j=1;j<4;j++)
		{
			if(c=='T') c=bn[j][j];
			if(c!=bn[j][j]&&bn[j][j]!='T')
			{
				up=false;
				break;
			}
		}
		if(up&&c!='.')
		{
			printf("%c won\n",c);
			return;
		}
	}
	for(int i=0;i<4;i++)
	{
		bool up=true;
		char c=bn[0][3];
		for(int j=1;j<4;j++)
		{
			if(c=='T') c=bn[j][3-j];
			if(c!=bn[j][3-j]&&bn[j][3-j]!='T')
			{
				up=false;
				break;
			}
		}
		if(up&&c!='.')
		{
			printf("%c won\n",c);
			return;
		}
	}
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(bn[i][j]=='.')
			{
				printf("Game has not completed\n");
				return;
			}
		}
	}
	printf("Draw\n");
	return;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
