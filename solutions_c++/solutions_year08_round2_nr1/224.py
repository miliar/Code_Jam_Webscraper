#include <iostream>
#include <stdio.h>
#include <set>
#include <vector>

using namespace std;

int main() {
	int N;
	cin >> N;
	for(int num=0;num<N;num++) {
		vector<pair<long long,long long> > p;
		long long A,B,C,D,x0,y0,M;
		int n;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		p.push_back( make_pair(x0,y0) );
		for(int j=1;j<=n-1;j++) {
			x0 = (A * x0 + B) % M;
			y0 = (C * y0 + D) % M;
			p.push_back( make_pair(x0,y0) );
		}
		int ret(0);
		for(int i=0;i<p.size();i++) for(int j=i+1;j<p.size();j++) for(int k=j+1;k<p.size();k++) {
			if( (p[i].first+p[j].first+p[k].first)%3 == 0 && (p[i].second+p[j].second+p[k].second) % 3 == 0 ) ret++;
		}
		printf("Case #%d: %d\n",num+1,ret);
	}
	return 0;
}
