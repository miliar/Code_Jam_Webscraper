#include <stdio.h>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;
#define FOR(A, B) for(A = 0; A < B; A++)

int colors[11];
vector< set<int> > polygons;
int N, C;
bool searching = true;

bool checkValid()
{
	int i, j;
	FOR(i, polygons.size()) {
		bool present[C+1];
		FOR(j, C+1) present[j] = false;
		set<int>::iterator it;
		for(it = polygons[i].begin(); it != polygons[i].end(); it++) {
			present[colors[*it]] = true;
		}
		for(j = 1; j <= C; j++) if(!present[j]) return false;	
	}

	return true;
}

void solve(int index)
{
	if(index == N) {
		if(checkValid()) searching = false;
		return;
	}
	for(int color = 1; color <= C; color++) {
		colors[index+1] = color;
		solve(index+1);
		if(!searching) return;
	}
}



int main()
{
	int T, z;
	scanf("%d", &T);
	FOR(z, T) {
		searching = true;
		printf("Case #%d: ", z+1);
		int M, i, j;
		scanf("%d %d", &N, &M);
		polygons.clear();
		set<int> starting; FOR(i, N) starting.insert(i+1);
		polygons.push_back(starting);
		vector< set<int> > newpolygons;
		int U[11], V[11];
		FOR(i, M) scanf("%d", U+i);
		FOR(i, M) scanf("%d", V+i);
		
		FOR(i, M) {
			newpolygons.clear();
			FOR(j, polygons.size()) {
				if(polygons[j].find(U[i]) != polygons[j].end() && polygons[j].find(V[i]) != polygons[j].end()) {
					set<int> polA; set<int> polB;
					set<int>::iterator it;
					//printf("Polygons: %d\n", polygons.size());
					for(it = polygons[j].begin(); it != polygons[j].end(); it++) {
						if(*it >= U[i] && *it <= V[i]) {
							 polA.insert(*it);
						}
						if(*it <= U[i] || *it >= V[i]) {
							polB.insert(*it);
						}
					}
					newpolygons.push_back(polA);
					newpolygons.push_back(polB);
				}
				else newpolygons.push_back(polygons[j]);
			}
			polygons = newpolygons;
		}
		
		int maxC = N;
		FOR(i, polygons.size()) maxC = min(maxC, (int)polygons[i].size());
		for(C = maxC; C >= 1; C--) {
			solve(0);
			if(!searching) {
				printf("%d\n", C);
				FOR(i, N) { printf("%d", colors[i+1]); if(i != N-1) printf(" "); }
				printf("\n");
				break;
			}
		}
	}
	return 0;
}
