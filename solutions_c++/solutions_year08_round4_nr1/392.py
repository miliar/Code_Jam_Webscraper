#include <iostream>

using namespace std;

int nodes[10010];
bool isAnd[10010];
bool canChange[10010];
bool isLeaf[10010];

int cache[10010][2];

int leftChild(int node) {
	return 2 * (node+1) - 1;
}

int cost(int node, int wantAnd) {
	if (isAnd[node] == wantAnd) return 0;
	int ans= canChange[node] ? 1 : 1<<29;
	return ans;
}

int go(int node, int want) {
	if (isLeaf[node]) {
		int ans = nodes[node] == want ? 0 : 1<<29;
		return ans;
	}

	int &ans = cache[node][want];
	if(ans>=0) return ans;

	ans = 1<<29;
	for(int le=0; le<=1; le++) for(int ri=0; ri<=1; ri++) {
		// AND
		if ((le & ri) == want) {
			ans <?= go(leftChild(node), le) + go(leftChild(node)+1, ri) + cost(node, 1);
		}
		
		// OR
		if ((le | ri) == want) {
			ans <?= go(leftChild(node), le) + go(leftChild(node)+1, ri) + cost(node, 0);
		}
	}
	
	return ans;
}

int main() {
	int cases;
	cin >> cases;
	for(int c=0; c<cases; c++) {
		int noden, want;
		cin >> noden >> want;


		for(int i=0; i<noden; i++) {
			if (i < (noden-1) / 2) {
				cin >> isAnd[i] >> canChange[i];
				isLeaf[i] = false;
			}
			else {
				cin >> nodes[i];
				isLeaf[i] = true;
			}
		}

		memset(cache,-1,sizeof(cache));

		int ans = go(0, want);
		cout << "Case #"<< (c+1)<<": ";
		if (ans >= 1<<29) cout << "IMPOSSIBLE"<<endl;
		else cout << ans<<endl;
		
	}

}
