#include <iostream>
#include <list>

using namespace std;

int main() {
	int T, R, k, N, i;
	cin >> T;
	i = T;
	while(T--) {
		list<int> passengers;
		list<int> riding;
		cin >> R >> k >> N;
		while(N--) {
			int g_i;
			cin >> g_i;
			passengers.push_back(g_i);
		}
		int sum = 0, times = 0, money = 0;
		while(times < R) {
			sum = 0;
			riding.clear();
			while(sum <= k && !passengers.empty()) {
				int p = *(passengers.begin());
				passengers.pop_front();
				riding.push_back(p);
				sum += p;
				if(passengers.empty() || sum + *(passengers.begin()) > k) break;
			}
			while(!riding.empty()) {
				passengers.push_back(*(riding.begin()));
				riding.pop_front();
			}
			money += sum;
			times++;
		}

		cout << "Case #" << (i-T) << ": " << money << endl;			
	}
}
