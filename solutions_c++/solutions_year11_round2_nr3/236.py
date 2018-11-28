#include <stdio.h>
#include <vector>
#include <set>
using namespace std;

int N, M, i, j, mm;
int U[10], V[10];
vector<set<int> > rooms;
set<int> p, p1, p2;
vector<set<int> >::iterator it;
set<int>::iterator it2;
int ret[10], best[10], bmm;
bool usd[10];

int ok() {
	bool used[10];
	int i;
	for (i = 1; i <= N+1; i++) {
		used[i] = false;
	}
	for (i = 0; i < N; i++) {
		used[ret[i]] = true;
	}
	if (!used[1]) return 0;
	i = 1;
	while (used[i]) i++;
	int r = i-1;
	for (; i <= N; i++) if (used[i]) return 0;
	return r;
}

int main() {
	int cases,kejs;
	scanf("%d", &cases);
	for (kejs = 1; kejs <= cases; kejs++) {
		printf("Case #%d: ", kejs);
		rooms.clear();
		bmm = 0;
		scanf("%d%d", &N, &M);
		for (i = 1; i <= M; i++) scanf("%d", &U[i]);
		for (i = 1; i <= M; i++) scanf("%d", &V[i]);
		
		for (i = 1; i <= N; i++) {
			p.insert(i);
		}
		rooms.push_back(p);

		for (i = 1; i <= M; i++) {
			for (it = rooms.begin(); it != rooms.end(); ++it) {
				if (it->find(U[i]) != it->end() && it->find(V[i]) != it->end()) {
					// split room
					p1.clear();
					p1.insert(U[i]);
					p1.insert(V[i]);
					j = U[i];
					while (j != V[i]) {
						do {
							j++; if (j > N) j = 1;
						} while (it->find(j) == it->end());
						p1.insert(j);
					}
//					rooms.push_back(p);

					p2.clear();
					p2.insert(U[i]);
					p2.insert(V[i]);
					j = U[i];
					while (j != V[i]) {
						do {
							j--; if (j < 1) j = N;
						} while (it->find(j) == it->end());
						p2.insert(j);
					}
					rooms.erase(it);
					rooms.push_back(p1);
					rooms.push_back(p2);
					break;
				}
			}
		}

/*
		for (i = 0; i < rooms.size(); i++) {
			printf("%d: ", i + 1);
			for (it2 = rooms[i].begin(); it2 != rooms[i].end(); ++it2) {
				printf(" %d", *it2);
			}
			printf("\n");
		}
	*/

		for (i = 0; i < N; i++) ret[i] = 1;
		ret[i] = 0;

		do {

			if ((mm = ok()) > 0 && mm > bmm) {
//				for (i = 0; i < N; i++) printf(" %d", ret[i]);
//				printf("---\n");
				for (it = rooms.begin(); it != rooms.end(); ++it) {
					for (i = 1; i <= N; i++) usd[i] = false;
					for (it2 = it->begin(); it2 != it->end(); ++it2) {
						usd[ret[*it2 - 1]] = true;
					}
					for (i = 1; i <= mm; i++) if (!usd[i]) break;
					if (i <= mm) {
						break;
					}
				}
				if (it == rooms.end()) {
					bmm = mm;
					for (i = 0; i < N; i++) best[i] = ret[i];
				}
			}

			i = 0;
			ret[i]++;
			while (ret[i] > N) {
				ret[i] = 1;
				i++;
				ret[i]++;
			}
		} while (i < N);

		printf("%d\n", bmm);
		printf("%d", best[0]);
		for (i = 1; i < N; i++) {
			printf(" %d", best[i]);
		}
		printf("\n");
	}
	return 0;
}


