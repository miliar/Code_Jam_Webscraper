#include <iostream>
using namespace std;

int main() {
	int N; cin >> N;
	for (int I=0; I<N; ++I) {
		int ksor=0, min=1<<30, sum=0;
		int n; cin >> n;
		for (int i=0; i<n; ++i) {
			int c; cin >> c;
			sum+=c;
			if (c<min) min=c;
			ksor^=c;
		}
		cout << "Case #" << I+1 << ": ";
		if (ksor) {
			cout << "NO";
		} else {
			cout << sum-min;
		}
		cout << endl;
	}
}
