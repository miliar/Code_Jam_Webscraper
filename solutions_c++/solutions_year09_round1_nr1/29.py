#include <iostream>
#include <sstream>
#include <map>

using namespace std;

const int limit = 10;

char str[10000];

int base[1000];
int n;

struct Node {
	int num, base;
	
	Node() {
	}
	
	Node(int num, int base) : num(num), base(base) {
	}
};

bool operator < (const Node &a, const Node &b) {
	return a.num != b.num ? a.num < b.num : a.base < b.base;
}

map<Node, bool> rec;

bool Check(int ans, int base) {
	int i, sum, m;
	for (i = 0; i < limit; i++) {
		for (sum = 0, m = ans; m; sum += (m % base) * (m % base), m /= base);
		ans = sum;
		if (ans == 1) {/*cout << i + 1 << endl; */return 1;}
	}
	return 0;
}

bool Check(int ans) {
	int i;
	for (i = 0; i < n; i++)
		if (!Check(ans, base[i])) return 0;
	return 1;
}

void Solve() {
	cin.getline(str, 10000);
	istringstream in(str);
	n = 0;
	int num;
	while (in >> num)
		base[n++] = num;
	int ans;
	for (ans = 2; ; ans++)
		if (Check(ans)) break;
	cout << ans << endl;
}

int main() {
	int T;
	cin >> T;
	cin.getline(str, 10000);
	int i;
	rec.clear();
	for (i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		Solve();
	}
	return 0;
}