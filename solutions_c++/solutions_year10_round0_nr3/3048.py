#include <iostream>
#include <queue>
using namespace std;

queue<int> q;
int t,n,r,k;
int people[101];
int main() {
	cin >> t;
	int x, peeps;
	for (int i = 0; i < t; i++) {
		cin >> r >> k >> n;
		int total = 0;
		for (int j = 0; j < n; j++) { cin >> x; q.push(x); }
		
		for (int j = 0; j < r; j++) {
		x = 0;
		peeps = 0;
			while (!q.empty() && x + q.front() <= k) { x += q.front(); people[peeps++] = q.front(); q.pop(); }
			total += x;
			for (int k = 0; k < peeps; k++) { q.push(people[k]); people[k] = 0; }
		} 
		cout << "Case #" << i+1 << ": " << total << endl;
		while (!q.empty()) q.pop();
	}
}
