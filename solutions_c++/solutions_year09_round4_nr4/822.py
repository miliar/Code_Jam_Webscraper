#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
typedef long long int lint;
typedef pair<int,int> par;
 
#define sz size
#define pb push_back
#define all(x) (x).begin() , (x).end()
#define sqr(x) (x)*(x)
#define rep(i,n)  for (int (i)=0;(i)<(int)(n);(i)++)
#define Rep(i,a,n) for (int (i)=(int)(a);(i)<(int)(n);(i)++)


double r[10],x[10],y[10];

int main() {

	int t;
	cin >> t;
	Rep(i,1,t+1) {
		int n;
		cin >> n;
		rep(j,n) {
			cin >> x[j] >> y[j] >> r[j];
		}
		
		double dist;
		switch (n) {
			case 1:
				dist = r[0];
				break;
			case 2:
				dist = max(r[0],r[1]);
				break;
			case 3: {
				double dist1, dist2, dist3;
		
				// 0 - 1,2
				dist1 = sqrt( sqr(x[1]-x[2]) + sqr(y[1] - y[2]) ) + r[1] + r[2];
				dist1 /= 2.0;
				dist1 = max(dist1, r[0]);
		
		
				// 1 - 0,2
				dist2 = sqrt( sqr(x[0]-x[2]) + sqr(y[0] - y[2]) ) + r[0] + r[2];
				dist2 /= 2.0;
				dist2 = max(dist2, r[1]);
		
		
				// 2 - 0,1
				dist3 = sqrt( sqr(x[0]-x[1]) + sqr(y[0] - y[1]) ) + r[0] + r[1];
				dist3 /= 2.0;
				dist3 = max(dist3, r[2]);
				
				dist = min(dist1,min(dist2,dist3));
			}
			break;
		
		}
			
		printf("Case #%d: %.6lf\n",i,dist);
	}
	return 0;
}

