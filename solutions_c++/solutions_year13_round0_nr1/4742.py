#include <cstdio>
#include <memory.h>
using namespace std;
int max(int a,int b)
{
	return a>b?a:b;
}
int main()
{
	int T;
	char s[4][5];
	freopen("A-large.in","r",stdin);
	freopen("Aoutlarge","w",stdout);
	scanf("%d",&T);
	for (int c=1;c<=T;++c)
	{
		gets(s[0]);
		gets(s[0]);
		gets(s[1]);
		gets(s[2]);
		gets(s[3]);

		int xnum=0,onum=0,tnum=0;
		int win=0;
		bool f=false;
		for(int i=0;i<4;++i)
		{
			xnum=0,onum=0,tnum=0;
			for (int j=0;j<4;++j)
			{
				switch(s[i][j])
				{
				case 'X':
					++xnum;
					break;
				case 'O':
					++onum;
					break;
				case 'T':
					++tnum;
					break;
				case '.':
					f=true;
					break;
				}
			}

			if(xnum+tnum==4)
			{
				win=1;
				break;
			}
			if (onum+tnum==4)
			{
				win=2;
				break;
			}
		}
		if(win==1)
		{
			printf("Case #%d: X won\n",c);
			continue;
		}
		else
		{
			if(win==2)
			{
				printf("Case #%d: O won\n",c);
				continue;
			}
		}


		for(int j=0;j<4;++j)
		{
			xnum=0,onum=0,tnum=0;
			for (int i=0;i<4;++i)
			{
				switch(s[i][j])
				{
				case 'X':
					++xnum;
					break;
				case 'O':
					++onum;
					break;
				case 'T':
					++tnum;
					break;
				}
			}

			if(xnum+tnum==4)
			{
				win=1;
				break;
			}
			if (onum+tnum==4)
			{
				win=2;
				break;
			}
		}
		if(win==1)
		{
			printf("Case #%d: X won\n",c);
			continue;
		}
		else
		{
			if(win==2)
			{
				printf("Case #%d: O won\n",c);
				continue;
			}
		}

		xnum=0,onum=0,tnum=0;
		for (int i=0;i<4;++i)
		{
			switch(s[i][i])
			{
			case 'X':
				++xnum;
				break;
			case 'O':
				++onum;
				break;
			case 'T':
				++tnum;
				break;
			}
		}

		if(xnum+tnum==4)
		{
			printf("Case #%d: X won\n",c);
			continue;
		}
		if (onum+tnum==4)
		{
			printf("Case #%d: O won\n",c);
			continue;
		}

		xnum=0,onum=0,tnum=0;
		for (int i=0;i<4;++i)
		{
			switch(s[i][3-i])
			{
			case 'X':
				++xnum;
				break;
			case 'O':
				++onum;
				break;
			case 'T':
				++tnum;
				break;
			}
		}

		if(xnum+tnum==4)
		{
			printf("Case #%d: X won\n",c);
			continue;
		}
		if (onum+tnum==4)
		{
			printf("Case #%d: O won\n",c);
			continue;
		}

		if(!f)
		{
			printf("Case #%d: Draw\n",c);
		}
		else
		{
			printf("Case #%d: Game has not completed\n",c);
		}
	}
}