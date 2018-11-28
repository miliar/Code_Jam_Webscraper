#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

typedef pair<int, int> pii;

struct student {
	int idx, r;
};

bool operator<(const student& a, const student& b) {
	return a.r > b.r;
}

bool intersects(pii ca, int ra, pii cb, int rb) {
	return abs(ca.first - cb.first) < (ra + rb) &&
		abs(ca.second - cb.second) < (ra + rb);
}

bool on_mat(pii c, int W, int L) {
	return c.first >= 0 && c.first <= W && c.second >= 0 && c.second <= L;
}

bool operator<(const pii& a, const pii& b) {
	return a.second < b.second ||
		(a.second == b.second && a.first > b.first);
}

bool die(pii ca, int ra, pii cb, int rb) {
//	fprintf(stderr, "F %d %d %d / %d %d %d\n", ra, ca.first, ca.second, rb, cb.first, cb.second);
	return false;
}

int main() {
	int T;

	scanf("%d", &T);
	for(int _t = 1; _t <= T; ++_t) {
		int N, W, L;
		scanf("%d%d%d", &N, &W, &L);

		student S[N];
		for(int i = 0; i < N; ++i) {
			S[i].idx = i;
			scanf("%d", &(S[i].r));
		}
		sort(S, S + N);

		pii A[N]; // assignments
		set<pii> corners;

		A[S[0].idx].first = 0;
		A[S[0].idx].second = 0;
		corners.insert(make_pair(0, S[0].r));
		corners.insert(make_pair(S[0].r, 0));
		corners.insert(make_pair(S[0].r, S[0].r));

		for(int i = 1; i < N; ++i) {
			for(set<pii>::iterator it = corners.begin();
					it != corners.end(); ++it) {
				pii c;
				c.first = it->first + S[i].r;
				c.second = it->second;
				if(on_mat(c, W, L)) {
//					fprintf(stderr, "? %d %d %d\n", S[i].r, c.first, c.second);
					bool good_place = true;
					for(int j = 0; j < i && good_place; ++j) {
						good_place &=
							!intersects(c, S[i].r, A[S[j].idx], S[j].r)
							|| die(c, S[i].r, A[S[j].idx], S[j].r);
					}
					if(good_place) {
//						fprintf(stderr, "Y %d %d %d\n", S[i].r, c.first, c.second);
						A[S[i].idx] = c;
						corners.insert(
								make_pair(it->first + 2*S[i].r, it->second));
						corners.insert(
								make_pair(it->first, it->second + S[i].r));
						corners.insert(
								make_pair(c.first + S[i].r, c.second + S[i].r));
						break;
					}
				}
				c.first = 0;
				c.second = it->second + S[i].r;
				if(on_mat(c, W, L)) {
//					fprintf(stderr, "? %d %d %d\n", S[i].r, c.first, c.second);
					bool good_place = true;
					for(int j = 0; j < i && good_place; ++j) {
						good_place &=
							!intersects(c, S[i].r, A[S[j].idx], S[j].r)
							|| die(c, S[i].r, A[S[j].idx], S[j].r);
					}
					if(good_place) {
//						fprintf(stderr, "Y %d %d %d\n", S[i].r, c.first, c.second);
						A[S[i].idx] = c;
						corners.insert(
								make_pair(S[i].r, it->second));
						corners.insert(
								make_pair(0, it->second + 2*S[i].r));
						corners.insert(
								make_pair(S[i].r, c.second + S[i].r));
						break;
					}
				}
			}
		}

		printf("Case #%d:", _t);
		for(int i = 0; i < N; ++i) {
			printf(" %d %d", A[i].first, A[i].second);
		}
		printf("\n");
	}

	return 0;
}
