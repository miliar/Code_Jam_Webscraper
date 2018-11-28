#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
using namespace std;

int main(void) {
	int T, N, d, l, target;
	
	cin >> T;
	for(int numCase = 1; numCase <= T; numCase++) {
		vector<pair<int, int> > vines;
		
		cin >> N;
		for(int i = 0; i < N; i++) {
			cin >> d >> l;
			
			vines.push_back(make_pair(d, l));
		}
		
		cin >> target;
		
		sort(vines.begin(), vines.end());
		
		map<int, bool> v;
		map<int, int> g;
		queue<int> q;
		bool possible = false;
		
		g[0] = min(vines[0].first, vines[0].second);
		q.push(0);
		
		while (!q.empty()) {
			int curr = q.front(); q.pop();
			int currLength = g[curr];
			
			v[curr] = true;
			
			if (vines[curr].first + currLength >= target) {
				possible = true;
				break;
			}
			
			for (size_t i = curr + 1; (i < vines.size()) && (vines[i].first <= vines[curr].first + currLength); i++) {
				int aux = min(vines[i].second, vines[i].first - vines[curr].first);
				
				if (!v[i] && aux > g[i]) {
					g[i] = aux;
					q.push(i);
				}
			}
		}
		
		cout << "Case #" << numCase << ": " << (possible ? "YES" : "NO") << endl;
	}
}
