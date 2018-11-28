#include <iostream>

using namespace std;

int main (void) {
    int T;
    cin >> T;
    for (int c = 1; c<=T; ++c) {
	int N;
	cin >> N;
	int wrong = 0;
	for (int i = 1; i<=N; ++i) {
	    int n;
	    cin >> n;
	    if (i != n) wrong++;
	}
	cout<<"Case #"<<c<<": "<<wrong<<".000000"<<endl;
    }
    return 0;
}
