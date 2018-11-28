//dyussenaliyev

#ifdef ONLINE_JUDGE
	#define _SECURE_SCL 0
#else
	#define _GLIBCXX_DEBUG
#endif

#if ( _WIN32 || __WIN32__ )
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <bitset>
#include <vector>
#include <string>
#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <string.h>
#include <iostream>
#include <algorithm>
//include <brain.h>
using namespace std;

#define bug(x) cout<<"->"<<#x<<": "<<x<<endl;
#define pb push_back
#define mp make_pair
#define sz(a) (int)a.size()
#define fill(a,key) memset(a, key, sizeof(a))
#define cpy(a,b) memcpy(a, b, sizeof(a))
#define all(x) x.begin(), x.end()
#define ones(x) __builtin_popcount((x)) // returns number of set bits
#define clz(x) __builtin_clz((x)) // returns number of leading zeros
#define ctz(x) __builtin_ctz((x)) // returns number of tailing zeros
#define REP(i,n) for (int i = 0; i < (n); i++)
#define REV(i,n) for (int i = (n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)
#define tr(it,vec) for (typeof(vec.begin())::iterator it = vec.begin(); it != vec.end(); it++)
#define belongs(x, c) find((c).begin(), (c).end(), (x)) != (c).end()
#define sqr(x) (x)*(x)
#define curtime double(clock())/double(CLOCKS_PER_SEC)

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int inf = 1<<30;
const long long Inf = 1LL<<62;

const int dx[] = {-1,0,1,0,-1,-1,1,1,0};
const int dy[] = {0,1,0,-1,-1,1,1,-1,0};

const double eps = 1e-9;
const double pi = 3.1415926535897932384626433832795;

template <class T> inline bool eq(const T &a, const T &b) { return fabs(a-b) < eps; }
template <class T> inline bool deg2(const T &n) {return (n&(n-1))==0;}//check on power of two
template <class T> inline void chmax(T &a, const T &b) { a = max(a, b); }
inline int Rand() {return (rand()<<16)|rand();}
/////////////////////////////////////////////////////////////////////////////////////////////////

int t[101], x, T, n, s, p, ans, i, j, num, best;

void go(int number, int best, int x)
{
    for (int i = 0; i < n; i++)
    if (t[i] == number && s && best >= p)
    {
        ans++;
        t[i] = -1;
        s--;
    } else
    if (t[i] == number && best-x >= p)
    {
        t[i] = -1;
        ans++;
    }
}

int main()
{
	ios_base::sync_with_stdio(false);

	srand(time(NULL));
	#ifndef ONLINE_JUDGE
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	#endif

	cin >> T;

	for (x = 1; x <= T; x++)
	{
		cin >> n >> s >> p;

		for (i = 0; i < n; i++)
			cin >> t[i];

		ans = 0;

        for (num = 2, best = 2; num < 28; num += 3, best++)
        {
            go(num,best,1);
            go(num+1,best,1);
        }

        for (num = 4, best = 2; num < 29; num += 3, best++)
            go(num,best,0);

        go(29,10,0);
        go(30,10,0);
        go(0,0,0);
        go(1,1,0);

		printf("Case #%d: %d\n", x, ans);
	}

	return 0;
}
