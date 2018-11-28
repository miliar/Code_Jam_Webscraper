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

int a, b;

void init()
{
    cin>>a>>b;
}

int getnum(string s)
{
    int x;
    sscanf(s.c_str(), "%d", &x);
    return x;    
}

int cal(int x, int a, int b)
{
    char tmp[13];
    sprintf(tmp, "%d", x);
    string s = tmp;
    int ret = 0, n = s.size();
    set<int> have;
    for(int i = 0; i < n; i++)
    {
        int m = getnum(s);
        if(m >= a && m <= b && m > x && !have.count(m)) 
        {
            ret++;
            have.insert(m);
        }
        s = s.substr(1, n - 1) + s.substr(0, 1);
        //cout<<x<<" "<<s<<endl;
    }
    return ret;
}

void solve(int tcase)
{
    int res = 0;
    for(int i = a; i <= b; i++)
    {
        res += cal(i, a, b);
    }
    
    printf("Case #%d: %d\n", tcase, res);
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T;
    cin>>T; getchar();
    
    for(int i = 1; i <= T; i++)
    {
        init();
        solve(i);
    }
    
    //while(1);
}

