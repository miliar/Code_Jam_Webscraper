#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
#include <map>
using namespace std;

int C, D;
vector<int> vendor;

typedef pair<int,int> ii;

int cache[3000][101];

int solve( int last, int i ) {
	if( i == vendor.size() ) return 0;

	int llast = last - vendor[i-1] + 510;
	int &ret = cache[llast][i];

	if( ret != -1 ) return ret;
	ret = 987654321;
	for(int now = vendor[i] - 510 ; now <= vendor[i] + 510 ; ++now ) {
		if( now - last < D ) continue;
		int diff = abs( vendor[i] - now );
		ret = min( ret, max( diff, solve( now, i+1 ) ) );
	}
	return ret;
}

int main() {
	int tn;
	cin >> tn;
	for(int cc=1;cc<=tn;++cc) {
		cin >> C >> D;
		D *= 2;
		vendor.clear();
		for(int i=0;i<C;++i) {
			int p, v;
			cin >> p >> v;
			while(v--) vendor.push_back(p*2);
		}
		sort( vendor.begin(), vendor.end() );
		memset( cache, -1, sizeof cache );
		int ret = 1e9;
		for(int last = vendor[0] - 510 ; last <= vendor[0] + 510 ; ++last ) ret = min( ret, max(abs(last-vendor[0]),solve( last, 1 )));
		printf("Case #%d: ",cc);
		printf("%d.%d\n", ret/2, (ret%2)*5);
	}
	
}
