
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef long long LL;
typedef unsigned long long ULL;

int H,W;
int map[100][100];
char basin[100][100];
char bas;

int ofs[4][2]={
	{0,-1},{-1,0},{1,0},{0,1}
};

char trvs(int h, int w) {
	int amn = map[h][w];
	int nr = 0;
	if( h > 0 ){
		if( map[h-1][w] < amn){
			amn = map[h-1][w];
			nr=2;
		}
	}
	if( w > 0 ){
		if( map[h][w-1] < amn){
			amn = map[h][w-1];
			nr=1;
		}
	}
	if( w+1 < W ){
		if( map[h][w+1] < amn){
			amn = map[h][w+1];
			nr=4;
		}
	}
	if( h+1 < H ){
		if( map[h+1][w] < amn){
			amn = map[h+1][w];
			nr=3;
		}
	}
	if( nr == 0 ){
		basin[h][w]=bas++;
	} else {
		nr--;
		int h2 = h + ofs[nr][0];
		int w2 = w + ofs[nr][1];
		if(basin[h2][w2] != 0) {
			basin[h][w]=basin[h2][w2];
		} else {
			basin[h][w]=trvs(h2,w2);
		}
	}
	return basin[h][w];
}

int main() {
	int N;
	scanf("%d",&N);

	for( int n=0; n<N; n++ ) {
		scanf("%d %d",&H,&W);

		for(int h=0; h<H; h++) {
			for(int w=0; w<W; w++) {
				scanf("%d",&map[h][w]);
			}
		}

		memset(basin,0,sizeof(basin));

		bas = 'a';
		
		for(int h=0; h<H; h++) {
			for(int w=0; w<W; w++) {
				if( basin[h][w]==0 ) {
					trvs(h,w);
				}
			}
		}

		printf("Case #%d:\n",n+1);
		for(int h=0; h<H; h++) {
			for(int w=0; w<W; w++) {
				printf("%c ",basin[h][w]);
			}
			printf("\n");
		}
	}

	return 0;
}

