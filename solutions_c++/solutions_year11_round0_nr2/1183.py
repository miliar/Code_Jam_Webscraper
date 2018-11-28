#include <iostream>
#include <cstdio>
#include <memory.h>
#include <vector>
using namespace std;

char table[300][300];
char opz[300];
vector<char> v;
char cha;
int c, x, y, n;
string s;
void check() {
	if (v.size() == 1)
		return;
	while (v.size() > 1 && table[v[int(v.size()) - 1]][v[int(v.size()) - 2]]
			!= 0) {
		cha = table[v[int(v.size()) - 1]][v[int(v.size()) - 2]];
		v.pop_back();
		v.pop_back();
		v.push_back(cha);
	}
	for (int i = 0; i < int(v.size()) - 1; ++i) {
		if (v[i] == opz[v.back()]) {
			v.clear();
			break;
		}
	}
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> c;
	for (int ccc = 1; ccc <= c; ++ccc) {
		memset(table, 0, sizeof(table));
		memset(opz, 0, sizeof(opz));
		v.clear();
		cin >> x;
		for (int i = 0; i < x; ++i) {
			cin >> s;
			table[s[0]][s[1]] = s[2];
			table[s[1]][s[0]] = s[2];
		}
		cin >> y;
		for (int i = 0; i < y; ++i) {
			cin >> s;
			opz[s[0]] = s[1];
			opz[s[1]] = s[0];
		}
		cin >> n;
		cin >> s;
		for (int i = 0; i < n; ++i) {
			v.push_back(s[i]);
			check();
		}
		cout << "Case #" << ccc << ": ";
		cout << '[';
		for (int i = 0; i < int(v.size()) - 1; ++i) {
			cout << v[i] << ", ";
		}
		if (v.size() > 0)
			cout << v.back();
		cout << "]" << endl;
	}
	return 0;
}
