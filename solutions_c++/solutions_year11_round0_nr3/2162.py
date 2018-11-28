#include <iostream>
#include <vector>
#include <string>

using namespace std;


int main(){
	int T;
	cin >> T;
	for (int j = 1; j<=T; j++) {
		
		int N;
		long long int sum=0;
		cin >> N;
		vector<int> entrada(N);
		int min = 20000000;
		for (int i = 0; i < N; i++) {
			cin >> entrada[i];
			sum += entrada[i];
			if(entrada[i] < min) min = entrada[i];
		}
		int pot = 1;
		while (pot < sum ) {
			pot = pot * 2;
			
		}
		bool error = false;
		do{
			pot =pot/2;
			int num = 0;
			for (int i = 0; i<N ; i++) {
				if( entrada[i] - pot >=0) {
					entrada[i] -= pot;
					num++;
				}
			}
			if (num%2 != 0) error = true;
		} while (pot!=1 && !error);
		
		if (error) {
			cout << "Case #" << j <<": NO" << endl;
		}
		else cout << "Case #" << j <<": "<< sum - min << endl;
		
	}
}
