#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;
typedef long double ld;
typedef pair<ld,ld> P;
int main() {
	int T;cin>>T;
	for(int a=1; a<=T; ++a) {
		ld x,s,r,t,n;
		cin>>x>>s>>r>>t>>n;

//		double res=t + double(x - r*t)/s;
		vector<P> v;
		ld sum = 0;
		for(int i=0; i<n; ++i) {
			ld b,e,w;
			cin>>b>>e>>w;
			v.push_back(P(w,e-b));
			sum += e-b;
		}
		ld rem = x - sum;
		ld rs = min(r*t,rem);
		rs = min(rs, x);
		ld res = rs / r;
		x -= rs;
		t -= res;
		sort(v.begin(),v.end());
//		cout<<"s0: "<<x<<' '<<res<<' '<<t<<' '<<rem<<'\n';
		for(int i=0; i<n; ++i) {
			P p = v[i];
			double dst = p.second;
			if (t > 1e-9) {
				double spd = r + p.first;
				double tt = dst / spd;
//				cout<<"kk: "<<tt<<' '<<t<<'\n';
				if (tt > t) {
					res += t;
					x -= t * spd;
					dst -= t * spd;
					t = 0;
				} else {
					res += tt;
					x -= dst;
					t -= tt;
					continue;
				}
			}
//			cout<<"lol: "<<t<<' '<<res<<' '<<dst<<' '<<x<<'\n';
			double spd = s + p.first;
			double tt = dst / spd;
			res += tt;
			x -= dst;
		}
		res += x / s;

		cout<<"Case #"<<a<<": "<<fixed<<setprecision(15)<<res<<'\n';
	}
}
