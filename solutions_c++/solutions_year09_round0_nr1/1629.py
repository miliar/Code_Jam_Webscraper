#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <map>
using namespace std;

class Trie{
public:
	int num;
	Trie *next[27];

	Trie(){
		num = 0;
		for(int i = 0; i < 27; i++)
			next[i] = NULL;
	}
	
	static Trie *insert(Trie *t, char *s, int p){
		if( t == NULL){
			t = new Trie();
		}
		if( s[p] != '\0'){
			t->next[s[p]] = insert(t->next[s[p]], s, p + 1);
		}else{
			t->num++;
		}
		return t;
	}
};

int L, D, N;
char sss[1024][20];
string ss[1024];
char s1[1024];
char s[1024];
Trie *root;
int am;
map<string, int> hash;

void normalize(char *s){
	int len = strlen(s);
	for(int i = 0; i < len; i++)
		s[i] = s[i] - 'a' + 1;
}

void go(Trie *t, char *s, int p, int p1){
	s1[p1] = '\0';
	string temp = s1;
	if( hash.count(temp) != 0){
		return;
	}
	if( p1 == L){
		hash[temp] = 1;
	}else{
		if( s[p] >= 'a' && s[p] <= 'z'){
			s1[p1] = s[p] - 'a' + 1;
			s1[p1 + 1] = '\0';
			temp = s1;
			if( t->next[s1[p1]] == NULL){
				return;
			}
			else{
				go(t->next[s1[p1]], s, p + 1, p1 + 1);
			}
			hash[temp] = 1;
		}else{
			int close= p + 1;
			while( s[close] != ')')
				close++;
			for(int i = p + 1; i < close; i++){
				s1[p1] = s[i] - 'a' + 1;
				s1[p1 + 1] = '\0';
				temp = s1;
				if( t->next[s1[p1]] != NULL){
					go(t->next[s1[p1]], s, close + 1, p1 + 1);
					
				}
				hash[temp] = 1;
			}
		}
	}
}

int main () {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	char temp[1024];
	
	root = new Trie();
	gets(temp);
	sscanf(temp, "%d %d %d", &L, &D, &N);
	for(int i = 0; i < D; i++){
		gets(sss[i]);
		normalize(sss[i]);
		ss[i] = sss[i];
		Trie::insert(root, sss[i], 0);
	}
	for(int i = 1; i <= N; i++){
		gets(s);
		hash.clear();
		go(root, s, 0, 0);
		int am = 0;
		for(int j = 0; j < D; j++)
			if( hash.count(ss[j]) != 0)
				am += hash[ss[j]];
		printf("Case #%d: %d\n",i, am);
	}
	return 0;
}

