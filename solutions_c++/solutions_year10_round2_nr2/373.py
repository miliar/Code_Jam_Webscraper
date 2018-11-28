#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

#define ME(s) memset((s), 0, sizeof((s)))
#define MM(s,a) memset((s),(a),sizeof((s)))
#define MCP(s,a) memcpy((s), (a), sizeof(s))
#define LL long long
#define LD long double
#define PII pair<int, int>
#define PDD pair<double, double>
#define mkp(a,b) make_pair((a),(b))
#define y first
#define x second
#define sqr(a) ((a)*(a))
#define lowbit ((x)&(-(x)))
#define two(x) (1<<(x))
#define contain(mask,x) ((mask&two(x))!=0) 

FILE *fin=freopen("B.in","r",stdin);
FILE *fout=freopen("B.out","w",stdout);

inline int sgn(double x){return fabs(x)<1e-12?0:(x<0?-1:1);}

int main () {	
	int x[10000],v[10000],t[10000];
    int Cases,n,k,B,T,s,r;
	fscanf (fin,"%d", &Cases);    
    for (int i = 1; i <= Cases; ++ i) {
        fscanf (fin,"%d %d %d %d", &n, &k, &B, &T);
        for (int j = 1; j <= n; ++ j)
            fscanf (fin,"%d", &x[j]);
        for (int j = 1; j <= n; ++ j)
            fscanf (fin,"%d", &v[j]);
        for (int p = 1; p < n; ++ p)
            for (int q = p + 1; q <= n; ++ q)
                if (x[p] < x[q]) {
                   swap (x[p], x[q]); swap (v[p], v[q]);
                }
        s = 0; r = 0;
        memset (t, 0, sizeof (t));
        for (int j = 1; j <= n; ++ j)
            if (x[j] + T * v[j] >= B) {
               -- k; 
			   t[j] = t[r] + (j - r - 1);
               s += t[j]; 
			   r = j;
               if (k == 0) 
			   	break;
            }
        if (k > 0) 
           fprintf (fout,"Case #%d: IMPOSSIBLE\n", i);
        else
           fprintf (fout,"Case #%d: %d\n", i, s);
    }
    return 0;
}
//Powered by [KawigiEdit] 2.0!

