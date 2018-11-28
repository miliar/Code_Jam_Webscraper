#include <iostream>
using namespace std;

#define MAXN 256
#define EPS 1E-9

typedef long long tint;

int N;
tint D;

struct grupo {
	tint s, e, t;
} n[MAXN];

bool operator<(const grupo &g1, const grupo &g2) {
	if (g1.s != g2.s) return g1.s < g2.s;
	else return g1.e < g2.e;
}

bool check(tint t) {
	tint tmp, last = n[0].e - (t - n[0].t);
	int i;

//	cout << "last = " << last/2.0 << endl;
	for (i=1; i<N; i++) {
//		cout << "considerando el intervalo (" << n[i].s/2.0 << ", " << n[i].e/2.0 << ")" << endl;
		if (n[i].s < last + 2*D) {
			tmp = last + 2*D - n[i].s;
			if (tmp > t - n[i].t) return false;
			else last = n[i].e + tmp;
		} else {
			tmp = min(t - n[i].t, n[i].s - (last + 2*D));
			last = n[i].e - tmp;
		}
//		cout << "last = " << last/2.0 << endl;
	}
	return true;
}

int main() {

freopen("in.txt", "r", stdin);

int V, SumV, i, t, T;
tint P, s, e, mid;

cin >> T;

for (t=1; t<=T; t++) {

cin >> N;
cin >> D;

s = SumV = 0;
for (i=0; i<N; i++) {
	cin >> P; P *= 2;
	cin >> V; SumV += V;

	n[i].t = (V-1)*D;
	n[i].s = P - D*(V-1);
	n[i].e = P + D*(V-1);

	s = max(s, n[i].t);

//	cout << P/2.0 << ' ' << V << " (" << n[i].s/2.0 << ", " << n[i].e/2.0 << ") " << n[i].t << endl;
}
e = SumV*D;

//sort(n, n+N);

while (s < e - 1) {
	mid = (s+e)/2;
	if (check(mid) == true) e = mid;
	else s = mid;
}
if (check(s) == false) s++;

printf("Case #%d: %.1lf\n", t, s/2.0);

}

return 0;
}
