#include<cstdio>
#include<map>
#include<queue>
using namespace std;
typedef long long LL;

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out.txt", "w", stdout);
	int ntc, N;
	LL R, k;
	scanf("%d", &ntc);
	for(int TC=1; TC <= ntc; TC++ ) {
		map< queue< LL >, int > mp;
		queue< LL > q, qcy;
		scanf("%I64d %I64d %d", &R, &k, &N);
		for(int i=0; i<N; i++) {
			LL x;
			scanf("%I64d", &x);
			q.push(x);
			qcy.push(x);
		}
		LL clen = 0LL;
		for(LL i=0LL; i >= 0LL; i++) {
			if ( mp.count( qcy ) > 0 ) {
				clen = clen - mp[ qcy ];
				break;
			} else {
				mp[ qcy ] = clen;
				int _n = qcy.size(), idx = 0;
				LL nnow = 0LL;
				while( idx < _n && nnow + qcy.front() <= k ) {
					idx++;
					nnow = nnow + qcy.front();
					qcy.push( qcy.front() );
					qcy.pop();
				}
				clen++;
			}
		}
		LL bclen = mp[qcy], csum = 0LL;
		for( LL i=0LL; i < clen; i++ ) {
			int _n = qcy.size(), idx = 0;
			LL nnow = 0LL;
			while( idx < _n && nnow + qcy.front() <= k ) {
				idx++;
				nnow = nnow + qcy.front();
				qcy.push( qcy.front() );
				qcy.pop();
			}
			csum += nnow;
		}
		LL ans = ((R - bclen) / clen) * csum, sisa = (R - bclen)%clen;
		for( LL i=0LL; i<sisa; i++) {
			int _n = qcy.size(), idx = 0;
			LL nnow = 0LL;
			while( idx < _n && nnow + qcy.front() <= k ) {
				idx++;
				nnow = nnow + qcy.front();
				qcy.push( qcy.front() );
				qcy.pop();
			}
			ans += nnow;
		}
		for( LL i=0; i<R && i<bclen; i++) {
			int _n = q.size(), idx = 0;
			LL nnow = 0LL;
			while( idx < _n && nnow + q.front() <= k ) {
				idx++;
				nnow = nnow + q.front();
				q.push( q.front() );
				q.pop();
			}
			ans += nnow;
		}
		printf("Case #%d: %I64d\n", TC, ans);
	}
	return 0;
}
