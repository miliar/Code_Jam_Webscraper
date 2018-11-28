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

vp ord;
int n;

void init()
{
    cin>>n;
    ord.clear();
    for(int i = 1; i <= n; i++)
    {
        int p;
        char s[3];
        scanf("%s %d", &s, &p);
        if(s[0] == 'O') ord.pb(mp(p, 0));
        else ord.pb(mp(p, 1));
    }
}

void solve(int tcase)
{
    int p[2] = {0}, lst[2] = {0};
    int cnt = 0;
    
    p[1] = p[0] = 1;
    for(int i = 0; i < n; i++)
    {
        int pos = ord[i].fst;
        int num = ord[i].snd;
        int dist = ABS(p[num] - pos) + 1;
        if(lst[num] + dist - 1 <= cnt) cnt++;
        else cnt = lst[num] + dist;
        
        lst[num] = cnt;
        p[num] = pos;
    }
    printf("Case #%d: %d\n", tcase, cnt);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin>>T;
    
    for(int i = 1; i <= T; i++)
    {
        init();
        solve(i);
    }
    //while(1);
}
