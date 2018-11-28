#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <strstream>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <string.h>

using namespace std;

#define VAR(i,v) __typeof((v))i=(v)
#define FOREACH(i,v) for(VAR(i,(v).begin());i!=(v).end();i++)

class leaf {
	public:
	leaf* n[256];

	leaf() { memset(n, 256, 0); }
};

leaf root;

void add_dict(char* w) {
	leaf *act = &root;
	for (int i=0; w[i]!=0; i++) {
		char c = w[i];
		if (act->n[c]==NULL) 
			act->n[c] = new leaf();
		act = act->n[c];	
	}
}

vector< list<char> > pat;
int pat_len;
int cnt(int size, int l=0, leaf* act=NULL) {
	int c=0;
	if (l==0) {
		pat_len = pat.size();
		act = &root;
	}

	if (l==size) return 1;

	FOREACH(i,pat[l]) {
		if (act->n[*i]!=NULL) 
			c += cnt(size, l+1, act->n[*i]);
	}
	
	return c;
}

void mkpat(int s, char* b) {
	list<char> l;
	pat.resize(0,l);
	pat.resize(s,l);

	int p=0, n=0;
	bool in=false;

	while (b[p]!=0) {
		char c = b[p];
		
		if (!in && c=='(') {
			in = true;
		} else if (c==')') {
			in = false;
		} else {
			pat[n].push_back(c);
		}
		
		if (!in) n++;
		p++;
	}
}

int main(int argc, char* argv[]) {

	if (argc<2) {
		printf("podaj nazwe pliku\n");
		exit(1);
	}

	char buf[2048];
	ifstream fin(argv[1]);
	istrstream nStr(buf, 2048);
	int N=0,L=0,D=0;

	fin.getline(buf, 2048);

	nStr >> L >> D >> N;

	for (int d=0; d<D; d++) {
		fin.getline(buf,2048);
		add_dict(buf);
	}


	for (int n=1; n<=N; n++) {
		fin.getline(buf,2048);
		mkpat(L,buf);
		printf("Case #%d: %d\n", n, cnt(L));
	}

	return 0;
}

