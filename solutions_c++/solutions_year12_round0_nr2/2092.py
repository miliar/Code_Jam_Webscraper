#include <iostream>
using namespace std;

int main()
{
	int T;
	cin >> T;
	getchar();
	for (int i = 1; i <= T; ++i) {
		int N, S, p;
		cin >> N >> S >> p;
		int result = 0;
		for (int j = 0; j < N; ++j) {
			int score;
			cin >> score;
			score -= p;
			if (score < 0) continue;	// impossible to get p as maximum
			int min = score / 2;
			if (p - min > 2) continue;
			if (p - min == 2) {
				if (S > 0) --S;
				else continue;
			}
			result++;
		}
		cout << "Case #" << i << ": " << result << endl;
	}

	return 0;
}
