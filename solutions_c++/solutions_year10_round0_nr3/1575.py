#include <iostream>

using namespace std;

long long r; //number of runs
long long k; //capacity of roller coaster
long long n; //length of queue
long long q[1000]; //the initial queue;
long long to[1000]; //beginning of next queue
long long profit[1000]; //profit front of queue
long long a;
long long b;
long long t;
long long c;

int main() {
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> r >> k >> n;
		for (int x = 0; x < n; x++) {
			cin >> q[x];
		}
		b = 0;
		c = 0;
		long long count = 0;
		for (a = 0; a < n; a++) {
			while (count < n && c + q[b] <= k) {
				count++;
				c += q[b];
				b = (b+1)%n;
			}
			count--;
			profit[a] = c;
			to[a] = b;
			c -= q[a];
		}
		
// 		cout << "Profit" << endl;
// 		for (int z = 0; z < n; z++) {
// 			cout << profit[z] << ' ';
// 		}
// 		cout << endl;
// 		for (int z = 0; z < n; z++) {
// 			cout << to[z] << ' ';
// 		}
// 		cout << endl;
		
		b = 0;
		c = 0;
		for (a = 0; a < r; a++) {
			c += profit[b];
			b = to[b];
		}
		cout << "Case #" << i << ": " << c << endl;
	}
}