#include <cmath>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <climits>
#include <ctime>
using namespace std;

#define NIL INT_MAX/2
#define inf 1e20
#define eps 1e-10

#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,a,b) for(int i=a; i<(b); ++i)
#define clr(x) memset(x,0,sizeof(x)) 

const int MAXN = 200000;

string s[20];
int ans;
int L, D, N;

class Trie
{
public:
	Trie() {
		memset(Child, 0, sizeof(Child));
		memset(Key, 0, sizeof(Key));
		root = 0, Size = 0;
	}

	void Insert(char *name, int key) {
		Insert(name, key, root, root);
	}

	void Search() {
		Search(root, 0);
	}

private:
	int Child[MAXN][26], Key[MAXN][26];
	int root, Size;

	inline int id(char c) {
		return c - 'a';
	}

	void Insert(char *name, int key, int &root, int &f) {
		int k = id(name[0]);
		if(name[0] == '\0')Key[f][id(name[-1])] = key;
		else if(!root) {
			Size++, root = Size;
			Insert(name+1, key, Child[root][k], root);
		}
		else Insert(name+1, key, Child[root][k], root);
	}

	void Search(int &root, int cnt) {
		if(cnt == L)return;
		for(int i = 0; i < s[cnt].size(); i++) {
			int k = id(s[cnt][i]);
			if(!Child[root][k]) {
				if(Key[root][k])ans++;
				continue;
			}
			Search(Child[root][k], cnt + 1);
		}
	}
};

Trie GCJA;

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	scanf("%d %d %d", &L, &D, &N);
	char inp[1000];

	while(D--) {
		scanf("%s", inp);
		GCJA.Insert(inp, 1);
	}

	int cases = 1;
	while(N--) {
		printf("Case #%d: ", cases++);
		ans = 0;
		scanf("%s", inp);
		int len = strlen(inp);
		for(int i = 0, j = 0; i < len; i++) {
			if(inp[i] == '(') {
				s[j] = "";
				for(int k = i + 1; k < len; k++) {
					if(inp[k] == ')') {
						j++;
						i = k;
						break;
					}
					else s[j] += inp[k];
				}
			}
			else {
				s[j] = "";
				s[j] += inp[i];
				j++;
			}
		}
		GCJA.Search();
		printf("%d\n", ans);
	}

	return 0;
}

/*Powered By Lynn-Beta1*/