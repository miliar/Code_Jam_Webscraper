#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <set>
#include <sstream>
#include <map>

using namespace std;

int tab[513][513];
bool visited[513][513];
int bestHoriz[513][513];
int bestVerti[513][513];
int bestSize[513][513];
int disc[513];

int convert(char ch) {
	if (isdigit(ch)) return ch - '0';
	return ch - 'A' + 10;
}

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int M, N; cin >> M >> N;
		memset(visited,0,sizeof(visited));
		memset(tab,0,sizeof(tab));
		memset(disc,0,sizeof(disc));
		memset(bestHoriz,0,sizeof(bestHoriz));
		memset(bestVerti,0,sizeof(bestVerti));
		memset(bestSize,0,sizeof(bestSize));
		for (int i = 0; i < M; i++) {
			string str; cin >> str;
			int pos = 0;
			for (int j = 0; j < str.size(); j++) {
				int v = convert(str[j]);
				for (int k = 3; k >= 0; k--) {
					tab[i][pos++] = v & (1 << k) ? 1 : 0;
				}
			}
		}
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				int start = tab[i][j];
				int last = start;
				int cnt = 1;
				for (int k = 1; k + i < M; k++, cnt++) {
					if (tab[k+i][j] == tab[k+i-1][j]) break;
				}
				bestVerti[i][j] = cnt;
				cnt = 1;
				for (int k = 1; k + j < N; k++, cnt++) {
					if (tab[i][k+j] == tab[i][k+j-1]) break;
				}
				bestHoriz[i][j] = cnt;
				//cout << i << "," << j << ": " << bestVerti[i][j] << " and " << bestHoriz[i][j] << "\n";
			}
		}
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				int size = 0;
				//if (i == 14 && j == 0) { cout << "V:" << bestHoriz[i][j] << " and " << bestVerti[i][j] << "\n";}
				for (size = 1; size + i <= M && size + j <= N && size <= bestVerti[i][j]; size++) {
					bool ok = true;
					//if (i == 14 && j == 0) { cout << "V:" << bestHoriz[i][j] << " and " << bestVerti[i][j] << "\n";}
					for (int m = i; m < i + size; m++) {
						if (bestHoriz[m][j] < size) {
							ok = false;
							break;
						}
					}
					if (!ok) {
						break;
					}
					bestSize[i][j] = max(bestSize[i][j], size);
				}
				//cout << "bestSize(" << i << "," << j << "): " << bestSize[i][j] << "\n";
			}
		}
		map<int, set<pair<int,int> > > mappings;
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				//cout << "bestSize(" << i << "," << j << "): " << bestSize[i][j] << "\n";
				mappings[512-bestSize[i][j]].insert(make_pair(i,j));
			}
		}
		int total = 0;
		for (map<int,set<pair<int,int> > >::iterator it = mappings.begin(); it != mappings.end(); it++) {
			for (set<pair<int,int> >::iterator it2 = it->second.begin(); it2 != it->second.end(); it2++) {
				if (!visited[it2->first][it2->second]) {
					int sX = it2->first;
					int sY = it2->second;
					int sZ = 512 - it->first;
					bool conflict = false;
					for (int i = 0; i < sZ && i + sX < M; i++) {
						for (int j = 0; j < sZ && j + sY < N; j++) {
							if (visited[sX+i][sY+j]) { conflict = true; break; }
						}
						if (conflict) break;
					};
					if (conflict) {
						// re-adjust
						mappings[it->first+1].insert(make_pair(sX,sY));
						continue;
					}
					for (int i = 0; i < sZ && i + sX < M; i++) {
						for (int j = 0; j < sZ && j + sY < N; j++) {
							visited[sX+i][sY+j] = true;
						}
					};
					disc[sZ]++;
				}
			}
		}
		int vv = 0;
		for (int i = 512; i >= 0; i--) {
			if (disc[i]) vv++;
		}
		cout << "Case #" << (t+1) << ": " << vv << "\n";
		for (int i = 512; i >= 0; i--) {
			if (disc[i]) cout << i << " " << disc[i] << "\n";
		}
	}
	return 0;
}