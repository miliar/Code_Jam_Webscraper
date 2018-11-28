#include<iostream>
#include<vector>

using namespace std;

int main() {
	int T, R, k, N;
	int q[1000];

	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> R >> k >> N;
		int s = 0;
		for (int j = 0; j < N; j++) 
			cin >> q[j];
		int s1 = 0, p1 = 0, p2, next;
		for (int j = 0; j < R; j++) {
			s1 = q[p1];
			p2 = p1 + 1;
			next = q[p2 % N];
			while ((p2 - p1) < N && s1 + next <= k) {
				s1 += next;
				next = q[(++p2) % N];
			} 
			p1 = p2 % N;
			s += s1;	
		}	
		cout << "Case #" << i + 1 << ": " << s << endl;	
	}
	return 0;
}
