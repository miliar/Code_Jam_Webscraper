#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <memory>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cmath>
#define sz(a) ((int)(a).size())
#define foreach(i, v) for(__typeof((v).begin()) i=(v).begin(); i!=(v).end(); i++)
using namespace std;
typedef long long llong;
typedef pair<int, int> Item;

const int Maxn = 100000+10;
const int INF = 0x7f7f7f7f;
const double eps = 1e-10;
const double pi = acos(-1.0);
inline int realcmp(double a, double b){ return (a>b+eps) ? 1 : ((a+eps<b)?-1:0); }

set<char> ch;
string sn[Maxn], sm[110];

bool check(string s, string t)
{
    for(int i=0; i<sz(s); i++)
    {
        if( t[i]=='_' && ch.find(s[i])!=ch.end() )
            return 0;
        if( t[i]!='_' && s[i]!=t[i] )
            return 0;
    }
    return 1;
}

int main()
{
    int cas, n, m;
    ios::sync_with_stdio(0);
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);

    cin>>cas;
    for(int c=1; c<=cas; c++)
    {
        cin>>n>>m;
        for(int i=0; i<n; i++)
            cin>>sn[i];
        for(int j=0; j<m; j++)
            cin>>sm[j];

        printf("Case #%d:", c);
        for(int i=0; i<m; i++)
        {
            string ans;
            int maxn=-1;
            for(int j=0; j<n; j++)
            {
                int cnt=0;
                string s=sn[j];
                set<string> st, tt;

                for(int k=0; k<sz(s); k++)
                    s[k] = '_';
                for(int k=0; k<n; k++)
                    if( sz(sn[k]) == sz(s) )
                        st.insert(sn[k]);

                ch.clear();
                for(int k=0; k<26; k++)
                {
                    bool f=false;
                    foreach(ptr, st)
                        if( ptr->find(sm[i][k]) != string::npos )
                        {
                            f = true;
                            break;
                        }
                    ch.insert(sm[i][k]);

                    if( !f )
                        continue;
                    f = false;
                    for(int l=0; l<sz(s); l++)
                        if( sn[j][l] == sm[i][k] )
                        {
                            f = true;
                            s[l] = sm[i][k];
                        }
                    if( !f )
                        cnt++;

                    foreach(ptr, st)
                        if( check(*ptr, s) )
                            tt.insert(*ptr);
                    st = tt;
                    tt.clear();
                    if( st.empty() )
                        break;
                }
                if( maxn < cnt )
                {
                    maxn = cnt;
                    ans = sn[j];
                }
            }
            printf(" %s", ans.c_str());
        }
        printf("\n");
    }

    return 0;
}
