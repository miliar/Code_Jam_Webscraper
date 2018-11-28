#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> a;
int N,K;

void Input() {
	cin >> N >> K;
	a.resize(N);
	for (int i = 0; i < N; ++i) {
		cin >> a[i];
	}
}

void Rotate() {
	for (int i = N - 1; i >= 0; --i) {
		int last = N - 1;
		string tmp(N, '.');
		for (int j = N - 1; j >= 0; --j) {
			if (a[i][j] != '.') {
				tmp[last--] = a[i][j];
			}
		}
		a[i] = tmp;
	}
}

bool CheckCol(int i, int j, char x) {
	for (int t = 0; t < K; ++t) {
		if (j + t >= N)
			return false;
		if (a[i][j + t] != x)
			return false;
	}
	return true;
}

bool CheckRow(int i, int j, char x) {
	for (int t = 0; t < K; ++t) {
		if (i + t >= N)
			return false;
		if (a[i + t][j] != x)
			return false;
	}
	return true;
}

bool CheckLeft(int i, int j, char x) {
	for (int t = 0; t < K; ++t) {
		if (i + t >= N || j + t >= N)
			return false;
		if (a[i + t][j + t] != x)
			return false;
	}
	return true;
}

bool CheckRight(int i, int j, char x) {
	for (int t = 0; t < K; ++t) {
		if (i + t >= N || j - t < 0)
			return false;
		if (a[i + t][j - t] != x)
			return false;
	}
	return true;
}

bool Check(char x) {
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			if (a[i][j] != x)
				continue;
			if (CheckCol(i,j,x) || CheckLeft(i, j, x) || CheckRight(i, j, x) || CheckRow(i, j, x))
				return true;
		}
	}
	return false;
}

string Solve() {
	Rotate();
	bool r = Check('R');
	bool b = Check('B');
	if (r && b) {
		return "Both";
	}
	if (r) {
		return "Red";
	}
	if (b) {
		return "Blue";
	}
	return "Neither";

}

int main() {
	//freopen("in.txt","r",stdin);
	freopen("A-large(2).in","r",stdin);
	freopen("out.txt","w",stdout);
	int ncase;
	cin >> ncase;
	for (int i = 0; i < ncase; ++i) {
		Input();
		string res = Solve();
		cout << "Case #" << i + 1 << ": " << res << endl;
	}
	return 0;
}