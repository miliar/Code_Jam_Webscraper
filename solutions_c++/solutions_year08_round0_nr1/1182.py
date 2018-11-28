#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <iostream>
#include <map>

#define MAX 128
#define INFINITO 99999

using namespace std;

map<string, int> m;
map<string, int>::iterator it;

vector<int> query;

char foi[MAX];

int main (void) {

	int casos;
	int s, q;
	char line[MAX];
	int id, ult;
	int caras, trocas;
	int i, j, k;

	scanf("%d", &casos);

	for (k=0; k<casos; ++k) {

		scanf("%d ", &s);

		id=0;
		m.clear();
		query.clear();

		for (i=0; i<s; ++i) {
			fgets(line, MAX, stdin);
			line[strlen(line)-1]=0;
			m[line] = id++;

		}

		scanf("%d ", &q);

		string s1;
		for (i=0; i<q; ++i) {
			fgets(line, MAX, stdin);
			line[strlen(line)-1]=0;
			s1 = line;
			
			it = m.find(s1);
			query.push_back(it->second);
		}


		trocas=0;
		if (q) {
			ult = query[0];
			for (i=0; i<q; ++trocas) {

				for (j=0; j<s; ++j)
					foi[j]=0;

				foi[ult]=1;
				caras=1;
				for (; i<q && caras<s; ++i) {
					if (!foi[ query[i] ]) {
						++caras;
						foi[ query[i] ] = 1;
						ult = query[i];
					}
				}
			}
			for (i=0; i<s; ++i)
				if (!foi[i]) {
					--trocas;
					break;
				}
		}
		printf("Case #%d: %d\n", k+1, trocas);
	}

	return 0;
}
