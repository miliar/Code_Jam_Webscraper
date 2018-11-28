#include <climits>
#include <iostream>
#include <queue>
#include <vector>
#include <map>

using namespace std;

int S, Q, X;
vector<int> queries;
vector<string> search_engines;

inline int cost(int i, int j) {
	int c = INT_MAX / 2;
	int q1 = i / S;
	int s1 = i % S;
	int q2 = j / S;
	int s2 = j % S;

	if (i >= X - 2 && j >= X - 2)
		return c;

	if (q2 == 0     && queries[q2] != s2 && i == X - 2)
		return 0;

	if (q1 == Q - 1 && queries[q1] != s1 && j == X - 1)
		return 0;

	if (q1 + 1 == q2 && queries[q1] != s1 && queries[q2] != s2)
		return (s1 == s2) ? 0 : 1;

/*	if (c != INT_MAX / 2)
		cout << q1<< "("<<search_engines[s1]<<") "<< q2 << "("<<search_engines[s2]<<") " << c << "\n";*/
	return c;
}

int
main(int argc, char **argv)
{
	int N, n;
	cin >> N;
	for (n = 0; n < N; n++) {
		char name[101];
		search_engines.clear();
		map<string, int> search_engine_map;

		cin >> S; cin.getline(name, 101);
		for (int i = 0; i < S; i++) {
			cin.getline(name, 101);
			string n = name;
			search_engines.push_back(n);
			search_engine_map[n] = i;
		}

		cin >> Q; cin.getline(name, 101);
		queries.clear();
		for (int i = 0; i < Q; i++) {
			cin.getline(name, 101);
			string n = name;
			queries.push_back(search_engine_map[n]);
		}

		if (Q == 0) {
			cout << "Case #" << n + 1 << ": 0\n";
			continue;
		}

		X = Q * S + 2;
		vector<bool> visited(X, false);
		vector<int> dist(X, INT_MAX / 2);
		priority_queue<pair<int, int> > queue;

		dist[X-2] = 0;
		queue.push(make_pair(0, X-2));

		while (!queue.empty()) {
			int u = queue.top().second;
			queue.pop();
			if (u == X - 1) {
				break;
			}
			//cout << "visiting " << u << " " << dist[u] << endl;
			if (!visited[u]) {
				int v0, v1, q = (u == X - 2) ? 0 : 1 + u / S;
				
				if (q == Q) {
					v0 = X - 1;
					v1 = X;
				}
				else {
					v0 = q * S;
					v1 = (q + 1) * S;
				}
				//cout << "v0 " << v0 << " v1 " << v1 << endl;

				for (int v = v0; v < v1; v++) {
					//cout << " " << u << " -> " << v << " " << dist[u] << endl;
					if (!visited[v]) {
						int d = dist[u] + cost(u, v);
						if (d < dist[v]) {
							dist[v] = d;
							queue.push(make_pair(-d, v));
						}
					}
				}
				visited[u] = true;
			}
		}

		cout << "Case #" << n + 1 << ": " << dist[X-1] << "\n";

	}
	return 0;
}

