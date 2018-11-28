#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define	MAXN	110

map <string, char> nonbase;
map <string, int> opposed;

vector<char> v;
char in[MAXN];
int c, d, n;

int Compoe() {
	char aux[3];
		
	if(v.size() <= 1)
		return 0;

	aux[0] = v[v.size()-2];
	aux[1] = v[v.size()-1];
	aux[2] = 0;
	if(nonbase.find(string(aux)) != nonbase.end()) {
		v.erase(v.begin() + v.size()-1);
		v.erase(v.begin() + v.size()-1);
		v.push_back(nonbase[string(aux)]);
		return 1;
	}
	return 0;
}

int Opostos() {
	char aux[3];
	int i, j;

	if(v.size() <= 1)
		return 0;

	aux[2] = 0;
	aux[0] = v[v.size()-1];
	for(i=0; i < v.size()-1; i++) {
		aux[1] = v[i];
		if(opposed.find(string(aux)) != opposed.end()) {
//			for(j=v.size()-1; j >= i; j--)
//				v.erase(v.begin() + j);
			v.clear();
			return 1;
		}
	}

	return 0;
}

void Resolve() {
	int i, j, k;

	v.push_back(in[0]);
	for(i=1; i < n; i++) {
		v.push_back(in[i]);
		while(Compoe() || Opostos())
			;
	}

	return ;
}

int main (void) {
	int i, j, k, t;

	char aux1[5];
	char aux2[5];

	scanf("%d", &t);
	for(k=1; k <= t; k++) {
		nonbase.clear();
		opposed.clear();
		v.clear();
		scanf("%d", &c);
		for(i=0; i < c; i++) {	
			scanf(" %s", aux1);
			aux2[0] = aux1[0]; aux2[1] = aux1[1]; aux2[2] = 0;
			nonbase[string(aux2)] = aux1[2];
			aux2[0] = aux1[1]; aux2[1] = aux1[0]; aux2[2] = 0;
			nonbase[string(aux2)] = aux1[2];
		}
		scanf("%d", &d);
		for(i=0; i < d; i++) {
			scanf(" %s", aux1);
			aux2[0] = aux1[0]; aux2[1] = aux1[1]; aux2[2] = 0;
			opposed[string(aux2)] = 1;
			aux2[0] = aux1[1]; aux2[1] = aux1[0]; aux2[2] = 0;
			opposed[string(aux2)] = 1;
		}
		scanf("%d %s", &n, in);
		Resolve();
		printf("Case #%d: [", k);
		if(v.size() == 0)
			printf("]\n");
		else {
			for(i=0; i < v.size() -1; i++)
				printf("%c, ", v[i]);
			printf("%c]\n", v[i]);
		}
	}

	return 0;
}
