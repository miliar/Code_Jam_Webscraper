#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int a[10], b[10], x[10], v[10];
int ans;

void getPer(int k, int now) {
	if (now == k) {
		int num = 0;
		for (int i = 0; i < k; i++) {
			num += a[i] * b[x[i]];
		}
		if (num < ans)
			ans = num;
		return;
	}
	for (int i  = 0; i < k; i++) {
		if (v[i] == 0) {
			v[i] = 1;
			x[now] = i;
			getPer(k, now+1);
			v[i] = 0;
		}
	}
}

int main() {
	ifstream fin("a-large.in");
	ofstream fout("output.txt");
	int n;
	fin >> n;
	vector<long long> a, b;

	for (int t = 1; t <= n; t++) {
		a.clear();
		b.clear();
		int k;
		fin >> k;

		long long x;
		for (int i = 0; i < k; i++) {
			fin >> x;
			a.push_back(x);
		}
		for (int i = 0; i < k; i++) {
			fin >> x;
			b.push_back(-x);
		}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		long long ans = 0;
		for (int i = 0 ;i < k; i++) {
			ans += a[i] * b[i];
		}
		fout << "Case #" << t << ": " << -ans << endl;
	}
	return 0;
}
