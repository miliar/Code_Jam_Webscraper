#include <iostream>
using namespace std;

int main() {
    int T;
    int N;
    cin >> T;
    for ( int casei = 1; casei <= T; casei++ ) {
	cin >> N;
	char matrix[N+2][N+2];
	int ones[N+1];
	for ( int i = 0; i < N; i++ ) {
	    ones[i] = 0;
	    for ( int j = 0; j < N; j++ ) {
		cin >> matrix[i][j];
		if ( matrix[i][j] == '1' ) {
		    ones[i] = j ;
		}
	    }
	}
	int sum = 0;
	for ( int i = 0; i < N; i++ ) {
	    if ( ones[i] <= i ) continue;
	    for ( int j = i+1; j < N; j++ ) {
		if ( ones[j] > i ) continue;
		sum = sum + j - i;
		for ( int k = j; k > i; k-- ) {
		    ones[k] = ones[k-1];
		}
		break;
	    }
	}
	cout << "Case #" << casei << ": " <<  sum << endl;
    }
}
