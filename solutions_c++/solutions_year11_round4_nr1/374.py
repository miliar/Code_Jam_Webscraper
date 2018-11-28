#include <iostream>
#include <vector>
using namespace std;

int main(){
	int t=0;
	cin >> t;
	for(int c=0;c<t;c++){
		printf("Case #%d: ", c+1);
		int x, s, r ,t;
		int n;
		cin >> x >> s >> r >> t >> n;
		vector<pair<int,pair<int,int> > > p;

		vector<pair<pair<int,int>,int > >  tt(n,make_pair(make_pair(0,0),0));
		for(int i=0;i<n;i++){
			cin >> tt[i].first.first >> tt[i].first.second >> tt[i].second;
		}
		sort(tt.begin(),tt.end());
		
		int last = 0;
		for(int i=0;i<n;i++){
			int b, e, w;
			b = tt[i].first.first;
			e = tt[i].first.second;
			w = tt[i].second;
			p.push_back(make_pair(s, make_pair(last, b)));
			p.push_back(make_pair(s+w, make_pair(b, e)));
			last = e;
		}
		p.push_back(make_pair(s, make_pair(last, x)));
		
		sort(p.begin(),p.end());
		
		double ans = 0;
		double total = t;
		for(int i=0;i<p.size();i++){
			double ss = p[i].first;
			double b = p[i].second.first;
			double e = p[i].second.second;
			double lo=0, hi=1;
			for(int j=0;j<100;j++){
				double mid = (hi+lo)/2.0;
				double dist = (e-b) * mid;
				double tim = dist/(ss-s+r);
				if(tim>=total)
					hi = mid;
				else
					lo = mid;
			}
			double dist = (e-b) * lo;
			ans += dist/(ss-s+r);
			ans += (e-b-dist)/ss;
			total -= dist/(ss-s+r);
		}

		printf("%.10lf\n", ans);

	}

	return 0;
}
