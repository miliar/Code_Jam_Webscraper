#include<iostream>
#include<fstream>

using namespace std;

int main() {
	long long nn, kk;
	int testcase;
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	fin >> testcase;
	for (int i = 0; i < testcase; ++i) {
		fin >> nn >> kk;
		fout << "Case #" << i+1 << ": ";
		++kk;
		nn = (long long(1)) << nn;
		if (kk % nn == 0) fout << "ON\n";
		else fout << "OFF\n";
	}
	fin.close();
	fout.close();
	return 0;

	int n = 10, k = 0;
	cin >> n;
	bool state[100] = {0}, power[100] = {0};
	power[1] = true;

	while (!power[n + 1]) {
		++k;
		for (int i = 1; i <= n; ++i)
			if (power[i]) state[i] = !state[i];
			else break;
		memset(power, 0, sizeof(bool) * 100);
		power[1] = true;
		for (int i = 2; i <= n+1; ++i)
			if (state[i-1]) power[i] = true;
			else break;
	}
	cout << k << endl;
	return 0;
}