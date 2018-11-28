#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main() {

freopen("in.txt", "r", stdin);

int N, i, SUM, XOR, m, tmp, t, T;

cin >> T;

for (t=1; t<=T; t++) {

cin >> N;

SUM = XOR = 0; m = 1000001;
for (i=0; i<N; i++) {
	cin >> tmp;
	SUM += tmp;
	XOR ^= tmp;
	m = min(m, tmp);
}

cout << "Case #" << t << ": ";
if (XOR !=0) cout << "NO" << endl;
else cout << SUM - m << endl;

}

return 0;
}
