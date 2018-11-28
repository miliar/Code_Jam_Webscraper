#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

#define PB push_back
#define MP make_pair
#define clr(a,b)    (memset(a,b,sizeof(a)))
#define rep(i,a)    for(int i=0; i<(int)a.size(); i++)

const int INF = 0x3f3f3f3f;
const double eps = 1E-8;

int T;
char g[10][10];
int c[3];

int check(char a,char b,char c,char d)
{
	int res[128];
	clr(res, 0);
	res[a]++,res[b]++;
	res[c]++,res[d]++;

	if(res['X'] + res['T'] == 4 && res['X'] >= 3)	return 1;
	if(res['O'] + res['T'] == 4 && res['O'] >= 3)	return 2;
	return 0;
}

int main()
{
	freopen("D:\\in.txt","r",stdin);
	//freopen("A-small-attempt0.in","r",stdin);
	freopen("D:\\out.txt","w",stdout);

	scanf("%d",&T);
	for(int cas=1; cas<=T; cas++)
	{
		clr(g, 0),clr(c,0);
		for(int i=1; i<=4; i++)
			scanf("%s",g[i]+1);

		int blank = 0;
		for(int i=1; i<=4; i++)
			for(int j=1; j<=4; j++)
				if(g[i][j] == '.')
					blank ++;

		int r;
		for(int i=1; i<=4; i++)
		{
			r = check(g[i][1], g[i][2], g[i][3], g[i][4]);
			c[r]++;
		}
		for(int i=1; i<=4; i++)
		{
			r = check(g[1][i], g[2][i], g[3][i], g[4][i]);
			c[r]++;
		}
		r = check(g[1][1], g[2][2], g[3][3], g[4][4]);
		c[r]++;
		r = check(g[1][4], g[2][3], g[3][2], g[4][1]);
		c[r]++;

		printf("Case #%d: ",cas);
		if(c[1] > 0)	puts("X won");
		else if(c[2] > 0)	puts("O won");
		else if(blank != 0)	puts("Game has not completed");
		else	puts("Draw");
	}
	return 0;
}
