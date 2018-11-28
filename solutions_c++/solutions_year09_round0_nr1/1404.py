#include <cstdio>
#include <set>
#include <cstring>
using namespace std;

int N, L, D;
char s[5005][16], com[512];

int solve(char c[]){
	int res, br, open, l;
	res = br = open = 0;
	set<char> st[32];
	l = strlen(c);
	for(int i=0; i<l; ++i){
		if( c[i]=='(' ) { open = 1; continue; }
		if( c[i]==')' ) { open = 0; ++br; continue; }
		if( !open ) st[br++].insert(c[i]);
		else st[br].insert(c[i]);
		}
	for(int i=0; i<D; ++i){
		for(int j=0; j<L; ++j)
			if( st[j].find(s[i][j])==st[j].end() ) goto next;
		++res;
		next:;
		}
	return res;
}

void input(){
	scanf ("%d%d%d",&L,&D,&N);
	for(int i=0; i<D; ++i) scanf ("%s",s[i]);
	for(int i=0; i<N; ++i){
		scanf ("%s",com);
		printf ("Case #%d: %d\n",i+1,solve(com));
		}
}

int main (void) {
	input ();
}
