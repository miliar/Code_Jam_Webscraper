#include <stdio.h>
#include <map>
#include <string>
#include <utility>
#include <vector>
#include <set>
#include <string.h>
using namespace std;

char buf[110];

map<string, int> M;
vector<int> v[200];
set<pair<int, int> > heap;

int V[1010];
int pos[200];

int main() {
	int N;
	gets(buf);
	sscanf(buf, " %d ", &N);
	for (int _42 = 1; _42 <= N; _42++) {
		printf("Case #%d: ", _42);
		int S;
		gets(buf);
		sscanf(buf, " %d ", &S);
		M.clear();
		for (int i = 0; i < S; i++) {
			gets(buf);
			M.insert(make_pair(buf, i));
			v[i].clear();
		}
		gets(buf);
		int Q;
		sscanf(buf, " %d ", &Q);
		for (int i = 0; i < Q; i++) {
			gets(buf);
			V[i] = M[buf];
			v[V[i]].push_back(i);
		}
		for (int i = 0; i < S; i++)
			v[i].push_back(Q+1);
		heap.clear();
		memset(pos, 0, sizeof(pos));
		for (int i =0; i < S; i++)
			heap.insert(make_pair(v[i][0], i));
		int atual = heap.rbegin()->second;
		int vezes = 0;
		for (int i = 0; i < Q; i++) {
			if (V[i] == atual) {
				vezes++;
				atual = heap.rbegin()->second;
			}
			pos[V[i]]++;
			heap.insert(make_pair(v[V[i]][pos[V[i]]], V[i]));
		}
		printf("%d\n", vezes);
	}
	return 0;
}
