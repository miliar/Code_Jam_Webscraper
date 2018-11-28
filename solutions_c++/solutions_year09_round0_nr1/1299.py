#include <cstdio>
#include <cstdlib>
#include <map>

using namespace std;

class Node{
public:
	int end;
	Node *next[26];

	Node *go(char x, bool create){
		if (next[x] == NULL && create) next[x] = (Node *)malloc(sizeof(Node));
		return next[x];
	}
	void endWord(){
		++end;
	}
	int howManyEndings(){
		return end;
	}
	Node () {
		for (int i = 0; i < 26; ++i) next[i] = NULL;
		end = 0;
	}

};

int L, D, N;
Node root;

void load(){
	scanf("%d%d%d", &L, &D, &N);
	char t[20];
	Node *x;

	for (int i = 0; i < D; ++i){
		scanf("%s", t);
		x = &root;
		for (int k = 0; k < L; ++k){
			x = x->go(t[k]-'a', true);
		}
		x->endWord();
	}
}

int main(){
	char t[1000];

	load();
	map <Node *, long long> q[2];

	for (int tt = 1; tt <= N; ++tt){
		scanf("%s", t);

		int qi = 0;
		int u_zagradi = 0;
		q[qi].clear(); q[!qi].clear();
		q[qi][&root] = 1;

		for (int i = 0; t[i]; ++i){
			if (t[i] == '(') { u_zagradi = 1; continue; }
			if (t[i] == ')') { u_zagradi = 0; q[qi].clear(); qi = !qi; continue; }

			for (map<Node *, long long>::iterator itr = q[qi].begin(); itr != q[qi].end(); ++itr){
				if (itr->first->go(t[i]-'a', false) == NULL) continue;
				long long ax = q[!qi][itr->first->go(t[i]-'a', false)];
				q[!qi][itr->first->go(t[i]-'a', false)] = ax+1;;
			}
			if (u_zagradi == 0) { q[qi].clear(); qi = !qi; continue; }
		}
		long long count = 0;
		for (map<Node *, long long>::iterator itr = q[qi].begin(); itr != q[qi].end(); ++itr){
			count += itr->second * (itr->first->howManyEndings());
		}
		printf("Case #%d: %lld\n", tt, count);
	}


	return 0;
}
