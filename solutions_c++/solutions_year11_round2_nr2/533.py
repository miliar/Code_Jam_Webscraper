#include<iostream>
#include<vector>
#include<queue>
#include<set>
#include<cstdio>
#include<algorithm>
#include<string>
#include<map>
#include<cmath>
#include<cstdlib>
#include<ctime>
using namespace std;


int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t; cin >> t;
	for (int k=0;k<t;k++) {
		int n,d; cin >> n >> d;
		vector<double> tmp,p;
		for (int i=0;i<n;i++) {
			double pp; int cnt; cin >> pp >> cnt;
			for (int j=0;j<cnt;j++) {
				tmp.push_back(pp);
			}
		}
		sort(tmp.begin(),tmp.end());
		p.resize(tmp.size());
		double l=0.0; double r=1e9;
		while (r-l>1e-7) {
			double mid=(r+l)/2.0;
			bool can=true;
			for (int i=0;i<p.size();i++)
				p[i]=tmp[i];
			for (int i=0;i<p.size();i++) {
				if (i==0) p[0]-=mid; else {
					double pre=p[i];
					p[i]-=mid;
					if (p[i]-p[i-1]<d) {
						p[i]=p[i-1]+d;
						if (p[i]-pre>mid) {
							can=false;
							break;
						}
					}
				}
			}
			if (can) r=mid; else l=mid;
		}
		printf("Case #%d: %.6f\n",k+1,r);
	}

	return 0;
}
