#include<iostream>

using namespace std;

int main(int argc, char** argv) {

	int T;
	cin >> T;
	for( int t = 0; t < T; t++) {

		int N;
		cin >> N;
		long long int K;
		cin >> K;
		if(K%(1 << N) == ((1 << N) - 1))
			cout << "Case #" << (t+1) << ": " << "ON" << endl;
		else
			cout << "Case #" << (t+1) << ": " << "OFF" << endl;
	}
}
