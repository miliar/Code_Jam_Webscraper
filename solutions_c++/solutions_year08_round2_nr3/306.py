#include <iostream>
#include <vector>

using namespace std;

int main() {
	int T;

	cin >> T;

	for(int i = 0; i < T; i++) {
		int K, n;

		cin >> K;
		cin >> n;

		vector<int> ns(n);
		for(int j = 0; j < n; j++) {
			int d;

			cin >> d;
			ns[j] = d;
		}

		vector<int> deck(K);
		vector<bool> taken(K, false);

		int pos = 0, left = K;

		for(int card = 0; card < K; card++) {
			int cnt = 0, seek = card % left;
			while(true) {
				if(!taken[pos]) {
					if(cnt == seek) {
						break;
					}
					cnt++;
				}
				pos = (pos + 1) % K;
			}
			deck[pos] = card;
			taken[pos] = true;
			left--;
			pos = (pos + 1) % K;
		}

		cout << "Case #" << (i + 1) << ":";
		for(int j = 0; j < n; j++) {
			cout << " " << (deck[ns[j] - 1] + 1);
		}
		cout << endl;
	}
}
