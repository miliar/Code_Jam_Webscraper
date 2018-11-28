#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

#define MAXN 1024

int n[MAXN], s[MAXN];

struct lap {
	double COST, GAIN;
	int id;
} l[MAXN];

bool operator<(const lap &a, const lap &b) {
	return a.GAIN*b.COST > b.GAIN*a.COST;
}

int main() {

freopen("in.txt", "r", stdin);

int S, R, N, i, tmp1, tmp2, L, k, K;
double RES, T, tmp;

cin >> K;

for (k=1; k<=K; k++) {

cin >> n[0];
cin >> S; s[0] = S;
cin >> R; R -= S;
cin >> T;
cin >> N;

for (i=1; i<=N; i++) {
	cin >> tmp1;
	cin >> tmp2;
	n[i] = tmp2 - tmp1; n[0] -= n[i];
	cin >> s[i]; s[i] += S;
}
L = N+1;

for (i=0; i<L; i++) {
	l[i].COST = ((double)n[i])/((double)(s[i] + R));
	l[i].GAIN = ((double)n[i])/((double)s[i]) - ((double)n[i])/((double)(s[i] + R));
	l[i].id = i;

//	cout << l[i].COST << ' ' << l[i].GAIN << endl;
}
sort(l, l+L);

RES = 0.0; i = 0;
while (i < L && l[i].COST <= T) {
	RES += l[i].COST;
	T -= l[i].COST;
	i++;
}
if (i < L) {
	if (T > 0.0) {
		RES += T;
		tmp = T*(s[l[i].id] + R);
		RES += ((double)n[l[i].id] - tmp)/((double)s[l[i].id]);
		T = 0.0;
		i++;
	}
	while (i < L) {
		RES += l[i].COST + l[i].GAIN;
		i++;
	}
}
printf("Case #%d: %.10lf\n", k, RES);

}

return 0;
}
