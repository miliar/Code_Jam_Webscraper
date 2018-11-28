#include <cstdio>
#include <vector>
#include <map>
#include <functional>
#include <algorithm>
#define MAX 1005

using namespace std;

int k, n;
vector< pair<char, char> > op;
map< pair<char, char>, char > mp;
vector<char> sol(MAX);

void add(char c) {
	int i, j;

	if (k) {
		if (mp.find( make_pair( sol[k-1], c ) ) != mp.end())
			sol[k-1] = mp[ make_pair(sol[k-1], c)];
		else {
			for (i=0; i<op.size(); i++)
				if (op[i].first == c)
					for (j=0; j<k; j++)
						if (sol[j] == op[i].second) { k = 0; return; }
			sol[k++] = c;
		}
	} else sol[k++] = c;
}

int main() {
	int t, z, c, d;
	int i;
	char tmp[5], S[MAX];

	scanf("%d", &t);
	for (z=1; z<=t; z++) {
		scanf("%d ", &c);
		mp.clear();
		op.clear();

		for (i=1; i<=c; i++) {
			scanf("%s", tmp);
			mp[ make_pair(tmp[0], tmp[1]) ] = tmp[2];
			mp[ make_pair(tmp[1], tmp[0]) ] = tmp[2];
		}
		scanf("%d", &d);
		for (i=1; i<=d; i++) {
			scanf("%s", tmp);
			op.push_back( make_pair(tmp[0], tmp[1]) );
			op.push_back( make_pair(tmp[1], tmp[0]) );
		}

		scanf("%d %s", &n, S);
		
		k = 0;
		for (i=0; i<n; i++)
			add(S[i]);

		printf("Case #%d: [", z);
		if (k) printf("%c", sol[0]);
		for (i=1; i<k; i++) printf(", %c", sol[i]);
		printf("]\n");

	}
	return 0;
}

