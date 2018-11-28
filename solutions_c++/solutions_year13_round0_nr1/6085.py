#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<cmath>
#include<climits>
#include<algorithm>
#include<map>
using namespace std;

char mp[10][10];

int getmax(int x, int y) { return x>y?x:y; }

int row(int id) {
	char ch=mp[id][0];
	if (ch=='T') ch=mp[id][1]; if (ch=='.') return 0;
	for (int i=0; i<4; ++i) if (mp[id][i]!='T' && mp[id][i]!=ch) return 0;
	if (ch=='X') return 2; return 1;
}

int col(int id) {
	char ch=mp[0][id];
	if (ch=='T') ch=mp[1][id]; if (ch=='.') return 0;
	for (int i=0; i<4; ++i) if (mp[i][id]!='T' && mp[i][id]!=ch) return 0;
	if (ch=='X') return 2; return 1;
}

int dia() {
	char ch=mp[0][0];
	if (ch=='T') ch=mp[1][1]; if (ch=='.') return 0;
	for (int i=0; i<4; ++i) if (mp[i][i]!='T' && mp[i][i]!=ch) return 0;
	if (ch=='X') return 2; return 1;
}

int adia() {
	char ch=mp[0][3];
	if (ch=='T') ch=mp[1][2]; if (ch=='.') return 0;
	for (int i=0; i<4; ++i) if (mp[i][3-i]!='T' && mp[i][3-i]!=ch) return 0;
	if (ch=='x') return 2; return 1;
}

void conduct() {
	int i, j, ed, win;
	for (i=0; i<4; ++i) scanf("%s", mp[i]);
	for (ed=i=0; i<4; ++i) for (j=0; j<4; ++j) if (mp[i][j]=='.') ed=1;
	for (win=i=0; i<4; ++i) win=getmax(win, row(i));
	for (i=0; i<4; ++i) win=getmax(win, col(i));
	win=getmax(win, dia());
	win=getmax(win, adia());
	if (win==2) { printf("X won\n"); return; }
	if (win==1) { printf("O won\n"); return; }
	if (ed==1) { printf("Game has not completed\n"); return; }
	printf("Draw\n");
}

int main() {
	int time; scanf("%d", &time);
	for (int i=1; i<=time; ++i) {
		printf("Case #%d: ", i);
		conduct();
	}
	return 0;
}
