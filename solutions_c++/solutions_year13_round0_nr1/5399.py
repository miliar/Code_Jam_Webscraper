#include <iostream>
#include <cstdio>
using namespace std;

char g[8][8];
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A.out","w",stdout);

	int cas;
	scanf("%d",&cas);
	for (int t=1; t<=cas; t++)
	{
		for (int i=0; i<4; i++) scanf("%s",g[i]);

		bool xwin=false;
		bool owin=false;
		for (int i=0; i<4 && !xwin && !owin; i++)
		{
			xwin=true;
			owin=true;
			for (int j=0; j<4; j++)
			{
				if (g[i][j]=='O' || g[i][j]=='.') xwin=false;
				if (g[i][j]=='X' || g[i][j]=='.') owin=false;
			}
		}
		for (int i=0; i<4 && !xwin && !owin; i++)
		{
			xwin=true;
			owin=true;
			for (int j=0; j<4; j++)
			{
				if (g[j][i]=='O' || g[j][i]=='.') xwin=false;
				if (g[j][i]=='X' || g[j][i]=='.') owin=false;
			}
		}
		if (!xwin && !owin)
		{
			xwin=true;
			owin=true;
		    for (int i=0; i<4; i++)
		    {
		    	if (g[i][i]=='O' || g[i][i]=='.') xwin=false;
		    	if (g[i][i]=='X' || g[i][i]=='.') owin=false;
		    }
		} 
		if (!xwin && !owin)
		{
			xwin=true;
			owin=true;
		    for (int i=0; i<4; i++)
		    {
		    	if (g[i][3-i]=='O' || g[i][3-i]=='.') xwin=false;
		    	if (g[i][3-i]=='X' || g[i][3-i]=='.') owin=false;
		    }
		}
		printf("Case #%d: ",t);
		if (xwin) puts("X won");
		else if (owin) puts("O won");
		else
		{
			bool full=true;
			for (int i=0; i<4; i++)
				for (int j=0; j<4; j++) if (g[i][j]=='.')
					full=false;
			if (full) puts("Draw");
			else puts("Game has not completed");
		}
	}
	return 0;
}