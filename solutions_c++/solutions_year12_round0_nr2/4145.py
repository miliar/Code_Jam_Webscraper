#include <iostream>

using namespace std;

int main() {
	int T;

	cin >> T;

	for (int t=0; t<T; t++) {
		int N,S,p,ti,lowestSup,lowestNonSup, count;

		cin >> N;
		cin >> S;
		cin >> p;

		lowestNonSup = p + 2*(p-1);
		lowestSup    = p + 2*(p-2);

		count = 0;
		for (int n=0; n<N; n++) {
			cin >> ti;
			if (ti >= lowestNonSup) count++;
			else if (ti >= 2 && ti <= 28 && ti >= lowestSup && S > 0) {
				count++;
				
				S--;
			}
		}

		cout << "Case #" << t+1 << ": " << count << endl;
	}
	return 0;
}
