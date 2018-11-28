#include <iostream>

using namespace std;

int val[100000];
int isChangeable[100000];
int node;
int caseN, N;
int isAnd[100000];
int rootvalue;
int i;
int ans;
int wh;

int find(int n, int wanted) {
	int tmpa, tmpb, tmpc, tmpd;

	//cout << n << " " << wanted << endl;

	if (val[n] == wanted) return 0;
	if (n > (node-1)/2) return -1;

	if (isChangeable[n]) {
		if (isAnd[n]) {
			if ((val[2*n] == 1 || val[2*n+1] == 1) == wanted) return 1;
		}
		else {
			if ((val[2*n] == 1 && val[2*n+1] == 1) == wanted) return 1;
		}
	}

	if (isAnd[n] && wanted == 0) {
		// both my children are 1
		tmpa = find(2*n, 0);
		tmpb = find(2*n+1, 0);
		if (tmpa == -1 && tmpb == -1) return -1;
		else {
			if (tmpa == -1) tmpd = 1000000000; else tmpd = tmpa;
			if (tmpb != -1 && tmpb < tmpd) tmpd = tmpb;
			return tmpd;
		}

		// No point changing
	}
	else if (isAnd[n] && wanted == 1) {
		// One or both children are zeros
		if (val[2*n] == 1) tmpa = 0; else tmpa = find(2*n, 1);
		if (val[2*n+1] == 1) tmpb = 0; else tmpb = find(2*n+1, 1);
		if (tmpa == -1 || tmpb == -1) tmpc = 1000000000;
		else {
			tmpc = tmpa + tmpb;
			//return tmpc;
		}

		if (isChangeable[n]) {
			if (tmpa == -1) tmpd = 1000000000; else tmpd = tmpa;
			if (tmpb != -1 && tmpb < tmpd) tmpd = tmpb;
			tmpd++;
			
			if (tmpd < tmpc) return tmpd;
		}

		if (tmpc == 1000000000) return -1;
		return tmpc;		
	}
	else if (!isAnd[n] && wanted == 0) {
		// One or both children are 1
		if (val[2*n] == 0) tmpa = 0; else tmpa = find(2*n, 0);
		if (val[2*n+1] == 0) tmpb = 0; else tmpb = find(2*n+1, 0);
		if (tmpa == -1 || tmpb == -1) tmpc = 1000000000;
		else {
			tmpc = tmpa + tmpb;
			//return tmpc;
		}

		if (isChangeable[n]) {
			if (tmpa == -1) tmpd = 1000000000; else tmpd = tmpa;
			if (tmpb != -1 && tmpb < tmpd) tmpd = tmpb;
			tmpd++;

			if (tmpd < tmpc) return tmpd;
		}

		if (tmpc == 1000000000) return -1;
		return tmpc;
	}
	else if (!isAnd[n] && wanted == 1) {
		// Both my children are zeros
		tmpa = find(2*n, 1);
		tmpb = find(2*n+1, 1);
		if (tmpa == -1 && tmpb == -1) return -1;
		else {
			if (tmpa == -1) tmpd = 1000000000; else tmpd = tmpa;
			if (tmpb != -1 && tmpb < tmpd) tmpd = tmpb;
			return tmpd;
		}
	}
}


int main() {
	cin >> caseN;
	for (N = 1; N <= caseN; N++) {
		cin >> node >> rootvalue;

		wh = 1;
		for (i = 0; i < (node-1)/2; i++) {
			cin >> isAnd[wh] >> isChangeable[wh];
			wh++;
		}
		for (i = 0; i < (node+1)/2; i++) {
			cin >> val[wh];
			wh++;
		}

		// Find the values of everything
		for (i = (node-1)/2; i > 0; i--) {
			if (isAnd[i]) {
				val[i] = ((val[i*2+1] == 1) && (val[i*2] == 1));
			}
			else {
				val[i] = ((val[i*2+1] == 1) || (val[i*2] == 1));
			}
		}
/*
		cout << "Values of node:\n";
		for (i = 1; i <= node; i++) cout << val[i] << " ";
		cout << endl;
*/
		ans = find(1, rootvalue);

		if (ans == -1)	cout << "Case #" << N << ": IMPOSSIBLE\n";
		else cout << "Case #" << N << ": " << ans << endl;
	}
	return 0;
}

