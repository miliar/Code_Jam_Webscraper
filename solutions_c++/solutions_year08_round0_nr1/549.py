#include <iostream>
#include <algorithm>
#include <string>
#include <map>
using namespace std;

const int MAXN = 1010;
const int MAXINT = 1000000;
int n, m;
int a[MAXN], b[MAXN], opt[MAXN][MAXN], pre[MAXN][MAXN];
string sa[MAXN], sb[MAXN];
map<string,int> nameMap;

int getIdOfName(const string &s) {
	if (nameMap.find(s) == nameMap.end()) {
		int id = nameMap.size();
		nameMap.insert(make_pair(s, id));
		return id;
	}
	else
		return nameMap[s];
}

int min(int a, int b) {
	return a < b ? a : b;
}

void printSolution(int i, int j) {
	int k = pre[i][j];
	if (i == 1)
		printf("start from some one\n");
	else {
		printSolution(i-1, k);
		if (k != j)
			printf("at %d, switch from %s to %s\n", i, sa[k].c_str(), sa[j].c_str());
	}
}

void process() {
	int i, j, k;
	string line;

	cin >> n;
	getline(cin, line);
	nameMap.clear();
	for (i = 0; i < n; i++) {
		getline(cin, sa[i]);
		sa[i].erase(sa[i].length()-1);
		a[i] = getIdOfName(sa[i]);
		// printf("a %d: %d\n", i, a[i]);
	}
	cin >> m;
	getline(cin, line);
	for (i = 0; i < m; i++) {
		getline(cin, sb[i]);
		sb[i].erase(sb[i].length()-1);
		b[i] = getIdOfName(sb[i]);
		// printf("b %d: %d\n", i, b[i]);
	}

	memset(opt, 0, sizeof(opt));
	for (i = 2; i <= m; i++)
		for (j = 0; j < n; j++)
			if (b[i-1] == a[j])
				opt[i][j] = MAXINT;
			else {
				opt[i][j] = MAXINT;
				for (k = 0; k < n; k++)
					if (b[i-2] != a[k] && opt[i][j] > opt[i-1][k] + (k!=j)) {
						opt[i][j] = opt[i-1][k] + (k!=j);
						pre[i][j] = k;
					}
				// printf("opt %d, %d: %d\n", i, j, opt[i][j]);
			}
	
	int res = MAXINT;
	int res_k;
	for (i = 0; i < n; i++)
		if (res > opt[m][i]) {
			res = opt[m][i];
			res_k = i;
		}
	cout << res << endl;
	// printSolution(m, res_k);
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i+1 << ": ";
		process();
	}
}

