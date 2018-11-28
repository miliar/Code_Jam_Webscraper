#include <iostream>
#include <queue>
using namespace std;

int main(){
	//freopen("B.in", "r", stdin);
	//freopen("B.out", "w", stdout);

	int tcase;
	cin >> tcase;
	for(int cur_tcase = 0; cur_tcase < tcase; cur_tcase++){
		long long R, K, N;
		queue<long long> g;

		cin >> R >> K >> N;
		for(long long i = 0; i < N; i++){
			long long num;
			cin >> num;
			g.push(num);
		}

		//********************************

		long long all_sum = 0;

		for(long long i = 0; i < R; i++){
			long long rnd_sum = 0, count = 0;

			while(((rnd_sum + g.front()) <= K) && (count < N)){
				long long tmp = g.front();
				g.pop();
				rnd_sum += tmp;
				g.push(tmp);

				count ++;
			}

			all_sum += rnd_sum;
			if(count = 0){
				break;
			}
		}

		cout << "Case #" << cur_tcase + 1 << ": " << all_sum << endl;
	}

	return 0;
}