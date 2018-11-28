/* Rajat Goel [C++] */
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<sstream>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;
const int    INF =     0x0FFFFFFF;
const double EPS =     1e-7;
typedef pair<int,int>  pii;
typedef long long      LL;
typedef long double    LD;
#define loop(i,n)      for(int i=0;i<n;i++)
#define foreach(i,a)   for(typeof((a).begin()) i=(a).begin();i!=(a).end();++i)
#define present(x,in)  (find((in).begin(),(in).end(),x) != (in).end())
#define all(a)         (a).begin(),(a).end()
#define cast(a,b)      { ostringstream myOut; myOut << a ; istringstream myIn ( myOut.str() ); myIn >> b; }
inline int fCMP(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

LD arr[100][2];
LD rad[100];

LD dist(int i, int j) {
	LD ans = sqrtl(powl(arr[i][0]-arr[j][0],2)+powl(arr[i][1]-arr[j][1],2));
	return ans+rad[i]+rad[j];
}

int main() {
	int T;cin >> T;
	for (int cas=1;cas<=T;cas++) {
		printf("Case #%d: ", cas);
		int n;
		cin >> n;
		loop(i,n) {
			cin >> arr[i][0] >> arr[i][1] >> rad[i];
		}
		if (n==1) {
			printf("%.7Lf\n", rad[0]);
		} else if(n==2) {
			printf("%.7Lf\n", max(rad[0], rad[1]));
		} else {
			LD a1 = dist(0,1)/2.0,a2 = dist(1,2)/2.0, a3 = dist(0,2)/2.0;
			LD an1 = max(a1,rad[2]);
			LD an2 = max(a2,rad[0]);
			LD an3 = max(a3,rad[1]);
			LD ans = min(an1, min(an2, an3));
			printf("%.7Lf\n", ans);
		}


	}
	return 0;
}
