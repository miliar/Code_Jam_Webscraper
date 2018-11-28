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
const int gcd(int a, int b) {return b ? gcd(b, a % b) : a;}

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

int n;
bool notp[1010]; //素数判定  
int pr[1010], pn; //pr存放素数,pn当前素数个数。

void table() 
{
    pn = 0;
    memset(notp, 0, sizeof(notp));
    for (int i = 2; i < N; i++) 
    {
        if(!notp[i]) pr[pn++] = i;
        for(int j = 0; j < pn && pr[j] * i < N; j++)
        {
            notp[pr[j] * i] = i;
            if (i % pr[j] == 0) break;
        }
    }
}

void init()
{
    cin>>n;
}

int get()
{
    int mid[N] = {0};
    int x = 0;
    for(int i = 2; i <= n; i++)
    {
        for(int j = 0; pr[j] <= i; j++)
        {
            if(i % pr[j] == 0)
            {
                int cnt = 0, tmp = i;
                 if (mid[pr[j]] == 0) x++;
                while(tmp % pr[j] == 0)
                {
                    tmp /= pr[j];
                    cnt++;
                } 
                if(cnt > mid[pr[j]]) mid[pr[j]] = cnt;
            }
        }
    }
    int res = 0;
    for (int i = 2; i <= n; ++i) res += mid[i];
    res++;
    return res - x;
}

void solve(int tcase)
{
    int res = get(); 
    if(n == 1) res = 0;
    printf("Case #%d: %d\n", tcase, res);
}

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    table();
    
    int T;
    cin>>T;
    
    for(int i = 1; i <= T; i++)
    {
        init();
        solve(i);
    }
    //while(1);
}
