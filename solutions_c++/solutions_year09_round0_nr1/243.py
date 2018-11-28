/*
 *  Problem A, Google code jam 09
 * Tries
 */

#include <cstdio>
#include <cstring>

///////////////////////////////
// The node structure
struct Node {
	int cnt;
	Node* edge[26];
};

// Op#1; create a Tries
Node* create() {
	Node* ptr = new Node();
	ptr->cnt = 0;
	for(int i=0; i<26; i++)
		ptr->edge[i] = NULL;
	return ptr;
}

// Op#2: add a word into an existing Tries
void addWord(Node* p, char* s, int len, int pos) {
	if(pos>=len) {
		p->cnt++; return;
	}
	if(p->edge[int(s[pos]-'a')]==NULL) p->edge[int(s[pos]-'a')]=create();
	addWord(p->edge[int(s[pos]-'a')], s, len, pos+1);
}

// Op#3: count #of words
int cntWords(Node* p, char* s, int len, int pos) {
	if(pos>=len) return p->cnt;
	
	if(s[pos]!='(') {
		if(!p->edge[int(s[pos]-'a')]) return 0;
		return cntWords(p->edge[int(s[pos]-'a')], s, len, pos+1);
	}
	
	// s[pos]=='('
	int nextPos=pos; while(s[nextPos]!=')') nextPos++;
	int ret = 0;
	while(s[pos++]!=')') {
		if(s[pos]>='a' && s[pos]<='z') { // a letter
			ret+= ( p->edge[int(s[pos]-'a')]==NULL?0:cntWords(p->edge[int(s[pos]-'a')], s, len, nextPos+1) );
		}
	}
	return ret;
}

// Op#4: delete a Tries
void del(Node* pt) {
	if(!pt) return;
	for(int i=0; i<26; i++)
		del(pt->edge[i]);
	delete pt;
}
///////////////////////////

int main (int argc, char * const argv[]) {
	FILE *f = fopen((const char*) argv[1], "r");
	
	int L, D, N; fscanf(f, "%d %d %d", &L, &D, &N);
	Node* pt = create(); 
	char w[17];
	for(int i=0; i<D; i++) {
		fscanf(f, "%s", w);
		addWord(pt, w, strlen(w), 0);
	}
	
	char ww[600];
	for(int i=1; i<=N; i++) {
		fscanf(f, "%s", ww);
		printf("Case #%d: %d\n", i, cntWords(pt, ww, strlen(ww), 0) );
	}
	
	del(pt);
	
    fclose(f); return 0;
}

