#include <cstdio>
#include <vector>
#include <string.h>
#include <map>
#include <string>
using namespace std;

struct r{
	string s;
	vector<r> child;
	r(){}
	r(string s):s(s){}
};
int sc, ans;
char s[110];
int a[30000];
r root;

void pass(bool co){
	char t[110]; 
	int len = strlen(s);
	s[len++] = '/';
	int tar = 1;
	r *no = &root;
	for (int i=1; i<len; i++)
		if (s[i] == '/'){
			memset(t, 0, sizeof(t));
			strncpy(t, s+tar, i-tar);
//			printf("'%s'\n", t);
			int size = no->child.size();
			string st = string(t);
			bool find = false;
			for (int j=0; j<size && !find; j++)
				if (no->child[j].s == st){
					find = true;
					no = &(no->child[j]);
				}
			if (!find){
				no->child.push_back(r(st));
				no = &(no->child[size]);
				if (co)
					ans++;
			}
			tar = i+1;
		}
//	printf("====\n");
}

int main(){
	int T, ca = 0;
	scanf("%d", &T);
	gets(s);
	while (T--){
		int n, m;
		sc = 1;
		ans = 0;
		memset(a, -1, sizeof(a));
		root = r();
		scanf("%d%d", &n, &m);
		gets(s);
		for (int i=0; i<n; i++){
			scanf("%s", s);
			pass(false);
		}
		for (int i=0; i<m; i++){
			scanf("%s", s);
			pass(true);
		}
		printf("Case #%d: %d\n", ++ca, ans);
	}
	return 0;
}
