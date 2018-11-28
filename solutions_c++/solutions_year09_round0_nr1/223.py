#include <iostream>
#include <cstring>
using namespace std;

const int MAXN = 100000;
const int SIGMA = 27;
int val[300];

struct Node{
	int next[SIGMA];
	int ed, suffix, ch, fa;
	Node(){
		for(int i = 0; i < SIGMA; ++i)
			next[i] = -1;
		ed = suffix = ch = fa = 0;
	}
}trie[MAXN];
int pt;
char buf[MAXN][20];
void init(){
	pt = 1;
	for(int i = 0; i < MAXN; ++i){
		for(int j = 0; j < SIGMA; ++j)
			trie[i].next[j] = -1;
		trie[i].ed = trie[i].suffix = 0;
	}
}

void build_trie(char *buf, int k){
	int i, p, v;
	p = 0;
	for(i = 0; buf[i]; ++i){
		v = val[buf[i]];
		if(trie[p].next[v] == -1){
			trie[pt].fa = p;
			trie[pt].ch = v;
			trie[p].next[v] = pt++;
		}
		p = trie[p].next[v];
	}
	trie[p].ed = k;
}

int LEN;
struct Len{
	int l, r;
}len[30];

int process(char *buf){
	int k = 0, f = 0, i, j;
	for(i = 0; buf[i]; ++i){
		if(buf[i] == '(')f = 1;
		else if(buf[i] == ')')f = 0;
		else {
			if(f){
				for(j = i+1; buf[j] != ')'; ++j);
				len[k].l = i;
				len[k++].r = j-1;
				i = j-1;
			}else {
				len[k].l = len[k++].r = i;
			}
		}
	}
	return k;
}
int cnt;
int vis[6000];
int calc(int pos, int level, char *buf){
	int ret = 0;
	if(level == LEN){
		if(trie[pos].ed == 0)cout<<"wa"<<endl;
		if(vis[trie[pos].ed] != cnt)
			ret = 1;
		else ret = 0;
		vis[trie[pos].ed] = cnt;
		return ret;
	}
	for(int i = len[level].l; i <= len[level].r; ++i){
		if(trie[pos].next[val[buf[i]]] != -1){
	//		cout<<buf[i]<<endl;
			ret += calc(trie[pos].next[val[buf[i]]], level+1, buf);
		}
	}
	return ret;
}
char str[2000];

int main()
{
	int D, N, sum;
	for(char c = 'a'; c <= 'z'; ++c)
		val[c] = c-'a';
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	while(scanf("%d %d %d", &LEN, &D, &N) != EOF){
		init();
		for(int i = 0; i < D; ++i){
			scanf("%s", str);
			build_trie(str, i+1);
		}
		for(int i = 1; i <= N; ++i){
			scanf("%s", str);
			if(process(str) != LEN){
				sum = 0;
			}else {
				cnt = i;
				sum = calc(0, 0, str);
			}
			printf("Case #%d: %d\n", i, sum);
		}
	}
	return 0;
}
