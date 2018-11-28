#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
using namespace std;

const int maxn = 105;

const char * tran[] = { 
	"ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv",
	"ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup"
};

int vis[ 128 ];
char buf[maxn];
char out[maxn];

void init() {
	memset(vis, 0, sizeof(vis));
	int len = strlen(tran[0]);
	for (int i = 0; i < len; i++) {
		vis[tran[0][i]] = tran[1][i];
	}
	vis['q'] = 'z';
	vis['z'] = 'q';
	vis[' '] = ' ';
}

int main( ) {
	init();
	freopen("A-small-attempt3.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cas;
	scanf("%d\n", &cas);
	for (int t = 1; t <= cas; t++) {
		gets(buf);
		int len = strlen(buf);
		for (int i = 0; i < len; i++) {
			out[i] = vis[buf[i]];
		}
		out[len] = 0;
		printf("Case #%d: %s\n", t, out);
	}
	return 0;
}
