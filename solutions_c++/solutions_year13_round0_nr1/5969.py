#include <cstdio>

char grid[4][10];

const char* check(){
	bool filled = true;
	bool xs,os;
	char c;
	int i,j;
	for(i=0;i<4;++i){
		xs = true;
		os = true;
		for(j=0;j<4;++j){
			if(! (xs||os)) break;
			c = grid[i][j];
			if(c=='.'){
				filled = false;
				xs = false;
				os = false;
			}
			if(c=='X') os = false;
			if(c=='O') xs = false;
		}
		if(xs || os) return (xs ? "X won" : "O won");
	}
	for(i=0;i<4;++i){
		xs = true;
		os = true;
		for(j=0;j<4;++j){
			if(! (xs||os)) break;
			c = grid[j][i];
			if(c=='.'){
				xs = false;
				os = false;
			}
			if(c=='X') os = false;
			if(c=='O') xs = false;
		}
		if(xs || os) return (xs ? "X won" : "O won");
	}
	xs = true;
	os = true;
	for(i=0;i<4;++i){
		if(! (xs||os)) break;
		c = grid[i][i];
		if(c=='.'){
			xs = false;
			os = false;
		}
		if(c=='X') os = false;
		if(c=='O') xs = false;
	}
	if(xs || os) return (xs ? "X won" : "O won");
	xs = true;
	os = true;
	for(i=0;i<4;++i){
		if(! (xs||os)) break;
		c = grid[3-i][i];
		if(c=='.'){
			xs = false;
			os = false;
		}
		if(c=='X') os = false;
		if(c=='O') xs = false;
	}
	if(xs || os) return (xs ? "X won" : "O won");
	return (filled ? "Draw" : "Game has not completed");
}

inline bool ok(int c){
	if(c=='X') return true;
	if(c=='T') return true;
	if(c=='.') return true;
	if(c=='O') return true;
	return false;
}

int main(){
	int T;
	int i,j;
	scanf("%d\n", &T);
	for(i=0;i<T;++i){
		do{
			j = getchar();
		}while(!ok(j));
		ungetc(j,stdin);
		for(j=0;j<4;++j){
			fgets(grid[j], 10, stdin);
		}
		printf("Case #%d: %s\n", i+1, check());
	}
	return 0;
}
