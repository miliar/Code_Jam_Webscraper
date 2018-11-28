#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <list>
#include <fstream>
#include <cstring>

using namespace std;
static const double EPS = 1e-5;
typedef long long ll;

#include <vector>
#include <map>
#include <utility>
#include <queue>
#include <algorithm>
#include <climits>


static const int NOT_LABELED = -1;
static const int MAX_NODES = 2048;

typedef ll TYPE;

class MinimumCostFlow
{
public:
	MinimumCostFlow(int numberOfNodes) {
		this->numberOfNodes = numberOfNodes;
		//EMPTY = LLONG_MAX / 2;
		EMPTY = INT_MAX / 2;
	}
	void addEdge(int from, int to, TYPE cost, TYPE flow){
		map<TYPE, TYPE>& edges = graph[from][to];
		if ((edges[cost] += flow) == 0){
			edges.erase(cost);
			if (edges.empty()){
				graph[from].erase(to);
			}
		}
	}
	void get(int start, int goal, TYPE maxFlow, TYPE& totalCost, TYPE& totalFlow){
		TYPE restFlow = maxFlow;
		totalCost = 0;
		totalFlow = 0;
		vector<int> path;
		while (restFlow > 0 && searchPath(start, goal, path)){
			pair<TYPE, TYPE> costAndFlow = getUnitCostAndMaxFlow(path);
			TYPE cost = costAndFlow.first;
			TYPE flow = costAndFlow.second;
			flow = min(restFlow, flow);
			restFlow -= flow;
			totalFlow += flow;
			totalCost += flow * cost;
			updateGraph(path, flow);
		}
	}
private:
	//TYPE EMPTY;
	TYPE EMPTY;
	int numberOfNodes;
	map<int, map<TYPE, TYPE> > graph[MAX_NODES]; //[接続元][接続先]->(コスト,許容量)
	bool searchPath(int start, int goal, vector<int>& path){
		int prevNodes[MAX_NODES];
		fill(prevNodes, prevNodes + numberOfNodes, NOT_LABELED);
		TYPE minCosts[MAX_NODES];
		fill(minCosts, minCosts + numberOfNodes, EMPTY);
		minCosts[start] = 0;
		bool finished = false;
		for (int k = 0; k < numberOfNodes && !finished; ++k){
			finished = true;
			for (int from = 0; from < numberOfNodes; ++from){
				map<int, map<TYPE, TYPE> >& edges = graph[from];
				map<int, map<TYPE, TYPE> >::iterator itEnd = edges.end();
				for (map<int, map<TYPE, TYPE> >::iterator it = edges.begin(); it != itEnd; ++it){
					int to = it->first;
					TYPE cost = it->second.begin()->first;
					if (minCosts[to] > minCosts[from] + cost){
						minCosts[to] = minCosts[from] + cost;
						prevNodes[to] = from;
						finished = false;
					}
				}
			}
		}
		if (minCosts[goal] == EMPTY){
			return false;
		}
		path.clear();
		int now = goal;
		while (now != start){
			path.push_back(now);
			now = prevNodes[now];
		}
		path.push_back(start);
		reverse(path.begin(), path.end());
		return true;
	}
	pair<TYPE, TYPE> getUnitCostAndMaxFlow(const vector<int>& path){//(コスト,許容量)
		TYPE minFlow = INT_MAX;
		TYPE cost = 0;
		for (int i = 0; i < path.size() - 1; ++i){
			int from = path[i];
			int to = path[i + 1];
			const pair<TYPE, TYPE>& p = *graph[from].find(to)->second.begin();
			minFlow = min(minFlow, p.second);
			cost += p.first;
		}
		return make_pair(cost, minFlow);
	}
	void updateGraph(const vector<int>& path, TYPE flow){
		for (int i = 0; i < path.size() - 1; ++i){
			int from = path[i];
			int to = path[i + 1];
			TYPE cost = graph[from].find(to)->second.begin()->first;
			graph[to][from][-cost] += flow;

			if ((graph[from][to][cost] -= flow) == 0){
				graph[from][to].erase(cost);
				if (graph[from][to].empty()){
					graph[from].erase(to);
				}
			}
		}
	}
};

#include <iostream>

static const int OFFSET = 100000;

int main()
{
	int T;
	cin >> T;

	for (int testCase = 1; testCase <= T; ++testCase){
		int n;
		cin >> n;

		MinimumCostFlow flow(n * 2 + 10);

		vector<ll> froms;
		vector<ll> tos;
		for (int from = 0; from < n; ++from){
			int in;
			cin >> in;
			froms.push_back(in);
		}
		for (int to = 0; to < n; ++to){
			int in;
			cin >> in;
			tos.push_back(in);
		}
		sort(froms.begin(), froms.end());
		sort(tos.begin(), tos.end());

		ll result = 0x3fffffffffffffffLL;
		do {
			ll temp = 0;
			for (int i = 0; i < n; ++i){
				temp += froms[i] * tos[i];
			}
			result = min(result, temp);

		} while (next_permutation(froms.begin(), froms.end()));

		cout << "Case #" << testCase << ": " << result << endl;
	}
}
