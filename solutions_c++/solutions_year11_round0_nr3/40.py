#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	int T;
	cin >> T;

	for (int t=1;t<=T;t++) {
		int N;
		int x;
		cin >> N;
		int total=0, min=100000000, xor=0;
		for (int i=0;i<N;i++) {
			cin >> x;
			total+=x;
			min=x<min?x:min;
			xor^=x;
		}
		cout << "Case #" << t << ": ";
		if (N<2 || xor!=0) cout << "NO";
		else {
			cout << (total-min);
		}
		cout << endl;
	}
	return 0;
}
