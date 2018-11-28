#include <iostream>
#include <cstdio>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstring>
#include <string.h>
#include <cstdlib>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <utility>
#include <cctype>
#include <list>
#include <limits.h>
#include <signal.h>
#include <map>
#include <set>

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
 
double a[1000010];
 
bool solvable(int n, double t, double d) 
{
	double x = max((a[0]-d),(double)INT_MIN);
  
  	for (int i = 1; i < n; ++i) {
    		if (a[i]+d<x+t) 
			return false;
    		x = max(a[i]-d,x+t);
  	}
  	return true;
}
 
int main() 
{
	int tt,test = 0;
  	scanf("%d", &tt);
 	 while (tt--) {
		test++;
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
				a[k++] = x;
		}
 		sort(a,a+k);
//		cout <<INT_MIN;
//		for(int i=0;i<k;i++)
//			cout << a[i] << " ";
//	cout << k<< t <<" \n";
    		double lo = 0, hi = 1;
    		while (!solvable(k, t, hi)) 
			hi *= 2;

    		while (lo+EPS<hi) {
      			double mid = (lo+hi)/2;
      			if (solvable(k,t,mid)) hi = mid;
      				else lo = mid;
    		}
    		printf("Case #%d: %.6lf\n", test,lo);
  	}
}
