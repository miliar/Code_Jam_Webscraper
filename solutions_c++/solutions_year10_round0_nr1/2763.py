#include <iostream>
#include <math.h>

using namespace std;

int main (int argc, char * const argv[]) {
	int T, N;
	long K;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		cin >> N >> K;
		int res = K % ((long) pow(2,N));
		cout << "Case #" << i <<": ";
		if(res == (pow(2,N)-1))
			cout << "ON";
		else
			cout << "OFF";
		if(i < T)
			cout << endl;
			
	}
    return 0;
}
