#include <iostream>
#include <queue>

using namespace std;

bool doCase() {
	int N;
	unsigned int K;
	
	cin >> N >> K;

	return ((K ^ (K + 1)) >> N) & 1;
}


int main (int argc, char * const argv[]) {

	int T;
	
	cin >> T;
	
	for(int i = 0; i < T; i++) {
		int result = doCase();
		
		cout << "Case #" << (i + 1) << ": " << (result ? "ON" : "OFF") << endl;
	}
	
	
    return 0;
}
