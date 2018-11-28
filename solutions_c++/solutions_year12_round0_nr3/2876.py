#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>
using namespace std;

int intSize(int n) {
	int a = 1;
	while (n >=10) {
		n/=10;
		a++;
	}
	return a;
}

string shift(string s, int n) {
	if (n <= 0)
		return s;
	return shift(s.substr(1) + s[0], n-1);
}

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int K;
	cin >> K;
	for (int dataset = 1; dataset <= K; dataset++) {
		int start, end;
		int count = 0;
		cin >> start >> end;
		for (int i = start; i <= end; i++) {
			string s;
			stringstream ss;
			ss << i;
			ss >> s;
			vector<int> v;
			for (int j = 1; j < intSize(i); j++) {
				int x = atoi(shift(s, j).c_str());
				for (int y = start; y < i; y++)
					if (x == y) {
						bool ohmygodthiscodeissoinefficientitsscary = false;
						for (int i = 0; i < v.size(); i++) {
							if (v[i] == x)
								ohmygodthiscodeissoinefficientitsscary = true;
						}
						if (!ohmygodthiscodeissoinefficientitsscary) {
							count++;
							v.push_back(x);
						}
					}
			}
		}
		cout << "Case #" << dataset << ": " << count << endl;
	}
}
