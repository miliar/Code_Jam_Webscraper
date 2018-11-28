#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>


const long double eps = 1e-9;

using namespace std;

namespace TTT{



int k;
string s;

void Load()
{
	cin >> k>> s;
}


void Solve()
{
	vector <int> tmp;
	int i, j;
	for (i = 1; i <= k; i++) tmp.push_back(i);
	int res = -1;
	string ts = s;
	do {
		for (i = 0; i < s.size(); i += k) {
			for (j = 0; j < tmp.size(); j++) ts[i + j] = s[i + tmp[j] - 1];
		}
		j = 1;
		for (i = 1; i < ts.size(); i++) {
			if ( ts[i] != ts[i - 1]) j++;
		}
		if (res < 0 || res > j) res = j;
	}while (next_permutation(tmp.begin(), tmp.end()));
	cout << res << "\n";
}

void Save()
{
}
}
using namespace TTT;

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve();
		Save();
	}
	return 0;
}