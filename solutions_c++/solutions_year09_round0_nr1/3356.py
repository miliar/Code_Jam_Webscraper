#include <iostream>
#include <cstdlib>
#include <cstdio>
#define FOR(i,a,b) for((i)=(a);(i)<(b);++(i))
using namespace std;

int N,L,D;
char words[5000][16];
char query[1024];

bool coresponds(int k) {
	int i,nr = 0,l = strlen(query);
	bool found;
	
	FOR(i,0,l) {
		if (query[i] == '(') { found = false;
			while ((query[i] != ')') && (i < l)) {
				if (query[i] == words[k][nr]) found = true;++i;}
			if (!found) return false;
		} else { if (query[i] != words[k][nr]) return false;}
		nr++;
	}
	
	return true;
}

int main() {

	FILE *fin,*fout;
	
	fin = fopen("A-small-attempt0.in","r");
	fout = fopen("A-small-attempt0.out","w");
	
	int i,t,res;
	
	fscanf(fin,"%d%d%d\n",&L,&D,&N);
	
	for (i=0;i<D;++i) fgets(words[i],sizeof(words[i]),fin);
	
	for (t=1;t<=N;++t) {	
		printf("%d\n",t);
		res = 0;
		memset(query,0,sizeof(query));
		fgets(query,sizeof(query),fin);
		for (i=0;i<D;++i) if (coresponds(i)) res++;
		fprintf(fout,"Case #%d: %d\n",t,res);
	}
	
	fclose(fin);
	fclose(fout);

	return 0;
}