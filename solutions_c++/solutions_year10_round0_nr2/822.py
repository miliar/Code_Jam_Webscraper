#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef unsigned int uint;

uint gcd( uint a, uint b ){
	if ( b == 0 ) return a;
	return gcd( b, a % b );
}

uint op_minus( uint a, uint b){
	return a > b ? a - b : b - a;
}

void print( uint a ){
	cout << a << " ";
}

int main(){
	uint c, n, tmp;
	cin >> c;
	for (uint i=1; i<=c; i++){
		cin >> n;
		vector<uint> t;
		for (uint j=0; j<n; j++){
			cin >> tmp;
			t.push_back( tmp );
		}
		transform( t.begin(), t.end()-1, t.begin()+1, t.begin(), op_minus );
		//cout << "t: ";
		//for_each( t.begin(), t.end(), print );
		transform( t.begin(), t.end()-2, t.begin()+1, t.begin()+1, gcd );
		//cout << "t2: ";
		//for_each( t.begin(), t.end(), print );
		//cout << endl;
		uint remainder =  t.back() % *(t.end()-2);
		cout << "Case #" << i << ": " <<
						(remainder > 0 ?  *(t.end()-2) - remainder : 0 )<< endl;
	}
}
