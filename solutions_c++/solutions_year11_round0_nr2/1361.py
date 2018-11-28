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

const int N = 38;
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
int cmb[N][N], opp[N][N];

const int char_int(char c) {return c - 'A';}

void init()
{
    memset(cmb, 0, sizeof(cmb));
    memset(opp, 0, sizeof(opp));
    cin>>n;
    while(n--)
    {
        string s;
        cin>>s;
        cmb[char_int(s[0])][char_int(s[1])] = char_int(s[2]);
        cmb[char_int(s[1])][char_int(s[0])] = char_int(s[2]);
    }
    cin>>n;
    while(n--)
    {
        string s;
        cin>>s;
        opp[char_int(s[0])][char_int(s[1])] = 1;
        opp[char_int(s[1])][char_int(s[0])] = 1;
    }
}

stack<int> clr;

void solve(int tcase)
{
    cin>>n;
    string str;
    cin>>str;
    stack<int> sta;
    int have[N] = {0};
    for(int i = 0; i < n; i++)
    {
        int num = char_int(str[i]);
        while(!sta.empty())
        {
            int tmp = sta.top();
            if(cmb[num][tmp])
            {
                num = cmb[num][tmp];
                have[tmp]--;
                sta.pop();
            }
            else break;
        }
        
        sta.push(num);
        have[num]++;
        for(int j = 0; j < 26; j++)
        {
            if(j != num)
            {
                if(!opp[num][j] || !have[j]) continue;
                sta = clr;
                memset(have, 0, sizeof(have));
                break;
            }
            else
            {
                if(!opp[num][num] || have[num] < 2) continue;
                sta = clr;
                memset(have, 0, sizeof(have));
                break;
            }
        }
    }
    vi res;
    while(!sta.empty()) {res.pb(sta.top()); sta.pop();}
    printf("Case #%d: [", tcase);
    int sz = res.size() - 1;
    for(int i = sz; i >= 0; i--)
    {
        if(i != sz) printf(", ");
        printf("%c", res[i] + 'A');
    }
    printf("]\n");
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    cin>>T;
    
    for(int i = 1; i <= T; i++)
    {
        init();
        solve(i);
    }
    //while(1);
}
