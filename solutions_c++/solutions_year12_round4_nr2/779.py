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
int gcd (int a, int b)
{
   if (b == 0)
      return a;
   else
      return gcd (b, a % b);
}
/* Main code starts from here */

int r[10000];
pair<int,int> R[10000];
double x[10000], y[10000];
vector<pair<double, double> >lst;
vector<double> lr;
int main() {
	int t,T;
	scanf("%d", &T);
	for (t=1; t<=T; t++) {
	  printf("Case #%d:", t);
	  int n, w, l;
	  cin >>n >>w >>l;
	  for (int i = 0; i < n; i++) {
	    cin >>r[i];
	    R[i].first = r[i];
	    R[i].second = i;
	  }
	  //sort(R, R+n, greater<pair<int,int> >());
	  lst.clear();
	  lr.clear();
	  for (int i = 0; i < n; i++) x[i] = y[i] = -1.0;
	  int i = 0;
	  lst.push_back(make_pair(0.0,0.0));
	  lr.push_back(R[0].first);
	  x[R[0].second] = 0.0;
	  y[R[0].second] = 0.0;
	  i++;
	  for (int X = 0; X < w; X++) {
	    double yi = -1, flag = 0;
	    if (i >= n) break;
	    for (int k = 0; k < lst.size(); k++) {
	      double dis = (lr[k] + R[i].first) * (lr[k] + R[i].first) - (lst[k].first - X) * (lst[k].first - X);
	      dis = max(dis + 0.3, 0.3);
	      int pos = 0;
	      if (1) {
	        dis = sqrt(dis);
	        yi = dis + lst[k].second;
	        pos = 1;
	        for (int g = 0; g < lst.size(); g++) {
	          double dd = (lst[g].first - X) * (lst[g].first - X);
	          dd = dd + (lst[g].second - yi) * (lst[g].second - yi);
	          dd = sqrt(dd);
	          if (dd < lr[g] + R[i].first) {
	            pos = 0;
	            break;
	          }
	        }
	      }
	      if (pos && yi >= 0 && yi <= l) {
	        flag = 1;
	        break; 
	      }
	    }
	   
	    if (flag) {
	      x[R[i].second] = X;
	      y[R[i].second] = yi;
	      lst.push_back(make_pair(X,yi));
	      lr.push_back(R[i].first);
	      i++;
	    }
	  }
	  printf(" %lf %lf",x[0],y[0]);
	  for (int i = 1; i < n; i++) {
	    printf(" %lf %lf",x[i],y[i]);
	  }
	 puts("");
	}
	return 0;
}
