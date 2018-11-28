#include <iostream>
using namespace std;

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		int N;
		cin >> N;
		int sum = 0, xorsum = 0;
		int mini = -1;
		for (int i = 0; i < N; i++) {
			int c;
			cin >> c;
			sum += c;
			xorsum = xorsum ^ c;
			if (mini < 0 || c < mini) mini = c;
		}
		
		if (xorsum != 0)
			cout << "Case #" << icase << ": NO" << endl;
		else
			cout << "Case #" << icase << ": " << sum-mini << endl;
	}
	return 0;
}
