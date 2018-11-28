#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

using namespace std;

#define clr(x) memset((x),0,sizeof(x))
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define For(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define Ford(i,s,e) for(int i=(s);i>=(int)(e);i--)
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define ford(i,n) for(int i=(n)-1;i>=0;i--)
#define fori(it,x) for (__typeof((x).begin()) it = (x).begin();it != (x).end();it++)

template <class T> inline T sqr(const T& x) { return x * x; }
template <class T> inline string tostr(const T& a) { ostringstream os(""); os << a; return os.str(); }
template <class T> inline istream& operator << (istream& is, const T& a) { is.putback(a); return is; }

// Types
typedef long double ld;
typedef signed   long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

// Constants
const ld PI = acos(-1.0);//3.1415926535897932384626433832795;
const ld EPS = 1e-11;
const int dx[] = {-1,0,1,0,-1,-1,1,1};
const int dy[] = {0,1,0,-1,-1,1,-1,1};
const int MAXN = 110;

int mat[MAXN][MAXN],old[MAXN][MAXN],n,x1,x2,yy,y2,num;

void dfs()
{
    for(int i = 1; i <= 100; i++)
        for(int j = 1; j <= 100; j++)
        {
            bool u = 1, l = 1;
            if(i == 1 || old[i - 1][j] == 0) u = 0;
            if(j == 1 || old[i][j - 1] == 0) l = 0;

            if(!u && !l && old[i][j] == 1) mat[i][j] = 0, num--;
            else if(u && l && old[i][j] == 0) mat[i][j] = 1, num++;
        }
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);  
    int cas;
    cin >> cas;
    for (int T = 1;T <= cas;T++)
    {
        clr(mat);
        cin >> n;
        num = 0;
        for(int i = 1;i <= n;i++)
        {
            cin >> x1 >> yy >> x2 >> y2;
            for(int j = x1; j <= x2; j++)
                for(int k = yy; k <= y2; k++)
                {
                    if(mat[k][j] == 0)
                    {
                        num++;
                        mat[k][j] = 1;
                    }
                }
        }

        int ans = 0;
        while(num)
        {
            memcpy(old,mat,sizeof(mat));
            ans++;
            dfs();
        }
        cout << "Case #" << T << ": " << ans << endl;
    }

    return 0;
}