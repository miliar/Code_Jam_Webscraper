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

const int Maxn = 1000+10;
const int INF = 0x7f7f7f7f;
const double eps = 1e-10;
const double pi = acos(-1.0);
inline int realcmp(double a, double b){ return (a>b+eps) ? 1 : ((a+eps<b)?-1:0); }

char com[300][300];
bool del[300][300];

int main()
{
    string str;
    int cas, c, d, n;
    ios::sync_with_stdio(0);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    cin>>cas;
    for(int cc=1; cc<=cas; cc++)
    {
        cin>>c;
        memset(com, 0, sizeof(com));
        memset(del, 0, sizeof(del));
        for(int i=0; i<c; i++)
        {
            cin>>str;
            com[str[0]][str[1]] = str[2];
            com[str[1]][str[0]] = str[2];
        }
        cin>>d;
        for(int i=0; i<d; i++)
        {
            cin>>str;
            del[str[0]][str[1]] = 1;
            del[str[1]][str[0]] = 1;
        }
        cin>>n>>str;

        string ans;
        for(int i=0; i<n; i++)
        {
            int len = sz(ans);
            if( len == 0 )
                ans += str[i];
            else
            {
                if( com[ans[len-1]][str[i]] )
                    ans[len-1] = com[ans[len-1]][str[i]];
                else
                {
                    ans += str[i];
                    for(int j=0; j<len; j++)
                        if( del[str[i]][ans[j]] )
                        {
                            ans = "";
                            break;
                        }
                }
            }
        }
        printf("Case #%d: [", cc);
        if( !ans.empty() )
            printf("%c", ans[0]);
        for(int i=1; i<sz(ans); i++)
            printf(", %c", ans[i]);
        printf("]\n");
    }

    return 0;
}
