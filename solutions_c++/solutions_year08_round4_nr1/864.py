#include <iostream>
#include <vector>
#include <string>

#define MAX 11000
#define INF 20000

using namespace std;

struct node{
	int type; // 0 - or 1 - and 2 - leaf
	bool changeable;
	int value;
} nodes[MAX];

int computevalue(int n) {
	if (nodes[n].type == 1) {
		computevalue(n * 2);
		computevalue(n * 2 + 1);
		nodes[n].value = (nodes[n * 2].value == 1 && nodes[n * 2 + 1].value == 1)?1:0;
	}
	if (nodes[n].type == 0) {
		computevalue(n * 2);
		computevalue(n * 2 + 1);
		nodes[n].value = (nodes[n * 2].value == 1 || nodes[n * 2 + 1].value == 1)?1:0;
	}
	return nodes[n].value;
}

int calculatechanges(int n, int v) {
	if (nodes[n].value == v) return 0;
	if (nodes[n].type == 2) return INF;

	if (nodes[n].type == 1 && v == 1) { //AND 1
		int wc = INF; int nc = calculatechanges(n * 2, 1) + calculatechanges(n * 2 + 1, 1);
		if (nodes[n].changeable) {
			wc = 1 + min (calculatechanges(n * 2, 1), calculatechanges(n * 2 + 1, 1));
		}
		return min (nc, wc);
	}

	if (nodes[n].type == 1 && v == 0) { //AND 0
		int wc = INF; int nc = min (calculatechanges(n * 2, 0), calculatechanges(n * 2 + 1, 0));
		if (nodes[n].changeable) {
			wc = 1 + calculatechanges(n * 2, 0) + calculatechanges(n * 2 + 1, 0);
		}
		return min (nc, wc);
	}

	if (nodes[n].type == 0 && v == 0) { //OR 0
		int wc = INF; int nc = calculatechanges(n * 2, 0) + calculatechanges(n * 2 + 1, 0);
		if (nodes[n].changeable) {
			wc = 1 + min (calculatechanges(n * 2, 0), calculatechanges(n * 2 + 1, 0));
		}
		return min (nc, wc);
	}

	if (nodes[n].type == 0 && v == 1) { //OR 1
		int wc = INF; int nc = min (calculatechanges(n * 2, 1), calculatechanges(n * 2 + 1, 1));
		if (nodes[n].changeable) {
			wc = 1 + calculatechanges(n * 2, 1) + calculatechanges(n * 2 + 1, 1);
		}
		return min (nc, wc);
	}
}

int main(){
	int ntc; cin >> ntc;
	
	for (int tc = 1; tc <= ntc; tc++) {
		int m, v; cin >> m >> v;
		
		for (int n = 1; n <= (m - 1)/2; n++) {
			int g, c; cin >> g >> c;
			nodes[n].type = g;
			nodes[n].changeable = (c==1);
		}

		for (int n = 1; n <= (m + 1)/2; n++) {
			int i; cin >> i;
			nodes[n + (m - 1)/2].type = 2;
			nodes[n + (m - 1)/2].value = i;
		}
		
		computevalue(1);
		
		int changes = calculatechanges(1, v);
		
		if (changes >= INF) cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << tc << ": " << changes << endl;
	}
	
	return 0;
}