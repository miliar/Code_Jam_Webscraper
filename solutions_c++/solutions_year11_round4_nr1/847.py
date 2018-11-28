#include <cassert>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(void) {
	int T;
	cin >> T;
	for(int tc=1; tc<=T; tc++) {
		int X,S,R,N;
		long double t;
		cin >> X >> S >> R >> t >> N;
		vector<pair<int,int> > ww;
		for(int i=0; i<N; i++) {
			int B,E,W;
			cin >> B >> E >> W;
			X-=(E-B);
			ww.push_back(make_pair(W,E-B));
		}
		assert(X>=0);
		if(X) ww.push_back(make_pair(0,X));
		sort(ww.begin(), ww.end());
		long double time=0;
		for(int i=0; i<ww.size(); i++) {
			long double A=ww[i].first;
			long double L=ww[i].second;
			//cout << A << " " << L << " " << t << " " << time << endl;
			if(t*(A+R)>=L) {
				time += L/(A+R+0.);
				t -= L/(A+R+0.);
				L=0;
				//cout << time << " " << t << L << endl;
			} else if(t) {
				time += t;
				L-=t*(A+R+0.);
				t = 0;
				//cout << time << " " << t << L << endl;
			}
			if(t==0 && L) {
				time += L/(A+S+0.);
				//cout << time << " " << t << L << endl;
			}
		}
		printf("Case #%d: %.9lf\n", tc, (double)time);
	}
}
