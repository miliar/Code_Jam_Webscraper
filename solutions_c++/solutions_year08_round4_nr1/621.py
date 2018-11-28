#include <iostream>
using namespace std;

int DP[2][20000];
int heap[20000];
int gates[2][10000];

int findVal(int i) {
	if(heap[i] < 0) {
		if(gates[0][i] == 1)
			heap[i] = findVal(2*i + 1) * findVal(2*i + 2);
		else {
			heap[i] = findVal(2*i + 1) + findVal(2*i + 2);
			if(heap[i] > 1)
				heap[i] = 1;
		}
	}
	return heap[i];
}

#define INF (int)1E7

int go(int i, int V, int N) {
	if(DP[V][i] != -1)
		return DP[V][i];
	int &ans = DP[V][i];
	int m, m1, m2;
	if(heap[i] == V) {
		ans = 0;
		return ans;
	}
	if(i >= (N-1)/2) {
		ans = INF;
		return ans;
	}
	int c1 = 2*i + 1, c2 = 2*i + 2;
	if(gates[1][i] == 1 && gates[0][i] == 1) {
		if(V == 0) {
			m1 = go(c1, 0, N);
			m2 = go(c2, 0, N);
			m = (m1 < m2) ? m1 : m2;
			ans = m;
			return ans;
		}
		if(heap[c1] == 1 || heap[c2] == 1) {
			ans = 1;
			return ans;
		}
		m1 = go(c1, 1, N);
		m2 = go(c2, 1, N);
		m = (m1 < m2) ? m1 : m2;
		ans = m+1;
		return ans;
	}
	if(gates[1][i] == 1) {
		if(V == 1) {
			m1 = go(c1, 1, N);
			m2 = go(c2, 1, N);
			m = (m1 < m2) ? m1 : m2;
			ans = m;
			return ans;
		}
		if(heap[c1] == 0 || heap[c2] == 0) {
			ans = 1;
			return ans;
		}
		m1 = go(c1, 0, N);
		m2 = go(c2, 0, N);
		m = (m1 < m2) ? m1 : m2;
		ans = m+1;
		return ans;
	}
	if(gates[0][i] == 1) {
		if(V == 0) {
			m1 = go(c1, 0, N);
			m2 = go(c2, 0, N);
			m = (m1 < m2) ? m1 : m2;
			ans = m;
			return ans;
		}
		m1 = go(c1, 1, N);
		m2 = go(c2, 1, N);
		ans = m1 + m2;
		return ans;
	}
	if(V == 1) {
		m1 = go(c1, 1, N);
		m2 = go(c2, 1, N);
		m = (m1 < m2) ? m1 : m2;
		ans = m;
		return ans;
	}
	m1 = go(c1, 0, N);
	m2 = go(c2, 0, N);
	ans = m1 + m2;
	return ans;
}

int main() {
	int N;
	cin >> N;
	for(int m = 1; m <= N; m++) {
		memset(DP, -1, sizeof DP);
		memset(heap, -1, sizeof heap);
		memset(gates, -1, sizeof gates);
		int M, V;
		cin >> M >> V;
		for(int i = 0; i < (M-1)/2; i++)
			cin >> gates[0][i] >> gates[1][i];
		for(int i = (M-1)/2; i < M; i++)
			cin >> heap[i];
		findVal(0);
		if(go(0, V, M) < INF)
			cout << "Case #" << m << ": " << go(0, V, M) << endl;
		else
			cout << "Case #" << m << ": IMPOSSIBLE" << endl;
	}
	return 0;
}