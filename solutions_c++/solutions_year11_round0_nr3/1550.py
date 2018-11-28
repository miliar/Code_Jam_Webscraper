#include <iostream>
#include <algorithm>

using namespace std;

int V[ 1000 ];

int main(){
	int T, N;
	int sum;
	
	cin >> T;
	for (int t=1; t<=T; t++){
		cin >> N;
		sum = 0;
		for (int i=0; i<N; i++){
			cin >> V[i];
			sum ^= V[i];
		}
	
		cout << "Case #" << t << ": ";
		if (sum) cout << "NO" << endl;
		else{
			sort( V, V+N );
			for (int i=1; i<N; i++) sum += V[i];
			cout << sum << endl;
		}
	}
	
	return 0;
}
