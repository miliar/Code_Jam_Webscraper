#include <algorithm>
#include <map>
#include <iostream>
#include <string>
using namespace std;

const int MaxS = 100 + 10;
const int MaxQ = 1000 + 100;
const int INF = MaxQ * 2;

int totCase, caseNum;

int s, q;

string sName[MaxS];
map <string, int> sMap;
int query[MaxQ];

int f[MaxS][MaxQ];

void init();
int switchNum();

int main() {
	cin >> totCase;
	for (int caseNum = 0; caseNum < totCase; ++caseNum) {
		init();
		cout << "Case #" << caseNum + 1 << ": " << switchNum() << endl;
	}
	return 0;
}

void init() {
	sMap.clear();
	cin >> s;
	string tmp;
	getline(cin, tmp);
	for (int i = 0; i < s; ++i) {
		getline(cin, sName[i]);
		sMap[sName[i]] = i;
	}
	cin >> q;
	getline(cin, tmp);
	for (int i = 0; i < q; ++i) {
		getline(cin, tmp);
		query[i] = sMap[tmp];
	}
}

int switchNum() {
	for (int i = 0; i < s; ++i)
		f[0][i] = 0;
	f[0][query[0]] = INF;
	for (int i = 1; i < q; ++i) {
		for (int j = 0; j < s; ++j) {
			if (query[i] == j) {
				f[i][j] = INF;
				continue;
			}
			int opt = INF;
			for (int k = 0; k < s; ++k) {
				int r = 1;
				if (k == j)
					r = 0;
				opt = min(opt, f[i - 1][k] + r);
			}	
			f[i][j] = opt;
		}
	}
	int res = INF;
	for (int i = 0; i < s; ++i)
		res = min(res, f[q - 1][i]);
	return res;
}
