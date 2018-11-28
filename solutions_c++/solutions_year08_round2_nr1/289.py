#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

#define FOREACH(it,x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define ALL(x) (x).begin(), (x).end()
template<class T> void DUMP(const T& v) { FOREACH(it,v) cout<<*it<<' '; cout<<endl; }

int perm[6][3] = {
	{0,4,8},
	{0,5,7},
	{1,3,8},
	{1,5,6},
	{2,3,7},
	{2,4,6}
};

typedef long long ll;
int main() {
	int TC; cin>>TC;
	for (int testcase = 1; testcase <= TC; testcase++) {
		ll n, a, b, c, d, x, y, m;
		cin>>n>>a>>b>>c>>d>>x>>y>>m;
		ll ps[3*3] = {0};
		for (int i = 0; i < n; i++) {
			++ps[(x%3)*3+(y%3)];
			//cout<<"("<<x<<","<<y<<")";
			x = (a*x+b)%m, y = (c*y+d)%m;
		}
		//for (int i = 0; i < 9; i++) cout<<ps[i]<<" "; cout<<endl;
		ll ans = 0;
		for (int i = 0; i < 6; i++) {
			ans += ps[perm[i][0]]*ps[perm[i][1]]*ps[perm[i][2]];
		}
		for (int i = 0; i < 9; i++) {
			ans += ps[i]*(ps[i]-1)*(ps[i]-2)/6;
		}
		ans += ps[0]*ps[1]*ps[2];
		ans += ps[3]*ps[4]*ps[5];
		ans += ps[6]*ps[7]*ps[8];
		ans += ps[0]*ps[3]*ps[6];
		ans += ps[1]*ps[4]*ps[7];
		ans += ps[2]*ps[5]*ps[8];
		
		cout<<"Case #"<<testcase<<": "<<fixed<<ans<<endl;
	}
	return 0;
}
