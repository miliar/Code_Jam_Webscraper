/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <complex>
#include <ctime>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <utility>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<double> point;
typedef long double ldb;

const int maxN = 100 * 1000 + 10;

int t,a,b;
double p[maxN],sum[maxN];

int main(){

	cin >> t;

	for (int i=1; i<=t; i++){
		cin >> a >> b;
		for (int j=1; j<=a; j++)
			cin >> p[j];
		for (int j=0; j<maxN; j++)
			sum[j] = 0.0;
		double ans1 = 0.0;
		double ans2 = 0.0;
		double ans3 = 1e9;
		double cur = 1.0;
		for (int j=1; j<=a; j++){
			double tmp = cur * (1.0-p[j]);
			ans1+= tmp * (b+1 + b-a+1);
			ans2+= tmp * (b+2);
			sum[a-j]+= tmp * (b+1);
			cur*= p[j];
		}

		ans1+= cur * (b-a+1);
		ans2+= cur * (b+2);

		double now = 0.0;

		for (int j=a; j>=0; j--){
			double tmp = j + (b-(a-j)+1);
			now+= sum[j];
			ans3 = min(ans3 , tmp + now);
		}
		
	//	cout << " : " << ans1 << ' ' << ans2 << ' ' << ans3 << endl;

		cout << "Case #" << i << ": ";
		cout << fixed << setprecision(6) << min(ans1,min(ans2,ans3)) << endl;
	}

	return 0;
}
