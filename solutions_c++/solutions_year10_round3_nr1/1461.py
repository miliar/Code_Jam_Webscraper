
#include <iostream>
#include <algorithm>

using namespace std;

class points {
public:
	int a, b;
	int posa, posb;
};

points p[2000];
int N;

bool preda(points p1, points p2) {
	if(p1.a < p2.a) return true;
	return false;
}

bool predb(points p1, points p2) {
	if(p1.b < p2.b) return true;
	return false;
}

int main() {
	
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
//	freopen("A-large.in", "r", stdin);
//	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {

		cin >> N;
		for(int i = 0; i < N; i++) cin >> p[i].a >> p[i].b;
		sort(&p[0], &p[N], preda);
		for(int i = 0; i < N; i++) p[i].posa = i;
		sort(&p[0], &p[N], predb);
		for(int i = 0; i < N; i++) p[i].posb = i;
		int res = 0;
		for(int i = 0; i < N; i++) if(p[i].posa < p[i].posb) res += p[i].posb - p[i].posa;
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}