#include <iostream>
using namespace std;
int L, D, N, res;
char s[300], cnt[300], ch[300][300];
struct Node{
	Node *next[26];
	bool visited;
	Node(){memset(next, NULL, sizeof(next));visited = false;}
}*root;

void insert(char *s){
	int i = 0, index;
	Node *p = root;
	while(s[i]){
		index = s[i++] - 'a';
		if(!p->next[index]) p->next[index] = new Node();
		p = p->next[index];
	}
	return;
}

void solve(int pos, Node *p){
	if(pos == L){
//		if(!p->visited) ++res;
		++res;
		p->visited = true;
		return;
	}
	int pp;
	for(pp = 0; pp < cnt[pos]; ++pp){
	
		if(p->next[ch[pos][pp] - 'a']) solve(pos + 1, p->next[ch[pos][pp] - 'a']);
	}
	return;
}
int main(){
	freopen("D:\\A-small-attempt10.in", "r", stdin);
	freopen("D:\\out.out", "w", stdout);
	scanf("%d%d%d", &L, &D, &N);
	root = new Node();
	for(int i = 0; i < D; ++i){
		scanf("%s", s);
		insert(s);
	}
	for(int i = 1; i <= N; ++i){
		res = 0;
		int pos = 0, index = 0, l;
		bool flag = false;
		scanf("%s", s);
		l = strlen(s);
		for(int j = 0; j < l; ++j){
			if(s[j] == '('){
				flag = true;index = j;
				continue;
			}
			if(s[j] == ')'){
				flag = false;cnt[pos] = 0;
				for(int k = index + 1; k < j; ++k)
					if(s[k] >= 'a' && s[k] <= 'z')  ch[pos][cnt[pos]++] = s[k];
				++pos;
			}
			else if(!flag){
				cnt[pos] = 0;
				ch[pos][cnt[pos]++] = s[j];
				++pos;
			}
		}
		solve(0, root);
		printf("Case #%d: %d\n", i, res);
//		fprintf(stderr, "Case #%d: %d\n", i, res);

	}
	return 0;
}