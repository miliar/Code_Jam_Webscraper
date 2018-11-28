#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

static long long findMin(const vector<vector<int> > &C, const vector<int> &m, int y, int x, int seen) {
	if (y==-1) {
		if (m[x]>seen)
			return -1;
		return 0;
	}
	long long cost0_0 = findMin(C, m, y-1, 2*x, seen);
	long long cost0_1 = findMin(C, m, y-1, 2*x+1, seen);
	long long cost0 = cost0_0==-1 || cost0_1==-1 ? -1 : cost0_0 + cost0_1;
	long long cost1_0 = findMin(C, m, y-1, 2*x, seen+1);
	long long cost1_1 = findMin(C, m, y-1, 2*x+1, seen+1);
	long long cost1 = cost1_0==-1 || cost1_1==-1 ? -1 : cost1_0 + cost1_1 + C[y][x];
	if (cost0==-1)
		return cost1;
	if (cost1==-1)
		return cost0;
	return cost0<cost1 ? cost0 : cost1;
}

static long long runTest() {
	int P;
	cin >> P;
	vector<int> M(1<<P);
	for (unsigned int i=0; i<M.size(); i++) {
		cin >> M[i];
		M[i] = P - M[i];
	}
	vector<vector<int> > C(P);
	for (int i=0; i<P; i++) {
		C[i].resize(1<<(P-i-1));
		for (unsigned int j=0; j<C[i].size(); j++)
			cin >> C[i][j];
	}
	return findMin(C, M, P-1, 0, 0);
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++)
		cout << "Case #" << (i+1) << ": " << runTest() << endl;
	return 0;
}
