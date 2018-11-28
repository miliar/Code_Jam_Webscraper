#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef vector<int> vi;
typedef vector<double>vd;
typedef vector<string> vs;
typedef vector<vi>vvi;
typedef map<string,int> msi;
typedef map<int,int>mii;
typedef map<pii,int>mpi;

#define pb push_back
#define MP make_pair
#define popb pop_back
#define all(a) a.begin(), a.end()
#define Sort(x) sort(x.begin(),x.end())
#define Reverse(x) reverse(x.begin(),x.end())
#define SZ(a) ( (int)a.size() )
#define mem(a, b) memset(a, b, sizeof(a))

#define REP(i,n) for (i=0;i<n;i++)
#define REV(i,n) for (i=n;i>=0;i--)
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)
#define FOR(i,p,k) for (i=p; i<k;i++)

#define COPY(c,r)   memcpy(c,r,sizeof(r))
#define popcount(i) __builtin_popcount(i)
#define fs first
#define sc second

/// Moves ///
//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[] = {-2, 2, -1, 1, -1, 1};int dy[] = {0, 0, 1, 1, -1, -1}; //Hexagonal Moves

/// Cycles ///
//#define cycl0 0
//#define cycl1 1
//#define cycl5 5
//#define cycl6 6
//int cycl2[] = {1, 2, 4, 8, 6};
//int cycl3[] = {1, 3, 9, 7, 1};
//int cycl4[] = {1, 4, 6};
//int cycl7[] = {1, 7, 9, 3, 1};
//int cycl8[] = {1, 8, 4, 2, 6};
//int cycl9[] = {1, 9, 1};

#define INF 1<<30

vector<string>v(4);

bool check_x(void);
bool check_o(void);
bool check_unfinished(void);

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    bool x, o;

    cin>>t;
    for (int cas=1; cas<=t; cas++)
    {
        x = false, o = false;
        cin>>v[0]>>v[1]>>v[2]>>v[3];
        if (check_x()) printf ("Case #%d: X won\n", cas);
        else if (check_o()) printf ("Case #%d: O won\n", cas);
        else
        {
            if (check_unfinished()) printf ("Case #%d: Game has not completed\n", cas);
            else printf ("Case #%d: Draw\n", cas);
        }
    }
	return 0;
}

bool check_unfinished(void)
{
    for (int i=0; i<4; i++)
        for (int j=0; j<4; j++)
            if (v[i][j] == '.') return true;
    return false;
}

bool check_x(void)
{
    for (int i=0; i<4; i++)
    {
        int cnt = 0;
        for (int j=0; j<4; j++)
            if (v[i][j]=='X' || v[i][j]=='T') cnt++;
        if (cnt==4) return true;
    }
    for (int i=0; i<4; i++)
    {
        int cnt = 0;
        for (int j=0; j<4; j++)
            if (v[j][i]=='X' || v[j][i]=='T') cnt++;
        if (cnt==4) return true;
    }
    int cnt = 0;
    for (int i=0; i<4; i++)
        if (v[i][i]=='X' || v[i][i]=='T') cnt++;
    if (cnt==4) return true;
    cnt = 0;
    for (int i=0, j=3; i<4; i++, j--)
        if (v[i][j]=='X' || v[i][j]=='T') cnt++;
    if (cnt==4) return true;
    return false;
}

bool check_o(void)
{
    for (int i=0; i<4; i++)
    {
        int cnt = 0;
        for (int j=0; j<4; j++)
            if (v[i][j]=='O' || v[i][j]=='T') cnt++;
        if (cnt==4) return true;
    }
    for (int i=0; i<4; i++)
    {
        int cnt = 0;
        for (int j=0; j<4; j++)
            if (v[j][i]=='O' || v[j][i]=='T') cnt++;
        if (cnt==4) return true;
    }
    int cnt = 0;
    for (int i=0; i<4; i++)
        if (v[i][i]=='O' || v[i][i]=='T') cnt++;
    if (cnt==4) return true;
    cnt = 0;
    for (int i=0, j=3; i<4; i++, j--)
        if (v[i][j]=='O' || v[i][j]=='T') cnt++;
    if (cnt==4) return true;
    return false;
}
