#include <queue>
#include <vector>
#include <math.h>
#include <iostream>
using namespace std;

#define forn(i,n) for(int i=0;i<n;i++)

typedef vector<bool> vbool;

int main(){
	int T; cin >> T;
	forn(t,T){
		long long int N, K; cin >> N >> K;
		long long int pot = pow(2,N);
		long long int rem = K%pot;
		cout << "Case #" << t+1 << ": " << ( rem==pot-1 ? "ON" : "OFF" ) << endl;
	}
	return 0;
}
