#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>

using namespace std;

#define fore(i,a) for(int i = 0; i < (a); i++)
#define fort(i,a) for(typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define x first
#define y second

#define inf 1e9

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef long long ll;

#define err(...)
#define err(...) fprintf(stderr, __VA_ARGS__)

int TT, R, C, F;
int vis[22][8][1<<7][1<<7], dp[22][8][1<<7][1<<7];
char t[22][22];
int r[22];

int foo(int,int,int,int);

int jump(int x, int y, int cur, int next)
{
	int q;
	for(q = 0; y < R+2 && (next & (1<<x)) == 0; q++)
	{
		cur = next;
		next = r[y];
		y++;
	}
	//printf("jump %d %d %d %d -- %d %d \n", x, y, cur, next, q, F);
	if(q > F) return inf;
	return foo(x, y, cur, next);
}

int foo(int x, int y, int cur, int next)
{
	if(y == R+1) return 0;
	if(vis[x][y][cur][next] == TT) return dp[x][y][cur][next];
	vis[x][y][cur][next] = TT;
	dp[x][y][cur][next] = inf;

	int left = x, right = x, res = inf;

	while(left > 0 && (cur & (1<<left-1)) == 0 && (next & (1<<left-1)) > 0) left--;
	while(right + 1 < C && (cur & (1<<right+1)) == 0 && (next & (1<<right+1)) > 0) right++;

	//printf("foo %d, %d, %d, %d -- left = %d, right = %d\n", x, y, cur, next, left, right);

	if(left > 0 && (cur & (1<<left-1)) == 0) res = min(res, jump(left-1, y, cur, next));
	if(right+1 < C && (cur & (1<<right+1)) == 0) res = min(res, jump(right+1, y, cur, next));

	for(int i = left; i < right; i++) res = min(res, 1 + foo(i, y, cur, next ^ (1<<i+1)));
	for(int i = left+1; i <= right; i++) res = min(res, 1 + foo(i, y, cur, next ^ (1<<i-1)));

	return dp[x][y][cur][next] = res;
}

void test()
{
	scanf("%d%d%d", &R, &C, &F);
	fore(i,R)
	{
		scanf("%s", t[i]);
		r[i] = 0;
		for(int j = C-1; j >= 0; j--) r[i] = r[i] * 2 + (t[i][j] == '#');
	}
	r[R] = (1<<C)-1;
	int res = foo(0,2,r[0],r[1]);
	if(res > 1e8) printf("No\n");
	else printf("Yes %d\n", res);
}

int main()
{
	int T;
	scanf("%d", &T);
	for(TT = 1; TT <= T; TT++)
	{
		printf("Case #%d: ", TT);
		test();
	}
}
