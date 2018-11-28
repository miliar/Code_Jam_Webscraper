#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main (void) {
    int T = 0;
    cin >> T;

    for (int c = 1; c<=T; ++c) {
	int N;
	cin >> N;

	long X = 0;
	long min = 0;
	long sum = 0;
	for (int i = 0; i<N; ++i) {
	    long C;
	    cin >> C;
	    X ^= C;
	    if (min == 0 or C<min) min = C;
	    sum += C;
	}

	cout<<"Case #"<<c<<": ";
	if (X != 0) {
	    cout<<"NO"<<endl;
	} else {
	    cout<<sum-min<<endl;
	}
    }

    return 0;
}
