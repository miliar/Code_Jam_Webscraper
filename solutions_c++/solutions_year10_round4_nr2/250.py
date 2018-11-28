#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int p, n;

vector<int> miss;
vector<int> attend;

vector<int> tree;

typedef long long ll;

const ll inf = 1000000000000LL;

ll memo[8000][20];

ll best(int at, int done){
	if ( at >= (1<<p) ){
		//printf("fin: %d\n", at-(1<<p));
		if(done >= attend[at-(1<<p)] ) return 0;
		else return inf;
	}
	
	ll& res = memo[at][done];
	if(res != -1) return res;
	
	
	ll propA = tree[at]+best(2*at, done+1) + best(2*at+1, done+1);
	ll propB = best(2*at, done) + best(2*at+1, done);
	res = min(propA, propB);
	return res;
}

int main(){
	int lz;
	scanf("%d", &lz);
	for(int cnt = 1; cnt <= lz; cnt++){
	
		scanf("%d", &p);
		n = (1<<p);
		miss = vector<int>(n);
		for(int i = 0; i < n; i++) scanf("%d", &miss[i]);
		attend = miss;
		for(int i = 0; i < n; i++) attend[i] = p-miss[i];
		tree = vector<int> (n);
		for(int lev = p-1; lev >=0; lev--){
			for(int at = (1<<lev); at < 2*(1<<lev); at++) scanf("%d", &tree[at]);//, printf("%d ", tree[at]);
			//printf("\n");
		}
		memset(memo, -1, sizeof(memo));
		printf("Case #%d: %lld\n", cnt, best(1, 0));
	}
	return 0;
	
}
