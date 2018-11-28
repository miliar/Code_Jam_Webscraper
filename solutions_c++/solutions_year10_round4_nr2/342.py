#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
#include <utility>
#include <map>
using namespace std;
int N, P;
typedef long long ll;
deque< vector<int> > price;
vector<int> miss;

typedef pair<int,int> ii;
map< pair< int, ii >, ll > cache;

ll go( int stage, int gameno, int nummiss ) {
	if( stage == P ) {
		if( miss[gameno] < nummiss ) return 987654321;
		else return 0;
	}
	
	pair<int, pair<int,int> > state = make_pair( stage, make_pair( gameno, nummiss ) );
	if( cache.find( state ) != cache.end() ) return cache[ state ];
	ll &ret = cache[ state ];
	ret = 987654321;
	ll ret1 = go( stage+1, gameno*2, nummiss ) + go( stage+1, gameno*2+1, nummiss ) + price[stage][gameno];
	ll ret2 = go( stage+1, gameno*2, nummiss+1 ) + go( stage+1, gameno*2+1, nummiss+1 );
	ret = min( ret, ret1 );
	ret = min( ret, ret2 );
	return ret;
}
int main() {
	freopen("B-large.in","r",stdin);

	int tn;
	scanf("%d", &tn);
	for(int cc=1;cc<=tn;++cc) {
		price.clear();
		miss.clear();
		scanf("%d", &P);

		N = 1 << P;
		miss.resize(N);
		for(int i=0;i<N;++i) scanf("%d", &miss[i]);
		int M = N / 2;
		for(int i=0;i<P;++i) {
			vector<int> vec;
			for(int j=0;j<M;++j) {
				int x;
				scanf("%d", &x);
				vec.push_back(x);
			}
			price.push_front( vec );
			M /= 2;
		}
		cache.clear();
		printf("Case #%d: %I64d\n", cc, go( 0, 0, 0 ));
	}
}
