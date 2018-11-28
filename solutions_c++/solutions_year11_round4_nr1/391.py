#include <iostream>
#include <utility>
#include <iomanip>
#include <algorithm>
using namespace std;

int main() {
	int T;
	cin >> T;
	cout << setprecision(10);
	for (int q = 0; q < T; q++) {
		int X, S, R, t, N;
		cin >> X >> S >> R >> t >> N;
		
		pair<int, int> walkways[N+1];
		for (int i = 0; i < N; i++) {
			int b, e, w;
			cin >> b >> e >> w;
			walkways[i].first = w;
			walkways[i].second = e-b;
			X -= (e-b);
		}
		walkways[N].first = 0;
		walkways[N].second = X;
		
		sort(walkways, walkways+N+1);
		long double timeTaken = 0;
		bool stillRunning = true;
		for (int i = 0; i < N+1; i++) {
			if (stillRunning) {
				long double runningTime = ((long double)walkways[i].second)/(walkways[i].first+R);
				if (runningTime+timeTaken <= t) timeTaken += runningTime;
				else {
					long double timeRemaining = t-timeTaken;
					long double spaceLeft = walkways[i].second-timeRemaining*(walkways[i].first+R);
					timeTaken = t+spaceLeft/(walkways[i].first+S);
					stillRunning = false;
				}
			}
			else timeTaken += ((long double)walkways[i].second)/(walkways[i].first+S);
		}
		cout << "Case #" << q+1 << ": " << timeTaken << '\n';
	}
	return 0;
}
