#include <iostream>
	using namespace std;

int main(){
	long long int T, Case, R, k, N, g[2200], i, j, cir;
	long long int sum[2200], end[2200], b[2200], it, ssum[2200];
	cin >> T;
	for(Case = 1; Case <= T; ++Case){
		cin >> R >> k >> N;
		for(i = 0; i < N; ++i)
			cin >> g[i];
		for(i = N; i < N+N; ++i)
			g[i] = g[i-N];
		for(i = 0; i < N; ++i){
			sum[i] = 0;
			ssum[i] = 0;
			b[i] = -1;
		}
		for(i = 0; i < N; ++i){
			for(j = i; j < N+i; j++){
				if(sum[i] + g[j]> k)
					break;
				else
					sum[i] += g[j];
			}
			end[i] = j % N;
		}
		it = 0;
		for(i = 0; i < N; ++i){
			if(b[it] >= 0)
				break;
			b[it] = i;
			ssum[i+1] = ssum[i] + sum[it];
			it = end[it];
		}
		cir = i-b[it];
		cout << "Case #"<< Case << ": " ;
		cout << ((R-b[it])/cir)*(ssum[i]-ssum[b[it]]) + ssum[(R-b[it])%cir+b[it]] << "\n";
	}
	return 0;
}
