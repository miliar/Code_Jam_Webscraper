#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
#include <cstring>

using namespace std;

#define MAX 101

int ma[MAX][MAX];
int names[MAX][MAX],h,w;
char letra;
int dir[4][2]={
	{-1,0},
	{0,-1},
	{0, 1},
	{1, 0}
};

char procesa(int f, int c) {
	int ff,cc,min=ma[f][c],dirmin=-1;
	
	if (names[f][c]==0) {
	
		for (int i=0; i<4; i++){
			ff=f + dir[i][0];
			cc=c + dir[i][1];
			if (ff>=0 && cc>=0 && ff<h && cc<w){
				if (ma[ ff ][ cc ]<min){
					min=ma[ff][cc];
					dirmin=i;
				}
			}
		}
		if (dirmin!=-1){
			names[f][c] = procesa( f + dir[ dirmin ][0], c + dir[ dirmin ][1] );
		}else{
			names[f][c] = letra++;
		}
	}
	return names[f][c];

}
int main() {
	int t;
	scanf("%d", &t);
	for (int k=1; k<=t; k++) {
		scanf("%d %d",&h, &w);
		for (int j=0; j<h; j++) {
			for (int k=0; k<w; k++) {
				scanf("%d",&ma[j][k]);	
			}
		}
		letra='a';
		memset(names, 0, sizeof(names));
		
		for (int i=0, j; i<h; i++) {
			for (j=0; j<w; j++){
				if (names[i][j]==0) {
					procesa( i,j );
				
				}
			}
		}
		
		printf("Case #%d:\n",k);
		for (int i=0, j; i<h; i++) {
			for (j=0; j<w; j++){
				printf("%c%c",names[i][j],j<w-1?' ':'\n');
			}
		}
	}
	return 0;
}

