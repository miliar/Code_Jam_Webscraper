#include <iostream>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

typedef vector<int> vi; 
typedef vector<string> vs;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define rep(i, n) for(int i = 0; i < n; ++i) 
#define foreach(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it) 
#define INT_INF 0x3F3F3F3F
// BEGIN CUT HERE
#define TRACE(x...) x
#define watch(x) TRACE(cout << #x" = " << x << endl)

string itos(int x) { stringstream ss; ss << x; return ss.str(); }
vector<string> split(string s) { vector<string> r; string t; stringstream ss(s); while(ss >> t) r.push_back(t); return r; }
// END CUT HERE

double prob[100000];
char feat[100000][20];
int children[100000][2];

char c;
int curr;

char animal[30];
char anfeats[110][30];
int numfeats;

char clean() {
	c = '\n';
	while (c == '\n' || c == ' ' || c == '\t') scanf("%c", &c);
	return c;
}

int build() {
	int node = ++curr;
	
	double aux;
	scanf("%lf", &aux);
	prob[node] = aux;

	clean();

	int counter = 0;
	if (c != ')') {
		feat[node][counter++] = c;

		while (1) {
			scanf("%c", &c);
			if (c == '\n' || c == ' ' || c == '\t') break;
			feat[node][counter++] = c;
		}
		
		clean();
		children[node][0] = build();
		clean();
		children[node][1] = build();

		clean();
	}
	feat[node][counter] = '\0';
	
	return node;
}

double check(int node) {
	if (children[node][0] == -1) return prob[node];

	bool hasfeat = false;
	rep(i, numfeats) {
		if (strcmp(anfeats[i], feat[node]) == 0) {
			hasfeat = true;
			break;
		}
	}

	if (hasfeat) return prob[node] * check(children[node][0]);
	else return prob[node] * check(children[node][1]);
}

int main() {
	int N, L;
	scanf("%d", &N);

	rep(n,N) {
		scanf("%d", &L);
		memset(children, -1, sizeof(children));
		curr = -1;
		
		clean();
		build();

		printf("Case #%d:\n", n+1);

		int A;
		scanf("%d", &A);
		rep(i, A) {
			scanf("%s", animal);

			scanf("%d", &numfeats);
			rep(j, numfeats) {
				scanf("%s", anfeats[j]);
			}

			printf("%.10lf\n", check(0));
		}
		
	}
}

