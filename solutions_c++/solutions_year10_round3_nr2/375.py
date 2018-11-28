#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
using namespace std;
long long T, L, C, P;
int main(){
	cin >> T;
	for(int z=1; z<=T; z++){
		cin >> L >> P >> C;
		long long l = 0;
		while(L*C<P){//<=
			L*=C;
			l++;
		}
		long long result = 0;
		long long i = 1;
		while(i<=l){
			result ++;
			i*=2;
		}
		cout <<"Case #"<<z <<": "<< result<< endl;
	
	
	}
	return 0;
}


