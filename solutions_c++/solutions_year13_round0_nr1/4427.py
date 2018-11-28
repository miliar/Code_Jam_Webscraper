/*	Jayesh Lahori	    */
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>

using namespace std;

/* General Declarations */

#define INF		1000000007
#define LL		long long int
#define SI(n)		scanf("%lld",&n);
#define SC(c)		scanf("%c",&c);
#define SS(s)		scanf("%s",s);
#define FOR(x,a,b)	for(LL x=a;x<b;x++)
#define REP(i,n)	for(LL i=0;i<n;i++)
#define MP		make_pair
#define PB		push_back


/* Container's */

#define	VI		vector<LL>
#define PLL             pair<LL,LL>  /* A Single Pair  */
#define VP		vector<PLL> /* Vector of Pairs */
#define VS		vector<string>
#define VVI		vector<VI>
#define VVS		vector<VS>

int main()
{
	LL tc,cpy;
	SI(tc);
	cpy=tc;
	char board[4][4];
	char c,d;
	SC(c);
	LL ct=0;
	while(tc--)
	{
		ct=0;
		for(LL i=0;i<4;i++)
		{
			for(LL j=0;j<4;j++)
			{
				SC(c);
				if(c=='.')
					ct++;
				board[i][j]=c;
			}
			SC(d);
		}
		SC(d);

		// row cases;

		if((board[0][0]=='O' || board[0][0]=='T') && (board[0][1]=='O' || board[0][1]=='T') && (board[0][2]=='O' || board[0][2]=='T') && (board[0][3]=='O' || board[0][3]=='T'))
		{
			printf("Case #%lld: O won\n",cpy-tc);
			continue;
		}

		if((board[0][0]=='X' || board[0][0]=='T') && (board[0][1]=='X' || board[0][1]=='T') && (board[0][2]=='X' || board[0][2]=='T') && (board[0][3]=='X' || board[0][3]=='T'))
		{
			printf("Case #%lld: X won\n",cpy-tc);
			continue;
		}

		if((board[1][0]=='O' || board[1][0]=='T') && (board[1][1]=='O' || board[1][1]=='T') && (board[1][2]=='O' || board[1][2]=='T') && (board[1][3]=='O' || board[1][3]=='T'))
		{
			printf("Case #%lld: O won\n",cpy-tc);
			continue;
		}

		if((board[1][0]=='X' || board[1][0]=='T') && (board[1][1]=='X' || board[1][1]=='T') && (board[1][2]=='X' || board[1][2]=='T') && (board[1][3]=='X' || board[1][3]=='T'))
		{
			printf("Case #%lld: X won\n",cpy-tc);
			continue;
		}

		if((board[2][0]=='O' || board[2][0]=='T') && (board[2][1]=='O' || board[2][1]=='T') && (board[2][2]=='O' || board[2][2]=='T') && (board[2][3]=='O' || board[2][3]=='T'))
		{
			printf("Case #%lld: O won\n",cpy-tc);
			continue;
		}

		if((board[2][0]=='X' || board[2][0]=='T') && (board[2][1]=='X' || board[2][1]=='T') && (board[2][2]=='X' || board[2][2]=='T') && (board[2][3]=='X' || board[2][3]=='T'))
		{
			printf("Case #%lld: X won\n",cpy-tc);
			continue;
		}

		if((board[3][0]=='O' || board[3][0]=='T') && (board[3][1]=='O' || board[3][1]=='T') && (board[3][2]=='O' || board[3][2]=='T') && (board[3][3]=='O' || board[3][3]=='T'))
		{
			printf("Case #%lld: O won\n",cpy-tc);
			continue;
		}

		if((board[3][0]=='X' || board[3][0]=='T') && (board[3][1]=='X' || board[3][1]=='T') && (board[3][2]=='X' || board[3][2]=='T') && (board[3][3]=='X' || board[3][3]=='T'))
		{
			printf("Case #%lld: X won\n",cpy-tc);
			continue;
		}
		// Col Cases;

		if((board[0][0]=='O' || board[0][0]=='T') && (board[1][0]=='O' || board[1][0]=='T') && (board[2][0]=='O' || board[2][0]=='T') && (board[3][0]=='O' || board[3][0]=='T'))
		{
			printf("Case #%lld: O won\n",cpy-tc);
			continue;
		}

		if((board[0][0]=='X' || board[0][0]=='T') && (board[1][0]=='X' || board[1][0]=='T') && (board[2][0]=='X' || board[2][0]=='T') && (board[3][0]=='X' || board[3][0]=='T'))
		{
			printf("Case #%lld: X won\n",cpy-tc);
			continue;
		}

		if((board[0][1]=='O' || board[0][1]=='T') && (board[1][1]=='O' || board[1][1]=='T') && (board[2][1]=='O' || board[2][1]=='T') && (board[3][1]=='O' || board[3][1]=='T'))
		{
			printf("Case #%lld: O won\n",cpy-tc);
			continue;
		}

		if((board[0][1]=='X' || board[0][1]=='T') && (board[1][1]=='X' || board[1][1]=='T') && (board[2][1]=='X' || board[2][1]=='T') && (board[3][1]=='X' || board[3][1]=='T'))
		{
			printf("Case #%lld: X won\n",cpy-tc);
			continue;
		}

		if((board[0][2]=='O' || board[0][2]=='T') && (board[1][2]=='O' || board[1][2]=='T') && (board[2][2]=='O' || board[2][2]=='T') && (board[3][2]=='O' || board[3][2]=='T'))
		{
			printf("Case #%lld: O won\n",cpy-tc);
			continue;
		}

		if((board[0][2]=='X' || board[0][2]=='T') && (board[1][2]=='X' || board[1][2]=='T') && (board[2][2]=='X' || board[2][2]=='T') && (board[3][2]=='X' || board[3][2]=='T'))
		{
			printf("Case #%lld: X won\n",cpy-tc);
			continue;
		}

		if((board[0][3]=='O' || board[0][3]=='T') && (board[1][3]=='O' || board[1][3]=='T') && (board[2][3]=='O' || board[2][3]=='T') && (board[3][3]=='O' || board[3][3]=='T'))
		{
			printf("Case #%lld: O won\n",cpy-tc);
			continue;
		}

		if((board[0][3]=='X' || board[0][3]=='T') && (board[1][3]=='X' || board[1][3]=='T') && (board[2][3]=='X' || board[2][3]=='T') && (board[3][3]=='X' || board[3][3]=='T'))
		{
			printf("Case #%lld: X won\n",cpy-tc);
			continue;
		}
		// diag case;

		if((board[0][0]=='O' || board[0][0]=='T') && (board[1][1]=='O' || board[1][1]=='T') && (board[2][2]=='O' || board[2][2]=='T') && (board[3][3]=='O' || board[3][3]=='T'))
		{
			printf("Case #%lld: O won\n",cpy-tc);
			continue;
		}

		if((board[0][0]=='X' || board[0][0]=='T') && (board[1][1]=='X' || board[1][1]=='T') && (board[2][2]=='X' || board[2][2]=='T') && (board[3][3]=='X' || board[3][3]=='T'))
		{
			printf("Case #%lld: X won\n",cpy-tc);
			continue;
		}

		// anti diag case;

		if((board[0][3]=='O' || board[0][3]=='T') && (board[1][2]=='O' || board[1][2]=='T') && (board[2][1]=='O' || board[2][1]=='T') && (board[3][0]=='O' || board[3][0]=='T'))
		{
			printf("Case #%lld: O won\n",cpy-tc);
			continue;
		}

		if((board[0][3]=='X' || board[0][3]=='T') && (board[1][2]=='X' || board[1][2]=='T') && (board[2][1]=='X' || board[2][1]=='T') && (board[3][0]=='X' || board[3][0]=='T'))
		{
			printf("Case #%lld: X won\n",cpy-tc);
			continue;
		}

		if(ct!=0)
		{
			printf("Case #%lld: Game has not completed\n",cpy-tc);
		}
		else
		{
			printf("Case #%lld: Draw\n",cpy-tc);
		}

	}
	return 0;
}
