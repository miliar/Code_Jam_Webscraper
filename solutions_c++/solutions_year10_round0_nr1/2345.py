#include <iostream>
using namespace std;
#define For_ij(mi, mj) for(int i = 0, j = 0; i < (mi); i+=(j=(j+1)%(mj))==0)
#define For_i(m) for(int i = 0; i < (m); ++i)

inline unsigned int pow(unsigned int x, unsigned int p){
	if(p == 0) return 1;
	if(x == 0) return 0;
	
	unsigned int r = 1;
	for(;;) {
		if(p & 1) r *= x;
		if((p >>= 1) == 0)	return r;
		x *= x;
	}
}

int main(){
	unsigned T, N, K;
	cin >> T;
	for( unsigned t = 1; t <= T; ++t ){
		cin >> N >> K;
		bool off = (K+1) % pow(2, N);
		cout << "Case #" << t << ": " << (off? "OFF": "ON") << endl;
	}
}
