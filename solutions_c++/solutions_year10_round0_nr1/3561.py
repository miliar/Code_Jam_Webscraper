#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


int main() {
	
	unsigned int T = 0;
	unsigned int K, N;
	cin >> T;
	
	for (int i = 0; i < T; i++) {
		cin >> N >> K;
		cout << "Case #" << (i+1);
		unsigned int tmp = ((~0) ^ (1 << 31)) >> (31 - N) ;
		if ( K >= tmp && (K & tmp) == tmp)
		{
			cout << ": ON";
		}
		else
			cout << ": OFF";
		cout << endl;
	
	}
	
	
	
	
	


}
