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

const int N = 1010;
const int M = 55;
const int K = 200010;
const int LIT = 2500;
const int INF = 1 << 30;
const int ABS(int x) {while(x < 0) x = -x; return x;}

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

int n;
int m[N];

void init()
{
    cin>>n;
    for(int i = 1; i <= n; i++) scanf("%d", &m[i]);
}

void solve(int tcase)
{
    int tot = 0, nor = 0, Min = INF;
    for(int i = 1; i <= n; i++) nor ^= m[i], tot += m[i], Min = min(Min, m[i]);
    if(nor) printf("Case #%d: NO\n", tcase);
    else printf("Case #%d: %d\n", tcase, tot - Min);
    
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T;
    cin>>T;
    
    for(int i = 1; i <= T; i++)
    {
        init();
        solve(i);
    }
    //while(1);
}
