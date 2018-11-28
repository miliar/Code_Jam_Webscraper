#include <iostream>
using namespace std;

int main()
{
	unsigned long long int R, k, temp, answer;
	unsigned int N, T;
	unsigned long long int *g;

	cin >> T;
	for (unsigned int j = 0; j < T; j++) {
		cin >> R;
		cin >> k;
		cin >> N;
		g = new unsigned long long[N];
		for (unsigned int i = 0; i < N; i++) {
			cin >> g[i];
		}
		answer = 0;
		unsigned int index = 0, start = 0;
		for (unsigned long long int i = 0; i < R; i++) {
			temp = 0;
			start = index;
			while(1) {
				if((temp + g[index]) > k) break;
				temp += g[index];
				index = (index + 1) % N;
				if (index == start) break;
			}
			answer += temp;
		}
		cout << "Case #" << j+1 << ": " << answer << ((j == T-1) ? "" : "\n");
		delete[] g; 

	}
	return 0;
}
