#include<iostream>
using namespace std;
long long f(int x){
	if(x == 1) return 1;
	return 2*f(x-1)+1;
}
int T,N,K;
int main(){
	cin >> T;
	for(int i=1;i<=T;i++){
		cin >> N >> K;
		int x = f(N);
		if(K%(x+1)==x)
			cout << "Case #" << i << ": ON" << endl;
		else
			cout << "Case #" << i << ": OFF" << endl;
	}
}
