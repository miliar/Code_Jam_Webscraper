#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;


map<string, int> m;
vector< vector<int> > v(1007);



inline int max(int a, int b) {
	return (a > b)? a: b;
}


int findMaxChildren(int k) {
	
	int children = v[k].size();
	int ret = children;

	for (int i = 0; i < children; i++) {
		ret = max(children, findMaxChildren(v[k][i]));
	}
	
	return ret;
}


int main() {
	int C;
	cin >> C;

	for (int t = 1; t <= C; t++) {
		int N;
		cin >> N;

		for (int i = 0; i < N; i++) {
			v[i].clear();
		}

		m.clear();
		
		for (int i = 0; i < N; i++) {
			string mix;
			cin >> mix;

			if (m.find(mix) == m.end()) {
				int k = m.size();
				m[mix] = k;
			}

			int par = m[mix];
			
			int M;
			cin >> M;

			for (int j = 0; j < M; j++) {
				string ing;

				cin >> ing;
				
				if (ing[0] > 'Z') continue;

				if (m.find(ing) == m.end()) {
					int k = m.size();
					m[ing] = k;
				}

				v[par].push_back(m[ing]);
			}
		}

		int ret = findMaxChildren(0) + 1;

		ret = 0;

		vector<int> perm;
		for (int i = 0; i < N; i++) {
			perm.push_back(i);
		}


		int best = 3000;
		int made[20];

		do {
			int bowls = 0;
			int free = 0;

			memset(made, 0, sizeof(made));

			int good = 1;
			
			for (int i = 0; i < N; i++) {
				int k = perm[i];

				for (int j = 0; j < v[k].size(); j++) {
					if (!made[v[k][j]]) {
						good = 0;
						break;
					}
				}

				if (!good) break;

				int need = v[k].size();
				
				if (free == 0) {
					bowls++;
					free = need;
				} else {
					free = free - 1 + need;
				}
				
				made[k] = 1;
			}

			if (good) best = min(best, bowls);
		} while(next_permutation(perm.begin(), perm.end()));

		cout << "Case #" << t << ": " << best << endl;
	}

	return 0;
}




