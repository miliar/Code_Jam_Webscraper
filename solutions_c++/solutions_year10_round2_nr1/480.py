#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#define h 100000
#define u 111

using namespace std;

int T,N,M,i,t,size,ans;
vector< pair<string, int> > a[h];
char s[u];

int find(int pos, string& s) {
	for(int i=0;i<a[pos].size();i++)
		if(a[pos][i].first == s)
			return a[pos][i].second;
	return -1;
}

void build(char* s) {
	int i,j,pos,next;
	string cur = "";
	pos = 0;
	for(i=1;s[i];i++)
		if(s[i] == '/') {
			next = find(pos, cur);
			if(next == -1) {
				next = size++;
				a[pos].push_back(make_pair(cur, next));
			}
			pos = next;
			cur = "";
		} else
		cur += s[i];
		next = find(pos, cur);
		if(next == -1) {
			next = size++;
			a[pos].push_back(make_pair(cur, next));
		}
}

void add(char* s) {
	int i,j,pos,next;
	string cur = "";
	pos = 0;
	for(i=1;s[i];i++)
		if(s[i] == '/') {
			next = find(pos, cur);
			if(next == -1) {
				next = size++;
				ans++;
				a[pos].push_back(make_pair(cur, next));
			}
			pos = next;
			cur = "";
		} else
		cur += s[i];
		next = find(pos, cur);
		if(next == -1) {
			next = size++;
			ans++;
			a[pos].push_back(make_pair(cur, next));
		}
}

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for(t=1;t<=T;t++) {
		for(i=0;i<h;i++)
			a[i].clear();
		size = 1;
		ans = 0;
		scanf("%d%d%*c", &N, &M);
		for(i=0;i<N;i++) {
			gets(s);
			build(&s[0]);
		}
		for(i=0;i<M;i++) {
			gets(s);
			add(&s[0]);
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}