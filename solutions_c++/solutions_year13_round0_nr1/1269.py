#include <iostream>
#include <vector>
#include <map>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>
#include <list>

// Input macros
#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)
#define INF                         (int)1e9
#define EPS                         1e-9

#define bitcount                    __builtin_popcount
#define gcd                         __gcd

#define forall(i,a,b)               for(int i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define mp							make_pair
#define DEBUG

using namespace std;

char g[5][5];

bool check(char c) {
	bool win = false;
	forall(i, 0, 4) {
		win = true;
		forall(j, 0, 4)
			if (g[i][j] != c && g[i][j] != 'T')
				win = false;
		if (win)
			return true;
	}

	forall(j, 0, 4) {
		win = true;
		forall(i, 0, 4)
			if (g[i][j] != c && g[i][j] != 'T')
				win = false;
		if (win)
			return true;
	}
#define eq(i,j) (g[i][j]==c || g[i][j]=='T')

	if (eq(0,0) && eq(1,1) && eq(2,2) && eq(3,3))
		return true;
	if (eq(0,3) && eq(1,2) && eq(2,1) && eq(3,0))
		return true;
	return false;
}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T = 0;

	scanf("%d", &T);
	gets(g[0]);
	forall(t, 1, T+1) {
		for (int i = 0; i < 4; i++)
			gets(g[i]);

		bool finished = true;
		forall(i, 0, 4)
			forall(j, 0, 4)
				if (g[i][j] == '.')
					finished = false;
		if (check('X'))
			printf("Case #%d: X won\n", t);
		else if (check('O'))
			printf("Case #%d: O won\n", t);
		else if (finished) {
			printf("Case #%d: Draw\n", t);
		} else
			printf("Case #%d: Game has not completed\n", t);
		gets(g[0]);
	}

	return 0;
}
