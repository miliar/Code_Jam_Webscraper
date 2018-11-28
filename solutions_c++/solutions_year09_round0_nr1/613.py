#include <cstdio>
#include <vector>

using namespace std;

int l, d, n, i, j, nrnod, nr;
int tr[100000][27];
bool sf[100000];
char cuv[3000];
vector <int> q[30];
long long nsol;

void baga_trie(char cuv[]) {
	int nod = 0, i, poz;

	for (i = 0; cuv[i] != 0; i++) {
		poz = cuv[i] - 'a';
		if (tr[nod][poz] == 0) {
			nrnod++;
			tr[nod][poz] = nrnod;
			nod = nrnod;
		}
		else
			nod = tr[nod][poz];
	}
	
	sf[nod] = 1;
}


void back(int k, int nod) {
	int i, j, t;
	if (k == l)
		nsol += sf[nod];
	else {
		for (i = 0; i < q[k + 1].size(); i++) {
			t = q[k + 1][i];
			if (tr[nod][t] != 0) 
				back(k + 1, tr[nod][t]);
		}
	}
}


int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);

	scanf("%d%d%d", &l, &d, &n);

	for (i = 1; i <= d; i++) {
		scanf(" %s ", cuv);
		baga_trie(cuv);
	}

	for (i = 1; i <= n; i++) {
		for (j = 1; j <= l; j++)
			q[j].clear();

		scanf(" %s ", cuv);
		nr = 0;

		bool inp = 0;

		for (j = 0; cuv[j] != 0; j++) {
			if (cuv[j] == '(') {
				nr++;
				inp = 1;
			}
			if (cuv[j] == ')')
				inp = 0;

			if (cuv[j] != ')' && cuv[j] != '(') {
				if (inp == 0) 
					nr++;
				q[nr].push_back(cuv[j] - 'a');
			}
		}

		nsol = 0;
		back(0, 0);
		printf("Case #%d: %lld\n", i, nsol);
	}

	return 0;
}
