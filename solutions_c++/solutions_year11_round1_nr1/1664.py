#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <iostream>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cctype>
#include <sstream>
#include <cassert>
#include <bitset>
#include <memory.h>

#define bit(n) (1<<(n))
#define bit64(n) ((LL(1))<<(n))
#define inf 1000000000
#define eps 1e-9
#define PI 3.1415926535897932385
#define pb push_back
#define sz size()
#define mp make_pair
#define cl clear()
#define all(a) a.begin(),a.end()
#define fill(ar,val) memset(ar,val,sizeof ar)
#define MIN(a,b) if(a>(b)) a=(b)
#define MAX(a,b) if(a<(b)) a=(b)
#define sqr(x) ((x)*(x))
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n); i >= 1; i--)
#define fore(i, a, n) for(int i = (int)(a); i < (int)(n); i++)
#define last(a) (int(a.size()) - 1)

using namespace std;

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef __int64 LL;
typedef unsigned __int64 ULL;

void solve() {
    long int N = 0, Pd = 0, Pg = 0;
    float aux;
    bool falso = true;
    scanf("%ld %ld %ld", &N, &Pd, &Pg);

    if ( (Pg == 100) && (Pd < 100) ) {
        falso = true;
    }
    else if ( (Pd != 0) && (Pg == 0) ) falso = true;
    else {
        ford(i, N) {
            aux = (float) i*(Pd/100.0);
            if ( aux == (int) aux ) {
                falso = false;
                break;
            }
        }
    }

    if (falso == true) printf("Broken\n");
    else printf("Possible\n");

}




int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wr", stdout);

	int tt;
	scanf("%d", &tt);
	forn(ii, tt) {
		printf("Case #%d: ", ii + 1);
		solve();
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
