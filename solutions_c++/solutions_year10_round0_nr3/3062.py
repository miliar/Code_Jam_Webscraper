#include<iostream>
#include<fstream>

using namespace std;

typedef long double ld;

int main(int argc, char** argv) {

	ld T;
	cin >> T;

	for(ld t = 0; t < T; t++) {
		ld R, k;
		int N;
		cin >> R;
		cin >> k;
		cin >> N;
		ld g[N];
		for(int n = 0; n < N; n++){
			cin >> g[n];
		}

		int ind[N];
		ld num[N];
		
		int cur_idx = 0;
		ld total = 0;

		for(int i = 0; i < N; i++) {
			ld sum = 0;
			int idx = i;
			for(int j = 0; j < N; j++) {

				if(sum + g[idx] > k) {
					idx = (idx-1)%N;
					break;
				}
				sum += g[idx];
				idx = (idx+1)%N;
			}
			ind[i] = idx;
			num[i] = sum;
		}

		for(ld r = 0; r < R; r++) {
			total += num[cur_idx];
			cur_idx = (ind[cur_idx] + 1)%N;
		}
		cout << "Case #" << (t+1) << ": " << total << std::endl;
	}

}
