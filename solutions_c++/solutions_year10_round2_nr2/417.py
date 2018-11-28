#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int func2(vector<int>& a, int k, int n) {
	int r = 0;
	a.push_back(n);
	for (int i = 1; i <= k; ++ i) {
		r += (k-i+1) * (a[a.size()-i]-a[a.size()-i-1]-1);
	}
	return r;
}

string func(int K, int B, int T, vector<int>& X, vector<int>& V) {
	int N = X.size();
	vector<int> a;
	for (int i = 0; i < N; ++ i) {
		if (X[i] + V[i]*T >= B) a.push_back(i);
	}
	if ((int)a.size() < K) return "IMPOSSIBLE";
	ostringstream out;
	out << func2(a, K, N);
	return out.str();
}

int main() {
	string buf;
	getline(cin, buf);
	int C = atoi(buf.c_str());
	for (int i = 1; i <= C; ++ i) {
		int N, K, B, T;
		cin >> N >> K >> B >> T;
		vector<int> X(N);
		vector<int> V(N);
		for (int j = 0; j < N; ++ j) {
			cin >> X[j];
		}
		for (int j = 0; j < N; ++ j) {
			cin >> V[j];
		}
		cout << "Case #" << i << ": " << func(K, B, T, X, V) << endl;
	}
}
