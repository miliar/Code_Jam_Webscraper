#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

#define MAXP 1048576

typedef long long tint;

int P;
tint p[100000], N;
bool isp[MAXP];

int cant(tint primo) {
	int RES = -1;
	for (tint n=1; n<=N; n*=primo) {
		RES++;
	}
	return RES;
}

int main() {

freopen("in.txt", "r", stdin);

int i, j, RES, T, t;

memset(isp, true, sizeof(isp)); P = 0;
for (i=2; i<MAXP; i++) {
	if (isp[i] == true) {
		p[P++] = i;
		for (j=2*i; j<MAXP; j+=i) {
			isp[j] = false;
		}
	}
}

cin >> T;

for (t=1; t<=T; t++) {

cin >> N;

RES = 0; if (N > 1) RES++;
for (i=0; i<P && p[i]*p[i]<=N; i++) {
//	cout << p[i] << ' ' << cant(p[i]) << endl;
	RES += cant(p[i])-1;
}

cout << "Case #" << t << ": " << RES << endl;

}

return 0;
}
