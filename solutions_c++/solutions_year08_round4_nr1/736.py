#include <iostream>
#include <vector>

using namespace std;

int op(int opcode, int a, int b)
{
	if (opcode == 1) return a && b;
	else return a || b;
}

int solve(int m, int v, const vector<int>& gs, const vector<int>& cs, const vector<int>& leafs)
{
	struct node
	{
		node() { min_changes[0] = min_changes[1] = -1; }
		node(int to0, int to1) { min_changes[0] = to0; min_changes[1] = to1; }
		int min_changes[2];
	};
	vector<node> nodes(m);
	for (int i = (m-1)/2, j = 0; i < m; ++i, ++j) nodes[i] = node(leafs[j] == 0 ? 0 : -1, leafs[j] == 1 ? 0 : -1);


	//for (int i = 0; i < m; ++i) {
	//	cout << "Node " << i << ": [0]=" << nodes[i].min_changes[0] << ",[1]=" << nodes[i].min_changes[1] << endl;
	//}


	for (int i = (m-1)/2 - 1; i >= 0; --i) {
		node nodea = nodes[2 * i + 1], nodeb = nodes[2 * i + 2];


		//cout << "Node " << i << 
		//	"; nodea[0]=" << nodea.min_changes[0] << ", nodea[1]=" << nodea.min_changes[1] <<
		//	"; nodeb[0]=" << nodeb.min_changes[0] << ", nodeb[1]=" << nodeb.min_changes[1] << endl;
		
			
		for (int thisop = 0; thisop < 2; ++thisop) for (int k0 = 0; k0 < 2; ++k0) for (int k1 = 0; k1 < 2; ++k1) {
			if (thisop != gs[i] && cs[i] == 0) continue;
			if (nodea.min_changes[k0] != -1 && nodeb.min_changes[k1] != -1) {
				int res = op(thisop, k0, k1);
				int cop = nodea.min_changes[k0] + nodeb.min_changes[k1] + (thisop == gs[i] ? 0 : 1);
				if (cop < nodes[i].min_changes[res] || nodes[i].min_changes[res] == -1) {
					nodes[i].min_changes[res] = cop;
					//cout << "\t\tshortest way to " << res << " by " << cop << " ops" << endl;
				}
			}
		}

		//cout << "\tnode[0]=" << nodes[i].min_changes[0] << "; node[1]=" << nodes[i].min_changes[1] << endl;

	}

	return nodes[0].min_changes[v];
}

int main()
{
	int tests;
	cin >> tests;
	for (int test = 0; test < tests; ++test) {
		int m, v;
		cin >> m >> v;
		vector<int> gs, cs;
		for (int i = 0; i < (m-1) / 2; ++i) {
			int g, c;
			cin >> g >> c;
			gs.push_back(g);
			cs.push_back(c);
		}
		vector<int> leafs;
		for (int i = 0; i < (m+1) / 2; ++i) {
			int leaf;
			cin >> leaf;
			leafs.push_back(leaf);
		}
		int sol = solve(m, v, gs, cs, leafs);
		cout << "Case #" << (test + 1) << ": ";
		if (sol == -1) cout << "IMPOSSIBLE" << endl;
		else cout << sol << endl;
	}
	return 0;
}