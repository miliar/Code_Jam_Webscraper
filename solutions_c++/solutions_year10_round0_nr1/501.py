#include <iostream>

using namespace std;

typedef long long Int;

string bits(Int i){
	string s = "";
	for(int k=0;k<31;k++){
		s = string(1, '0'+i%2) + s;
		i /= 2;
	}
	//if( s == "" ) s = "0";
	return s;
}

int main(int argc, char *argv[])
{
	int T;
	int c = 1;
	//Int m = UINT_MAX;
	//Int mb = (m & ~(m >> 1));

	//cout << bits(m) << endl;
	//cout << bits(mb) << endl;
	cin >> T;
	while(T--){
		int N, K;
		cin >> N >> K;

		/*
		Int s = 0;
		while(K--){
			cout << "K: " << K << endl;
			cout << "state: " << bits(s) << endl;
			Int b = ((~s) & -(~s));
			//cout << b << endl;
			cout << "maximum bit: " << bits(b) << endl;
			if( b == 0 ){
				b = 1;
			}else{
				b = ((s % b) << 1) | 1;
			}
			cout << "fill: " << bits(b) << endl;
			//cout << b << endl;
			s = (s & ~b) | ((s ^ b) & b);
			cout << bits(s) << endl;
		}
		*/
		int p = 1 << N;
		cout << "Case #" << c++ << ": " << ((K%p) == p-1 ? "ON" : "OFF") << endl;
	}
    return 0;
}

