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

int d;
string s[20];

bool check(int n, int u, int v)
{
    double sumx=0, sumy=0;
    double x=(2*u+n)*0.5, y=(2*v+n)/2.0;

    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
        {
            if( (i==0&&j==0) || (i==0&&j==n-1) ||
                (i==n-1&&j==0) || (i==n-1&&j==n-1) )
                continue;
            sumx += (u+i+0.5-x)*(s[i+u][j+v]-'0'+d);
            sumy += (v+j+0.5-y)*(s[i+u][j+v]-'0'+d);
        }
    //cout<<u<<" "<<v<<" "<<sumx<<" "<<sumy<<endl;
    if( realcmp(sumx, 0)==0 && realcmp(sumy, 0)==0 )
        return true;
    return false;
}

int main()
{
    int cas, n, m;
    ios::sync_with_stdio(0);
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("B-small-attempt2.out", "w", stdout);

    cin>>cas;
    for(int c=1; c<=cas; c++)
    {
        cin>>n>>m>>d;
        for(int i=0; i<n; i++)
            cin>>s[i];
        bool f=false;
        int t=min(n, m);
        //if( t%2 == 0 )
            //t--;
        for(int i=t; i>=3&&!f; i--)
        {
            for(int j=0; j+i<=n&&!f; j++)
                for(int k=0; k+i<=m&&!f; k++)
                    if( check(i, j, k) )
                    {
                        f = true;
                        printf("Case #%d: %d\n", c, i);
                    }
        }
        if( !f )
            printf("Case #%d: IMPOSSIBLE\n", c);
    }

    return 0;
}
