#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set> 
#include <map>
#include <iomanip>
using namespace std;

#define FOR0(i, n) for(int i=0;i<n;i++)
#define ALL(c) c.begin(),c.end()
#define TR(it, c) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define FORE(x,c) TR(__I,c)if(bool __B=1)for(typeof(*__I) x=*__I;__B;
#define FOR1(i, n) for(int i=1;i<=n;i++)
#define IT(c) typeof(c.begin())
#define REP(n) for(int __z=0;__z<n;__z++)

typedef long long int lli;
typedef pair<int,int> ii;

const int N = 110;
char W[N][N];
long double WP[N], OWP[N], OOWP[N];
int op[N];
int main()
{
    int T;
    cin >> T;
    FOR1(q,T)
    {
    int n;
    cin >> n;
    FOR0(i,n) FOR0(j,n) cin >> W[i][j];

    FOR0(i,n)
    {
	// calc WP
	int w = 0, t = 0;
	FOR0(k,n)
	{
	    if(W[i][k] == '1')
		w++;
	    if(W[i][k] != '.')
		t++;
	}
	op[i] = t;
	WP[i] = (long double)(w) / (long double)(t);
//	cout << WP[i] << ' ' << op[i] << endl;
    }

    FOR0(i,n)
    {
	long double wpsum = 0.0;
	FOR0(k,n)
	{
	    if(W[i][k] != '.')
	    {
		long double toadd;
		if(W[i][k] == '1')
		{
		    toadd = (WP[k] * op[k]) / (op[k]-1.0);
		}
		else
		{
		    toadd = ((WP[k] *op[k])-1.0) / (op[k]-1.0);
		}
		wpsum += toadd;
	    }
	}
	OWP[i] = wpsum / (long double)(op[i]);

//	cout << OWP[i] << '\n';
    }
    
    FOR0(i,n)
    {
	long double owpsum = 0.0;
	FOR0(k,n)
	{
	    if(W[i][k] != '.')
	    {
		owpsum += OWP[k];
	    }
	}
	OOWP[i] = owpsum / (long double)(op[i]);
    }
    
    cout << "Case #"<<q<<":\n";
    FOR0(i,n)
    {
	long double ans = ((0.25*WP[i]) + (0.50*OWP[i]) + (0.25*OOWP[i]));
	cout << setprecision(12) << ans << '\n';
    }
    }

    return 0;
}
