#include <iostream>'
#include <cmath>
#include <cstdio>
#include <string>
using namespace std;

#define INF 1<<31

int S;
unsigned long long RES;
string s;

bool check(unsigned long long x) {
	unsigned long long start, end, mid;

	mid = sqrt(x);
	if (mid*mid == x) return true;
	mid++;
	if (mid*mid == x) return true;
	return false;

/*	start = 0; end = INF;
	while (end-start > 1) {
		mid = (start+end)/2;
		if (mid*mid > x) end = mid;
		else start = mid;
	}
	return (start*start == x) || ((start+1)*(start+1) == x);*/
}

void dfs(int pos, unsigned long long cur) {
	if (pos == S) {
		if (check(cur) == true) RES = cur;
	} else {
		if (s[pos] != '?') dfs(pos+1, cur*2ULL + (unsigned long long)(s[pos]-'0'));
		else {
			dfs(pos+1, cur*2ULL);
			dfs(pos+1, cur*2ULL + 1ULL);
		}
	}
}

int main() {

freopen("in.txt", "r", stdin);

int i, T, t;

cin >> T;

for (t=1; t<=T; t++) {

cin >> s; S = s.size();

dfs(0, 0);

cout << "Case #" << t << ": ";
for (i=S-1; i>=0; i--) {
	cout << ((RES>>i)&1);
}
cout << endl;

}

return 0;
}
