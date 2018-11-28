#include <iostream>

using namespace std;

int main(){
	int T;
	cin >> T; 
	int count = 1;
	while(T--){
		long long N,K;
		cin >> N >> K;
		long long mod = (1L << N);
		long long val = (K+1)%mod;
		if(val == 0){
			cout << "Case #" << count <<": "<< "ON" << endl;
		}
		else{
			cout << "Case #" << count <<": "<< "OFF" << endl;
		}
		count++;

	}
}
