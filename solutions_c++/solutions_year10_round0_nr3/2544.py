#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef set<int> se;
typedef pair<int,int> pii;
typedef long long int tint;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(a) int((a).size())
#define pb push_back
#define pf pop_front

#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define all(c) (c).begin(), (c).end()
#define D(a) cout << #a << "=" << a << endl;
#define Mostrar(a) for(int i =0 ; i<a.size() ; ++i) cout << a[i] << " ";

int main()
{
	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);

	int t;
	cin >> t;

	forn(i, t)
	{
	    int R, k, n;
        cin >> R >> k >> n;
        deque<int> cola, segunda;
        int entrada;
        forn(l, n)
        {
            cin >> entrada;
            cola.pb(entrada);
        }
        int res = 0;
        forn(h, R)
        {
            int grupos = 0;
            int resto = k;
            int f;
            while(((f = cola.front()) <= resto) && (grupos++ < n))
            {
                cola.pf();
                cola.pb(f);
                resto -= f;
                res += f;
            }
        }
        cout << "Case #" << i + 1 << ": " << res << "\n";
	}

	return 0;

}
