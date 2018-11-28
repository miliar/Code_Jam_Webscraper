#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cmath>
#include <list>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b(b);i<_b;++i)
#define FORD(i,a,b) for(int i=(a),_b(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define SZ(a) ((int) a.size())
#define pb push_back

#define VAR(a,b) __typeof(b) a=(b)
#define FORE(it,a) for(VAR(it,(a).begin());it!=(a).end();it++)
#define X first
#define Y second
#define DEBUG(x) cout << #x << " = " << x << endl;

#define INF 1000000000

typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long ll;

struct f 
{
    double x;
    string name;
    int q, w;
};

vector <f> p;

int parse ()
{
    f h;    
    cin >> h.x;
    char c;    
    h.q = h.w = -1;
    while (1)
    {
        cin >> c;                
        if (c == ' ' || c == '\n' || c == '\t') continue;
        if (c == ')') break;
        if (c == '(')
        {
            h.q = parse ();
            while (1)
            {
                cin >> c;                
                if (c == '(')
                    break;
            }
            h.w = parse ();
            while (1)
            {
                cin >> c;
                if (c == ')')
                    break;
            }
            break;
        }        
        h.name += c;
    }
    p.pb (h);    
    return SZ (p) - 1;
}

int main() {
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;
    cin >> test;
    while (test--)
    {
        int lin;
        cin >> lin;

        char c;
        cin >> c;
        p.clear ();
        int xxx = parse ();
        
        int k;
        cin >> k;
        static int ddd = 0;
        ++ddd;
        printf ("Case #%d:\n", ddd);
        
        REP (i, k)
        {
            string tmp;
            cin >> tmp;
            set <string> chars;
            int kil;
            cin >> kil;
            REP (j, kil)
            {
                string s;
                cin >> s;                
                chars.insert (s);               
            }
            int x = xxx;
            double P = 1.0;
            while (true)
            {
                P *= p[x].x;                
                if (!SZ (p[x].name))
                    break;
                if (chars.count (p[x].name))
                    x = p[x].q;
                else
                    x = p[x].w;
            }
            printf ("%.9lf\n", P);
        }        
    }
	return 0;
}
