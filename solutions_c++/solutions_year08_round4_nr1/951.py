#include <iostream>
#define INF 200000000
#define min(a, b) ((a < b) ? a : b)

using namespace std;

int v[10000], logic[10000];
int gate[10000];
int node;
int flag = 0;
int NN, N;

int t, i, ans, wh;

int getanswer(int n, int x) {
	int a, b, tmp, tmp2;

	if (v[n] == x) return 0;
	if (n > (node-1)/2) return INF;

	if (gate[n]) {
		if (logic[n]) {
			if ((v[2*n] == 1 || v[2*n+1] == 1) == x) return 1;
		}
		else {
			if ((v[2*n] == 1 && v[2*n+1] == 1) == x) return 1;
		}
	}

	if (logic[n] && !x) {
		a = getanswer(2*n, 0);
		b = getanswer(2*n+1, 0);
		if (a == INF && b == INF) return INF;
		else return min(a, b);
	}
	else if (!logic[n] && x) {
		a = getanswer(2*n, 1);
		b = getanswer(2*n+1, 1);
		if (a == INF && b == INF) return INF;
		else return min(a, b);
	}
	else if (!logic[n] && !x) {
		if (v[2*n] == 0) a = 0; else a = getanswer(2*n, 0);
		if (v[2*n+1] == 0) b = 0; else b = getanswer(2*n+1, 0);
		if (a == INF || b == INF) tmp = INF;
		else tmp = a + b;

		if (gate[n]) {
			tmp2 = min(a, b);
			tmp2++;

			if (tmp2 < tmp) return tmp2;
		}

		if (tmp == INF) return INF;
		return tmp;
	}
	else if (logic[n] && x) {
		if (v[2*n] == 1) a = 0; else a = getanswer(2*n, 1);
		if (v[2*n+1] == 1) b = 0; else b = getanswer(2*n+1, 1);
		if (a == INF || b == INF) tmp = INF;
		else tmp = a + b;

		if (gate[n]) {
			tmp2 = min(a, b);
			tmp2++;
			
			if (tmp2 < tmp) return tmp2;
		}

		if (tmp == INF) return INF;
		return tmp;		
	}
}


int main() {
	cin >> N;

	for (NN = 1; NN <= N; NN++) {
		cin >> node >> t;

		wh = 1;
		for (i = 0; i < (node-1)/2; i++) {
			cin >> logic[wh] >> gate[wh];
			wh++;
		}
		for (i = 0; i < (node+1)/2; i++) {
			cin >> v[wh];
			wh++;
		}

		for (i = (node-1)/2; i > 0; i--) {
			if (logic[i]) v[i] = ((v[i*2+1] == 1) && (v[i*2] == 1));
			else{
			  	v[i] = ((v[i*2+1] == 1) || (v[i*2] == 1));
				flag = 1;

			}
		}
		
		ans = getanswer(1, t);

		if (ans == INF)	cout << "Case #" << NN << ": IMPOSSIBLE\n";
		else cout << "Case #" << NN << ": " << ans << endl;
	}
	return 0;
}

