#include <iostream>

using namespace std;

int N, K;

int main(int argc, char* argv) {
	int T;
	cin >>T;
	for(int i=0; i<T; i++) {
		cin >>N >>K;
		N = 1 << N;
		K = K % N;
		cerr <<"2^N=" <<N <<" residual=" <<K <<endl;
		bool on = K == N-1;
		cout <<"Case #" <<i+1 <<": " <<(on?"ON":"OFF") <<endl;
	}
	return 0;
}
