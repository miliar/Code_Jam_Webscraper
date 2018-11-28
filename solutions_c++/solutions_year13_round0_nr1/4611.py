#include <cstdio>
#include<algorithm>
#include <queue>

#define FORN(i,a,b) for (int i = (a); i <= (b); i++)
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define S ({int x; scanf("%d%*c", &x); x;})
#define PN(x) ({printf("%d\n", x);})
#define PS(x) ({printf("%d ", x);})
#define NL ({printf("\n");})
#define printarr(i, x, y) ({for(int i=0;i<y;i++){ printf("%d ", x[i]);} printf("\n");})
#define inputarr(i, x, y) ({for(int i=0;i<y;i++){ scanf("%d", &x[i]);}})
#define MOD 1000000007
#define LL long long

using namespace std;
int main()
{
	int n5;
	scanf("%d", &n5);
	int casenum=0;
	while(n5--)
	{
		scanf("%*c");
		casenum++;
		int x=0,o=0,t=0,flag=0, tog=0;
		char arr[4][4];
		FOR(i,0,4)
		{
			FOR(j,0,4)
			{
				scanf("%c", &arr[i][j]);
				if(arr[i][j]=='.')
					tog=1;
			//	printf("%c", arr[i][j]);
			}
			scanf("%*c");
		}
		FOR(i,0,4)
		{
			x=t=o=0;
			FOR(j,0,4)
			{
				if(arr[i][j]=='O')
					o++;
				else if(arr[i][j]=='X')
					x++;
				else if(arr[i][j]=='T')
				{
					o++; x++;
				}
			}
			if(x==4)
			{
				flag=1;
				printf("Case #%d: X won\n", casenum);
				break;
			}
			else if(o==4)
			{
				flag=1;
				printf("Case #%d: O won\n", casenum);
				break;
			}
		}
		if(flag)
			continue;
		FOR(i,0,4)
		{
			x=t=o=0;
			FOR(j,0,4)
			{
				if(arr[j][i]=='O')
					o++;
				else if(arr[j][i]=='X')
					x++;
				else if(arr[j][i]=='T')
				{
					o++; x++;
				}
			}
			if(x==4)
			{
				flag=1;
				printf("Case #%d: X won\n", casenum);
				break;
			}
			else if(o==4)
			{
				flag=1;
				printf("Case #%d: O won\n", casenum);
				break;
			}
		}
		if(flag)
			continue;
		x=t=o=0;
		FOR(i,0,4)
		{
			if(arr[i][i]=='O')
				o++;
			else if(arr[i][i]=='X')
				x++;
			else if(arr[i][i]=='T')
			{
				o++; x++;
			}
		}
		if(x==4)
		{
			flag=1;
			printf("Case #%d: X won\n", casenum);
		}
		else if(o==4)
		{
			flag=1;
			printf("Case #%d: O won\n", casenum);
		}
		if(flag)
			continue;
		x=t=o=0;
		for(int i=3; i>=0; i--)
		{
			if(arr[i][3-i]=='O')
				o++;
			else if(arr[i][3-i]=='X')
				x++;
			else if(arr[i][3-i]=='T')
			{
				o++; x++;
			}
		}
		if(x==4)
		{
			flag=1;
			printf("Case #%d: X won\n", casenum);
		}
		else if(o==4)
		{
			flag=1;
			printf("Case #%d: O won\n", casenum);
		}
		if(!flag)
		{
			if(tog)
				printf("Case #%d: Game has not completed\n", casenum);
			else
				printf("Case #%d: Draw\n", casenum);
		}
	}
	return 0;
}
