#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

int t;
char grid[5][5];

main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &t);
    for(int test=1; test<=t; test++) {
	for(int i=0;i<4;i++) scanf("%s", grid[i]);
	bool xwin=false, owin=false, full=true;
	for(int i=0;i<4;i++) {
	    bool okx=true, oko=true;
	    for(int j=0;j<4;j++) okx &= grid[i][j]=='X' || grid[i][j]=='T';
	    for(int j=0;j<4;j++) oko &= grid[i][j]=='O' || grid[i][j]=='T';
	    xwin |= okx; owin |= oko;
	    okx=true, oko=true;
	    for(int j=0;j<4;j++) okx &= grid[j][i]=='X' || grid[j][i]=='T';
	    for(int j=0;j<4;j++) oko &= grid[j][i]=='O' || grid[j][i]=='T';
	    xwin |= okx; owin |= oko;
	    }
	bool okx=true, oko=true;
	for(int i=0;i<4;i++) okx &= grid[i][i]=='X' || grid[i][i]=='T';
	for(int i=0;i<4;i++) oko &= grid[i][i]=='O' || grid[i][i]=='T';
	xwin |= okx; owin |= oko;
	okx=true, oko=true;
	for(int i=0;i<4;i++) okx &= grid[i][3-i]=='X' || grid[i][3-i]=='T';
	for(int i=0;i<4;i++) oko &= grid[i][3-i]=='O' || grid[i][3-i]=='T';
	xwin |= okx; owin |= oko;
	for(int i=0;i<4;i++) for(int j=0;j<4;j++) full &= grid[i][j]!='.';
	
	printf("Case #%d: ", test);
	if(xwin) printf("X won\n");
	else if(owin) printf("O won\n");
	else if(full) printf("Draw\n");
	else printf("Game has not completed\n");
	}
    }









