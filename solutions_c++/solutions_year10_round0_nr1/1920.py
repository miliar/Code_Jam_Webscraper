#include<iostream>
#include<cmath>
#include<bitset>
using namespace std;

int main(){
	int t,N,K;
	cin >> t;
	for(int i=0;i<t;i++){
		cin >> N >> K;
		if(K==0){
			cout << "Case #"<< i+1 <<": OFF" << endl;
			continue;
		}
			
		int totalStates = pow(2,N);
		int finalState = K % totalStates;
		int sum=0;
		bitset <30> b(finalState);
		cout << "Case #"<< i+1 <<": ";
		for(int j=0;j<N;j++){
			sum += b[j];
		}
		if(sum == N)
			cout << "ON" <<endl;
		else
			cout << "OFF" << endl;
	}
	return 0;
}
