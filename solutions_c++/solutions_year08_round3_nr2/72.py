#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctype.h>
#include <bitset>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef istringstream iss;
typedef ostringstream oss;

#define d2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a):(-(a))) 
#define cl(a, val) memset(a, val, sizeof(a))
#define deb(x) cout<<#x<<" = "<<(x)<<endl
#define FG(a, b) for((a) = (b); (a) >= 0; (a)--)
#define FD(a, b) for((a) = 0; (a) < (b); (a)++)
#define all(a) (a).begin(),(a).end() 
#define sz(a) int((a).size())
#define PB push_back
#define INF 0x3fffffff
#define Y second
#define X first

char in[] = "B-small-attempt0.in";
char out[] = "B-small-attempt0.out";

int n, m, len;
int ul;
char s[20];
int ugly(ll nn)
{
	if(nn == 0) return 1;
	if(nn < 0) nn = -nn;
	return (nn % 2 == 0 || nn % 3 == 0 || nn % 5 == 0 || nn % 7 == 0);
}
void make(int pos, ll r)
{
	ll k(0);
	if(pos == len && ugly(r)){ ul++; return; }
	if(r == 71)
	{
		k = 0;
	}

	for(int i = pos; i < len; i++)
	{
		k = k * 10 + s[i] - '0';
		make( i + 1, r + k );
		make( i + 1, r - k );
	}
}


int main()
{
	freopen(in, "rt", stdin);
	freopen(out, "wt", stdout);

	int i, j, k, tt;
	int T, t;
	scanf("%d", &T);
	//printf("%d\n", ugly(1));

	for(t = 1; t <= T; t++)
	{
		
		scanf("%s", s);
		len = strlen(s);

		ul = 0;
		make(0, 0);

		printf("Case #%d: %d\n", t, ul / 2);
	}
	return 0;
}