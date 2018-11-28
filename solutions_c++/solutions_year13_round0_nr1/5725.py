#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

char t[10][10];
int main()
{
	freopen("A.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int cas=0;
	while (T--)
	{
		for (int i=0;i<4;i++)
			scanf("%s",t[i]);
		printf("Case #%d: ",++cas);
		bool flag=false;
		for (int i=0;i<4;i++)
		{
			if (t[i][0]=='.' || t[i][1]=='.') continue;
			char hey=t[i][0];
			if (hey=='T') hey=t[i][1];
			int p=0;
			for (int j=0;j<4;j++)
			{
				if (t[i][j]==hey) p++;
				else if (t[i][j]=='T') p++;
			}
			if (p==4)
			{
				flag=true;
				printf("%c won\n",hey);
				break;
			} 
		}
		if (flag) continue;
		for (int i=0;i<4;i++)
		{
			if (t[0][i]=='.' || t[1][i]=='.') continue;
			char hey=t[0][i];
			if (hey=='T') hey=t[1][i];
			int p=0;
			for (int j=0;j<4;j++)
			{
				if (t[j][i]==hey) p++;
				else if (t[j][i]=='T') p++;
			}
			if (p==4)
			{
				flag=true;
				printf("%c won\n",hey);
				break;
			} 
		}
		if (t[0][0]!='.' && t[1][1]!='.')
		{
			char hey=t[0][0];
			if (hey=='T') hey=t[1][1];
			int p=0;
			for (int i=0;i<4;i++)
			{
				if (t[i][i]==hey) p++;
				else if (t[i][i]=='T') p++;
			}
			if (p==4)
			{
				flag=true;
				printf("%c won\n",hey);
				continue;
			} 
		}
		if (t[0][3]!='.' && t[1][2]!='.')
		{
			char hey=t[0][3];
			if (hey=='T') hey=t[1][2];
			int p=0;
			for (int i=0;i<4;i++)
			{
				if (t[i][3-i]==hey) p++;
				else if (t[i][3-i]=='T') p++;
			}
			if (p==4)
			{
				flag=true;
				printf("%c won\n",hey);
				continue;
			} 
		}
		if (flag) continue;
		int now=0;
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++)
				if (t[i][j]!='.') now++;
		if (now!=16) puts("Game has not completed");
		else puts("Draw");
	}	
}