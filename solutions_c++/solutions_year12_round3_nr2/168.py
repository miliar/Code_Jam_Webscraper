#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define tr(container, it)for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
int inline ABS(int a){ return a>0?a:-a; }
typedef pair<int,int> pi;
typedef unsigned long long ULL;
typedef long long LL;

/* Main code starts from here */

double tt[5],xx[5];
double eps = 10e-7;
int main() {
	int t, T;
	for (scanf("%d", &T), t = 1; t <= T; t++) {
		double D;
		int N,A;
		cin>>D>>N>>A;
		for (int i = 0; i < N; i++) {
		  cin>>tt[i]>>xx[i];
		}
		cout<<"Case #"<<t<<":\n";
		for (int i = 0; i < A; i++) {
		  double a;
		  cin>>a;
		  double t1,t2;
		  t1 = (D-xx[0]) * (tt[1]-tt[0])/(xx[1]-xx[0]);
		  t2 = sqrt(D*2/a);
		  if (N == 1) {
		     printf("%.10lf\n", t2);
		     continue;
		  }
		  if (N == 2) {
		  if (t1 > t2) 
		    printf("%.10lf\n", t1);
		  else
		    printf("%.10lf\n", t2);
		}
		}
	}
	return 0;
}
