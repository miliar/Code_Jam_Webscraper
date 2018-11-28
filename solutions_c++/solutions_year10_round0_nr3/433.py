#include <iostream>
#include <cstring>
using namespace std;

int main() {

freopen("C-large.in", "r", stdin);
freopen("C-large.out", "w", stdout);

int T, t;
long long n[1024], N, i, j, K, R, next[1024], cant[1024], sum[1024], v[1024], S, cur, RES, c, C;

cin >> T;

for (t=1; t<=T; t++) {

cin >> R;
cin >> K;
cin >> N;

for (i=0; i<N; i++) {
	cin >> n[i];
}

//for (i=0; i<N; i++) cout << n[i] << ' '; cout << endl << endl;

for (i=0; i<N; i++) {
	cant[i] = 0;
	for (j=0; j<N; j++) {
		cant[i] += n[(i+j)%N];
		if (cant[i] > K) break;
	}
	if (j < N) cant[i] -= n[(i+j)%N];
	next[i] = (i+j)%N;
}

/*for (i=0; i<N; i++) {
	cout << i << ' ' << cant[i] << ' ' << next[i] << endl;
}*/

memset(v, -1, sizeof(v));
v[0] = sum[0] = S = cur = 0;
while (S < R-1 && v[next[cur]] == -1) {
//	cout << "en el paso S=" << S << " estoy en " << cur << " con la suma " << sum[S] << endl;
	sum[S+1] = sum[S] + cant[cur];
	S++;
	cur = next[cur];
	v[cur] = S;
}

RES = sum[S] + cant[cur];

//cout << "termino en " << cur << " con la suma " << RES << endl;

if (S < R-1) {
	c = RES - sum[v[next[cur]]];
	C = S - v[next[cur]] + 1;

//	cout << C << ' ' << c << endl;

	RES += ((R-S-1)/C)*c;
	cur = next[cur];
	for (i=0; i<(R-S-1)%C; i++) {
		RES += cant[cur];
		cur = next[cur];
	}
}
cout << "Case #" << t << ": " << RES << endl;

}

return 0;
}
