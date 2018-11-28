#include <iostream>
#include <string>
#include <vector>

using namespace std;

int test;

vector<string> s;
vector<string> q;

int F[101][1001];

int find(int ss, int qq) {
	if (qq == q.size()) return 0;
	if (F[ss][qq] != -1) return F[ss][qq];
	int& res = F[ss][qq]; res = 1e9;
	if (s[ss] == q[qq]) return res = 1e9;
	res = find(ss, qq+1);
	for (int i = 0; i < s.size(); i++)
		res = min(res, find(i, qq+1) + 1);
	return res;
}

void solve() {
	int res = 0;
	
	s.clear(); q.clear();

	int n; cin >> n;
	for (int i = 0; i < n; i++) {
		string tmp; while (tmp == "") getline(cin, tmp);
		s.push_back(tmp);
	}
	cin >> n;
	for (int i = 0; i <n; i++) {
		string tmp; while (tmp == "") getline(cin, tmp);
		q.push_back(tmp);
	}
	
	res = 1e9;

	memset(F, 0xff, sizeof(F));

	for (int i = 0; i < s.size(); i++)
		res = min(res, find(i, 0));

	cout << "Case #" << test << ": " << res << endl;
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int N;
	cin >> N;
	for (test = 1; test <= N; test++)
		solve();
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}