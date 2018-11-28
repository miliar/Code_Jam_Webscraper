#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>

#define REP(i,n) for(typeof(n) _n=n, i=0;i<_n;++i)
#define FOREACH(i,x) for(typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define ALL(x) (x).begin(),(x).end()
#define INFTY 1000000

using namespace std;

#define GATE_AND 1
#define GATE_OR 0
#define CHANGE_YES 1
#define CHANGE_NO 0

struct elem{
	int gate;
	int change;
	int val;
	int minTo[2];
};

vector<elem> tree;

void runCase(){
	int m, v;
	cin >> m >> v;
	tree = vector<elem>(m+1);
	for(int i=1; i <= (m-1)/2; i++){
		cin >> tree[i].gate >> tree[i].change;
		tree[i].minTo[0] = INFTY;
		tree[i].minTo[1] = INFTY;
	}
	for(int i=(m-1)/2+1; i<= m; i++){
		cin >> tree[i].val;
		tree[i].minTo[tree[i].val] = 0;
		tree[i].minTo[1-tree[i].val] = INFTY;
	}
	string s;
	getline(cin,s);

	for(int i=(m-1)/2; i >= 1; i--){
		int v1 = tree[2*i].val;
		int v2 = tree[2*i+1].val;
		if (tree[i].gate == GATE_AND)
			tree[i].val = v1 & v2;
		else
			tree[i].val = v1 | v2;
		int v = tree[i].val;
		tree[i].minTo[v] = 0;
		tree[i].minTo[1-v] = INFTY;

		tree[i].minTo[1-v] = INFTY;

		// other gates change
		
		REP(vv1,2) REP(vv2,2) REP(gg,2){
			int vv;
			if (gg == GATE_AND)
				vv = vv1 & vv2;
			else
				vv = vv1 | vv2;
			int cost = tree[2*i].minTo[vv1]+tree[2*i+1].minTo[vv2];
			if (gg != tree[i].gate){
				if (tree[i].change == CHANGE_YES)			
					cost += 1;
				else
					continue;
			}
			if (vv == 1-v)
				tree[i].minTo[vv] = min(tree[i].minTo[vv], cost);
		}

//		cout << i << " " << tree[i].minTo[0] << " " << tree[i].minTo[1] << endl;

	}	

	int minToChange = tree[1].minTo[v];
	if (minToChange < INFTY)
		cout << minToChange << endl;
	else
		cout << "IMPOSSIBLE" << endl;
}

int main(){
	int cases;
	cin >> cases;
	string s;
	getline(cin,s);
	REP(i,cases){
		cout << "Case #" << i+1 << ": ";
		runCase();
	}
	return 0;
}
