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

const int N = 110;
const int M = 55;
const int K = 200010;
const int LIT = 2500;
const int INF = 1 << 30;
const int ABS(int x) {while(x < 0) x = -x; return x;}

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

int n, m;
vector<string> dic, lst;
bool have[N][30];

void init()
{
    cin>>n>>m;
    dic.clear(); lst.clear(); memset(have, 0, sizeof(have));
    for(int i = 0; i < n; i++)
    {
        string s;
        cin>>s;
        dic.pb(s);
        for(int j = 0; j < s.size(); j++)
        {
            int x = s[j] - 'a';
            have[i][x] = 1;
        }    
    }
    for(int i = 0; i < m; i++)
    {
        string s;
        cin>>s;
        lst.pb(s);
    }
}

int getres(int x, int y)
{
    int cnt = 0;
    bool vis[N] = {0};
    for(int i = 0; i < n; i++)
    {
        if(dic[i].size() == dic[y].size()) vis[i] = 1, cnt++;
    }
    int res = 0;
    for(int i = 0; i < 26; i++)
    {
        if(cnt == 0) 
        {
            cout<<"ERROR"<<endl;
            while(1);    
        }
        if(cnt == 1) break;
        int ch = lst[x][i] - 'a';
        bool f = 0;
        for(int j = 0; j < n; j++)
        {
            if(!vis[j] || !have[j][ch]) continue;
            f = 1;
            break;
        }
        if(f)
        {
            if(!have[y][ch]) 
            {
                res++;
                for(int j = 0; j < n; j++)
                {
                    if(vis[j] && have[j][ch]) vis[j] = 0, cnt--;    
                }
            }   
            else
            {
                bool chk[13] = {0};
                for(int j = 0; j < dic[y].size(); j++)
                {
                    if(dic[y][j] == lst[x][i]) chk[j] = 1;
                }
                for(int j = 0; j < n; j++)
                {
                    if(!vis[j]) continue;
                    for(int k = 0; k < dic[y].size(); k++)
                    {
                        if(chk[k] && dic[j][k] != lst[x][i])
                        {
                            vis[j] = 0; cnt--; break;    
                        }
                        if(dic[j][k] == lst[x][i] && !chk[k])
                        {
                            vis[j] = 0; cnt--; break;    
                        }
                    }
                }
            }
        }
    }
    return res;
}

void solve()
{
    for(int i = 0; i < m; i++)
    {
        int Max = -1, id = -1;
        for(int j = 0; j < n; j++)
        {
            int tmp = getres(i, j);
            if(tmp > Max) Max = tmp, id = j;
        }
        cout<<" "<<dic[id];
    }
}

int main()
{
    freopen("B-small-attempt3.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T;
    cin>>T;
    
    for(int i = 1; i <= T; i++)
    {
        printf("Case #%d:", i);
        init();
        solve();
        printf("\n");
    }
    //while(1);
}
