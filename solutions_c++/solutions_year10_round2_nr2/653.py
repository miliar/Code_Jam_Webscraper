#include <iostream>

using namespace std;
int main(){
	int C; 
	int N, K, B, T;

	cin >> C;
	
	for(int i = 0; i < C; i++){
		int answer = 0;
		cin >> N;
		cin >> K;
		cin >> B;
		cin >> T;
		int x[50];
		int v[50];
		int dest[50];
		memset(x, 0, N);
		memset(v, 0, N);
		for(int j = 0; j < N; j++){
			cin >> x[j];
		}
		for(int j = 0; j < N; j++){
			cin >> v[j];
			dest[j] = x[j] + v[j] * T;
		}

		int needtopass = 0;
		int canfinish = 0;
		for(int j = N-1; j >= 0 && canfinish < K; j--){
			if(dest[j] < B){
				needtopass++;
			}
			else{
				answer += needtopass;
				canfinish++;
			}
		}
		if(canfinish < K){
			cout << "Case #" << i+1  << ": IMPOSSIBLE" << endl;
			continue;
		}

		cout << "Case #" << i+1  << ": " << answer << endl;;
	}
	return 0;
}