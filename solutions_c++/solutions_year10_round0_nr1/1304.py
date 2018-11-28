/*
Google CodeJam 2010 - Qualification Round
Leonardo Borges Avelino
Problem A
*/
#include <iostream>

using namespace std;

main(){
	int T, N, K, P;
	cin >> T;
	for(int i=1;i<=T;++i){
		cin >> N >> K;
		P=(N==0?1:2<<(N-1));
		cout << "Case #" << i << ": ";
		if( (K%P)==(P-1) ) cout << "ON" << endl;
		else cout << "OFF" << endl;
	}
}
