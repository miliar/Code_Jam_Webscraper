#include <iostream>
#include <vector>
using namespace std;

typedef long long LL;

int main(){
	LL Cases;
	cin >> Cases;
	for(LL e2 = 1; e2 <= Cases; e2++){
		// INPUT
		LL R, k, N;
		cout << "Case #" << e2 << ": ";
		cin >> R >> k >> N;
		vector<LL> g(N);
		for(LL i = 0; i < N; i++)
			cin >> g[i];
		
		// PREPROCESSING
		vector<LL> s(N);
		vector<LL> next(N);
		for(LL i = 0; i < N; i++){
			LL people = g[i];
			LL j = (i + 1)%N;
			while (people + g[j] <= k && j != i){
				people += g[j];
				j++;
				if (j == N) j = 0;
			}
			s[i] = people;
			next[i] = j;
		}
		
// 		for(LL i = 0; i < N; i++)
// 			cout << "Si " << i << " está enfrente a la cola se gana " << s[i] << " money\n";
		
		// CYCLE PREPROCESSING
		vector<LL> cicle(N);
		vector<LL> timing(N);
		vector<LL> nextt(N);
		vector<LL> round_and_around(N, 0);
		for(LL i = 0; i < N; i++){
			vector<LL> done(N, 0);
			LL sum = 0;
			LL times = 0;
			LL j = i;
			while(!done[j]){
				sum += s[j];
				done[j] = true;
				j = next[j];
				times++;
			}
			cicle[i] = sum;
			timing[i] = times;
			nextt[i] = j;
			if (nextt[i] == i){
				round_and_around[i] = 1;
			}
		}
		for(LL i = 0; i < N; i++){
			//cout << "El ciclo con " << i << " a la cabeza tiene tamanio " << timing[i] << " y te da " << cicle[i] << " money! " << endl;
			//cout << "El ciclo con " << i << " es circular? " << round_and_around[i] << " y sale en " << nextt[i] << endl;
		}
		
		//GET SOLUTION
		LL res = 0;
		LL pos = 0;
		while(R){
 			//cout << "Me quedan " << R << " vueltas y estoy en " << pos << endl;
			if (R >= timing[pos]){
				if (!round_and_around[pos]){
					res += cicle[pos];
					R -= timing[pos];
					pos = nextt[pos];
				}
				else{
					res += cicle[pos] * (R/timing[pos]);
					R = R%timing[pos];
					pos = nextt[pos];
				}
			}
			else{
				res += s[pos];
				R--;
				pos = next[pos];
			}
		}
		cout << res << endl;
	}
}
