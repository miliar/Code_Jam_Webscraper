#include <cstdio>
#include <string>
#include <queue>
#include <map>
using namespace std;

int s, q, Q[1005], tab[105][1005], d[1005];
map<string, int> S;
bool was[1005];

string readstring() {
	int k = 0;
	char t[105];
	do scanf("%c", &t[k++]);
	while(t[k - 1] != '\n');
	t[k - 1] = (char)NULL;
	return t;
}

int BFS(int x) {
	queue<int> V;
	for(int i=0; i<=q; ++i) was[i] = false;
	was[x] = true, d[x] = 0, V.push(x);
	while(true) {
		int u = V.front();
		if(u == q) break;
		for(int i=0; i<s; ++i) {
			int j = u + tab[i][u];
			if(was[j]) continue;
			was[j] = true, d[j] = d[u] + 1, V.push(j);
		}
		V.pop();
	}
	return d[q];
}

int main() {
	int N;
	scanf("%d", &N);
	for(int z=1; z<=N; ++z) {
		scanf("%d%*c", &s);
		for(int i=0; i<s; ++i) S[readstring()] = i;
		//for(map<string, int>::iterator i=S.begin(); i!=S.end(); ++i)
		//	printf("%s (%d)\n", i->first.c_str(), i->second);
		scanf("%d%*c", &q);
		for(int i=0; i<q; ++i) Q[i] = S[readstring()];
		//for(int i=0; i<q; ++i) printf("* %d\n", Q[i]);
		S.clear();
		for(int i=0; i<s; ++i) {
			int counter = 0;
			for(int j=q-1; j>=0; --j)
				if(Q[j] != i) tab[i][j] = ++counter;
				else tab[i][j] = counter = 0;
		}
		/*for(int i=0; i<s; ++i) {
			for(int j=0; j<q; ++j)
				printf("%d ", tab[i][j]);
			printf("\n");
		}*/
		printf("Case #%d: %d\n", z, max(BFS(0) - 1, 0));
	}
	return 0;
}
