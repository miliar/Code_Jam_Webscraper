#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>

#define TR(c, i) for ( typeof((c).begin()) i = (c).begin(); i != (c).end(); i++ ) 
#define FOR(i, a, b) for ( i = a; i <= b; i++ )
#define ROF(i, a, b) for ( i = a; i >= b; i-- )
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort( ALL(v) )
#define MAX(a, b) ((a) >= (b) ? (a) : (b))
#define MIN(a, b) ((a) <= (b) ? (a) : (b))
#define ABS(a) ((a) < (0) ? (a)*(-1) : (a))
#define SWAP(a, b) typeof(a) T; T=a; a=b; b=T;

using namespace std;

const double EPS = 1e-6;
 
double ar[1000010];
 
bool anshu(int n, double t, double d) 
{
	double x = max((ar[0]-d),(double)INT_MIN);
  
  	for (int i = 1; i < n; ++i) {
    		if (ar[i]+d<x+t) 
			return false;
    		x = max(ar[i]-d,x+t);
  	}
  	return true;
}
 
int main() 
{
	int tt, z;
  	scanf("%d", &tt);
 	for(z = 1; z <= tt; z++) {
    		int n;
		double t;
    		scanf("%d%lf", &n, &t);
		int k = 0;
    		for (int i = 0; i < n; i++) {
			double x;
			int y;
			scanf("%lf",&x);
			scanf("%d",&y);
			for(int j=0;j<y;j++)
				ar[k++] = x;
		}
 		sort(ar,ar+k);

    		double lo = 0, hi = 1;
    		while (!anshu(k, t, hi)) 
			hi *= 2;

    		while (lo+EPS<hi) {
      			double mid = (lo+hi)/2;
      			if (anshu(k,t,mid)) hi = mid;
      				else lo = mid;
    		}
    		printf("Case #%d: %.12lf\n", z,lo);
  	}
}
