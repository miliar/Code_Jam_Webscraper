#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define REP(a,b) for(int a=0;a<(b);++a)
#define FOR(a,c,b) for(int a=c;a<(b);++a) 

int bestdst, bestdom;
char v[500];

int dst[500];
int dst2[500];
int nt[500];
char inP[500];

vector <int> al[500];
int n;

void search(int pos, int cnt, int dist) {
	if (pos == 1) {
		if (cnt+1 > bestdom) bestdom = cnt+1;
		return;
	}

	REP(i,al[pos].size()) {
		int next = al[pos][i];
		++nt[next];
		if (nt[next] == 1 && inP[next] == 0) ++cnt;
	}

	REP(i,al[pos].size()) {
		int next = al[pos][i];
		if (dst[next] == dist+1 && dst2[next] == bestdst-dist-1) {
			search(next, cnt-1, dist+1);
		}
	}

	REP(i,al[pos].size()) {
		int next = al[pos][i];
		--nt[next];
	}
}

int main() 
{
	ifstream fin("d.in");
	ofstream fout("d.out");

	int tc;
	int m, a, b;	
	char c;

	fin >> tc;

	REP(tcase,tc) {
		fin >> n >> m;

		REP(i,n) al[i].clear();
		REP(i,m) {
			fin >> a >> c >> b;
			al[a].push_back(b);
			al[b].push_back(a);
		}

		memset(dst, -1, sizeof(dst));
		queue <int> q;
		q.push(0); dst[0] = 0;
		while (!q.empty()) {
			int pos = q.front(); q.pop();
			REP(i,al[pos].size()) {
				int next = al[pos][i];
				if (dst[next] < 0) {
					dst[next] = dst[pos]+1;
					q.push(next);
				}
			}
		}

		while (!q.empty()) q.pop();

		memset(dst2, -1, sizeof(dst2));
		q.push(1); dst2[1] = 0;
		while (!q.empty()) {
			int pos = q.front(); q.pop();
			REP(i,al[pos].size()) {
				int next = al[pos][i];
				if (dst2[next] < 0) {
					dst2[next] = dst2[pos]+1;
					q.push(next);
				}
			}
		}

		bestdst = dst[1];
		bestdom = 0;
		memset(nt, 0, sizeof(nt));
		memset(inP, 0, sizeof(inP));
		inP[0] = 1;

		search(0, 0, 0);

		fout << "Case #" << tcase+1 << ": " << bestdst-1 << " " << bestdom << endl;
		cout << tcase+1 << " / " << tc << endl;
	}

	fout.close();

	return 0;
}