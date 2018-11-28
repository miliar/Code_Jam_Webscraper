#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <map>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vp;
typedef vector<vi> vvi;

const int N = 100010;
const int M = 55;
const int K = 200010;
const int LIT = 2500;
const int INF = 1 << 30;
const int ABS(int x) {while(x < 0) x = -x; return x;}

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

ll n, pd, pg;

void init()
{
    cin>>n>>pd>>pg;
}

bool solve(int tcase)
{
    if(pg == 100 && pd != 100) return 0;
    if(pg == 0 && pd != 0) return 0;
    if(n >= 100) return 1;
    for(ll i = 1; i <= n; i++)
    {
        ll tmp = (i * pd) % 100;
        if(!tmp) return 1;
    }
    return 0;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    cin>>T;
    
    for(int i = 1; i <= T; i++)
    {
        init();
        printf("Case #%d: %s\n", i, solve(i) ? "Possible" : "Broken");
    }
    //while(1);
}
