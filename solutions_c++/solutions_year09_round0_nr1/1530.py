#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

struct trie {
	bool terminal;
	trie *children[26];
	
	trie(): terminal(false) {
		memset(children, 0, sizeof(children));
	}
	
	void add(char *str) {
		if(!*str) {
			terminal = true;
			return;
		} else {
			if(! children[*str-'a'])
				children[*str-'a'] = new trie();
			children[*str-'a']->add(str + 1);
		}
	}
	
	int count(char *str) {
		if(*str == '(') {
			char *str2 = ++str;
			
			while(*str2 != ')') str2++;
			
			sort(str, str2);
			
			*(str2++) = '\0';
			
			int total = 0;
			for( ; *str; str++) {
				if(*str == *(str-1)) continue;
				if(children[*str-'a'])
					total += children[*str-'a']->count(str2);
			}
			
			*(str2-1) = ')';
			
			return total;
		} else if ('a' <= *str && *str <= 'z') {
			if(!children[*str-'a']) return 0;
			return children[*str-'a']->count(str+1);
		} else {
			return terminal;
		}
	}
};

int main() {
	int L, D, N, nCase = 1;
	char line[1000000];
	
	scanf("%d %d %d\n", &L, &D, &N);
	
	trie *root = new trie();
	
	while(D--) {
		scanf("%s\n", line);
		root->add(line);
	}
	
	while(N--) {
		scanf("%s\n", line);
		printf("Case #%d: %d\n", nCase++, root->count(line));
	}
	
	return 0;
}
