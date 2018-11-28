#include<cstdio>
#include<algorithm>
#include<string>
using namespace std;
const int n = 4;
char dat[8][8];
char ans[4][64] = {"X won", "O won", "Draw", "Game has not completed"};
int check(char x) {
	int cnt, cmt;
	for(int i=0;i<n;++i) {
		cnt = cmt = 0;
		for(int j=0;j<n;++j){
			if(dat[i][j] == x) cnt++;
			else if(dat[i][j]=='T') cmt++;
		}
		if(cnt+cmt == 4 && cmt <= 1) return 1;
		cnt = cmt = 0;
		for(int j=0;j<n;++j){
			if(dat[j][i] == x) cnt++;
			else if(dat[j][i]=='T') cmt++;
		}
		if(cnt+cmt == 4 && cmt <= 1) return 1;
	}
	cnt = cmt = 0;
	for(int j=0;j<n;++j){
		if(dat[j][j] == x) cnt++;
		else if(dat[j][j]=='T') cmt++;
	}
	if(cnt+cmt == 4 && cmt <= 1) return 1;
	cnt = cmt = 0;
	for(int j=0;j<n;++j){
		if(dat[n-1-j][j] == x) cnt++;
		else if(dat[n-1-j][j]=='T') cmt++;
	}
	if(cnt+cmt == 4 && cmt <= 1) return 1;
	return 0;
}
int check() {
	if(check('X')) return 0;
	if(check('O')) return 1;
	int cnt = 0;
	for(int i = 0 ; i < n; ++i)
		for(int j = 0; j < n; ++j)
		if(dat[i][j]=='.')
			cnt++;
	if(cnt == 0) return 2;
	return 3;
}
int main() {
	int e = 0, T;
	scanf("%d",&T);
	while(T --) {
		for(int i = 0; i < n; ++i) {
			scanf("%s", dat[i]);
		}
		int res = check();
		printf("Case #%d: %s\n", ++e, ans[res]);
	}
	return 0;
}
