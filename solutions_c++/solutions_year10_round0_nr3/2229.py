#include <iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	
	int r, k, n;
	unsigned queue[1000];
	
	for (int i = 1; i <= t; ++i) {
		cin >> r >> k >> n;
		
		for (int j = 0; j < n; ++j) {
			cin >> queue[j];
		}
		
		long long temp = 0, money = 0;
		int it = 0, start;
		for (int j = 0; j < r; ++j) {
			start = it;
			while (1) {
				if (temp + queue[it] > k) {
					break;
				}
				temp += queue[it];
				it = (it + 1) % n;
				if (it == start) break;
			}
			money += temp;
			temp = 0;
		}
		
		cout << "Case #" << i << ": " << money << "\n";
 	}
}