#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int l, d, n;
vector<string> a;
vector<string> b;

bool map[20][30];

void analyze(string b) {
	memset(map,false, sizeof(map));
	int p=0;
	bool flag = false;
	for (int i=0; i<b.length(); i++) {
		if (b[i] == '(')
			flag = true;
		else if (b[i] == ')') {
			flag = false;
			p++;
		}
		else {
			map[p][b[i]-'a'] = true;
			if (!flag)
				p++;
		}
		if (p>l) {
			memset(map,false, sizeof(map));
			break;
		}
	}
}

bool check(string ans) {
	for (int i=0; i<ans.length(); i++)
		if (!map[i][ans[i]-'a'])
			return false;
	return true;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin >> l >> d >> n;
	for (int i=0; i<d; i++) {
		string tmp;
		cin >> tmp;
		a.push_back(tmp);
	}
	for (int i=0; i<n; i++) {
		string tmp;
		cin >> tmp;
		b.push_back(tmp);
	}
	for (int i=0; i<n; i++) {
		int ret = 0;
		analyze(b[i]);
		for (int j=0; j<d; j++)
			if (check(a[j]))
				ret++;
		cout << "Case #" << i+1 << ": " << ret << endl;
	}
	return 0;
}