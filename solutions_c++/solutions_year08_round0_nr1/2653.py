#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

const int S = 11;
const int Q = 101;
int dist[Q][S];
int s, q;

struct Node {
	int s;
	int q;
	int w;
	Node(int _s, int _q, int _w) : s(_s), q(_q), w(_w) {}
	bool operator<(const Node &nd) const {
		return w > nd.w;
	}
};

int dijkstra(const vector<string> &engine, const vector<string> &query)
{
	int cost[Q][S];
	fill(&cost[0][0], &cost[Q-1][S], INT_MAX);

	priority_queue<Node> node;
	for (int i=0; i < s; ++i) {
		cost[0][i] = 0;
		node.push(Node(i, dist[0][i], 0));
	}

	int res = INT_MAX;
	while (!node.empty()) {
		Node now = node.top();
		node.pop();
		if (now.q>=q-1) {
			res = now.w;
			break;
		}
		if (cost[now.q][now.s]<now.w) continue;
		cost[now.q][now.s] = now.w;

		for (int i=0; i < s; ++i) {
			if (now.s==i) continue;
			if (engine[i]==query[now.q]) continue;
			node.push(Node(i, now.q+dist[now.q][i], now.w+1));
		}
	}
	if (res==INT_MAX) return -1;

	return res;
}

int main()
{
	int T;
	for (cin>>T; T>0; --T) {
		cin >> s;

		string buf;
		getline(cin, buf);
		vector<string> engine;
		for (int i=0; i < s; ++i) {
			getline(cin, buf);
			engine.push_back(buf);
		}

		cin >> q;
		getline(cin, buf);
		vector<string> query;
		for (int i=0; i < q; ++i) {
			getline(cin, buf);
			query.push_back(buf);
		}

		for (int i=0; i < q; ++i) {
			for (int j=0; j < s; ++j) {
				int t = 0;
				for (int k=i+1; k < q; ++k) {
					++t;
					if (query[k] == engine[j]) {
						break;
					}
				}
				dist[i][j] = t;
			}
		}

		static int counter = 0;
		cout << "Case #" << ++counter << ": " << dijkstra(engine, query) << endl;
	}
	return 0;
}

