#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

void solve();
void runCase();

#define rep(i,n) for(int i = 0; i < (n); i++)

char s[4][5],t[4][5];

bool check_win(char c) {
	int n = 4;
	rep(i,n) rep(j,n) t[i][j] = s[i][j];
	rep(i,n) rep(j,n) if(t[i][j]=='T') t[i][j] = c;
	
	bool win = true;
	rep(i,n) {
		win = true;
		rep(j,n) if(t[i][j]!=c) win = false;
		if(win) return win;
	}
	rep(i,n) {
		win = true;
		rep(j,n) if(t[j][i]!=c) win = false;
		if(win) return win;
	}
	win = true;
	rep(i,n) if(t[i][i]!=c) win = false;
	if(win) return win;
	
	win = true;
	rep(i,n) if(t[i][n-1-i]!=c) win = false;
	if(win) return win;
	
	return false;
}

void runCase()
{
	int n = 4;
	rep(i,n) {
		scanf("%s",s[i]);
	}
	if(check_win('X')) {
		printf("X won\n");
	}
	else if(check_win('O')) {
		printf("O won\n");
	} else {
		bool draw = true;
		rep(i,n) rep(j,n) if(s[i][j]=='.') draw = false;
		if(draw) {
			printf("Draw\n");
		} else {
			printf("Game has not completed\n");
		}
	}
	
}

void runSample()
{
	string input;

	char buf[501] = {0};
	cin.getline(buf,501);

	input = buf;


	printf("%s\n",input.c_str());
}

void solve()
{
	int n;
	scanf("%d",&n);
	getchar();

	for(int i = 0; i < n; i++) {
		printf("Case #%d: ",i+1);
		runCase();
		//runSample();
	}
}

int main()
{
	solve();
	return 0;
}
