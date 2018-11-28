#include <cstdio>
#include <sstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

char s[1005];

string getLine() {
	fgets(s, 1000, stdin);
	return s;
}

vector <int> getNumbers() {
	string s = getLine();
	vector <int> ret;
	istringstream sin(s);
	int tmp;
	while (sin >> tmp) {
		ret.push_back(tmp);
	}
	return ret;
}

int getNumber() {
	vector <int> t = getNumbers();
	return t[0];
}

int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int N, S, Q;
	N = getNumber();

	vector <int> check;
	map <string, int> engine;
	
	for (int cn = 1; cn <= N; ++cn) {
		printf("Case #%d: ", cn);
		S = getNumber();
		
		for (int i = 0; i < S; ++i) {
			engine[getLine()] = i;
		}
		Q = getNumber();

		check.assign(S, 0);
		int ret = 0, sum = 0;
		for (int i = 0; i < Q; ++i) {
			int t = engine[getLine()];
			if (check[t] == 0) {
				sum++;
				check[t] = 1;
				if (sum == S) {
					ret++;
					check.assign(S, 0);
					sum = 1;
					check[t] = 1;
				}
			}
		}
		printf("%d\n", ret);
	}

}

