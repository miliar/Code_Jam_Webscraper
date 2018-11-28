#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int T, N, S, p, t[100];
	
	cin >> T;
	for(int numCase = 1; numCase <= T; numCase++) {
		cin >> N >> S >> p;
		
		for(int i = 0; i < N; i++) {
			cin >> t[i];
		}
		
		sort(t, t + N);
		
		int result = 0, p1 = max(3*p - 2, p), p2 = max(3*p - 4, p);
		for(int i = 0; i < N; i++) {
			if (p1 <= t[i]) {
				result += (N - i);
				break;
			} else if (S && p2 <= t[i]) {
				result++;
				S--;
			}
		}
		
		cout << "Case #" << numCase << ": " << result << endl;
	}
}
