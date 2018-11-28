#include <stdio.h>
#include <string.h>
#include <map>
#include <set>
#include <algorithm>
#define mp(a,b) make_pair(a,b)
using namespace std;

map <pair <int, char>, int> mapa;
char palavra [20];
char atual [20000];
set <int> fim;
typedef map<pair <int, char>, int>::iterator iter;

int parse (int no, int pos) {
	if (fim.count(no)) return 1;
	iter temp;
	if (atual[pos] == '(') {
		int ini = ++pos;
		while (atual[pos++] != ')');
		int fim = pos;
		int cont = 0;
		for (int i = ini; i < fim; ++i) {
			temp = mapa.find (mp(no, atual[i]));
			if (temp == mapa.end()) continue;
			cont += parse (temp->second, pos);
		}
		return cont;
	} else {
		temp = mapa.find (mp(no, atual[pos++]));
		if (temp == mapa.end()) return 0;
		else return parse (temp->second, pos);
	}
}

int main () {
	int l, d, n;
	freopen ("A.in","r",stdin);
	freopen ("A.out","w",stdout);
	scanf ("%d%d%d", &l, &d, &n);
	
	int next = 0;
	iter temp;
	int no;
	for (int i = 0; i < d; ++i) {
		scanf ("%s", palavra);
		no = 0;
		for (int p = 0; palavra[p]; ++p) {
			if ((temp = mapa.find(mp(no,palavra[p]))) == mapa.end()) {
				no = mapa[mp(no,palavra[p])] = ++next;
			} else no = temp->second;
		}
		fim.insert (next);
	}
	
	/*for (iter i = mapa.begin(); i != mapa.end(); ++i) {
		printf ("(%d,%c)->%d\n", i->first.first, i->first.second, i->second);	
	}*/
	
	for (int i = 1; i <= n; ++i) {
		scanf ("%s", atual);
		printf ("Case #%d: %d\n", i, parse(0, 0));
	}
	return 0;
}
