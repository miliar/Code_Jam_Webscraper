#include<cstdio>
#include<algorithm>

using namespace std;

#define SIZE 5009

typedef __int64 ll;

int start[SIZE], pos[SIZE], arr[SIZE], sum[SIZE];

int main(){
	int T, X, R, k, N, i, curst, curcnt, cnt, cycle, clen;
	ll ret, cur, tsum, totsum;

	//freopen("C-small.in", "r", stdin); freopen("C-small.out", "w", stdout);
	freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);
	scanf("%d", &T);
	for(X = 1; X<=T; ++X){
		scanf("%d%d%d", &R, &k, &N);

		for( i = 0; i<N; ++i) scanf("%d", &arr[i]);
		memset(pos, -1, sizeof(pos));

		ret = 0;
		i = 0;
		for(cnt = 0; cnt < R ;cnt++){
			cur = 0;
			curst = i;
			curcnt = 0;
			for( ;;i = (i+1)%N){
				if( curcnt < N && cur + arr[i] <= k){
					cur += arr[i];
					curcnt++;
				}
				else break;
			}

			
			start[cnt] = curst; sum[cnt] = cur;
			if( pos[curst] == -1) pos[curst] = cnt;
			else break;
			ret += cur;
		}

		if( cnt >= R){
			goto hell;
		}

		cycle = pos[curst]; clen = cnt - pos[curst];
		ret = 0;
		for(i=0; i<R && i< cycle; ++i){
			ret += sum[i];
		}

		
		tsum = 0; totsum = 0;
		for( i = pos[curst]; i<cnt; ++i){
			totsum += sum[i];
		}

		R -= cycle;
		totsum *= (R/clen);
		R%=clen;
		for( i = pos[curst]; i<pos[curst] + R; ++i){
			tsum += sum[i];
		}

		ret += totsum + tsum;

hell:

		printf("Case #%d: %I64d\n", X, ret);
	}
	return 0;
}