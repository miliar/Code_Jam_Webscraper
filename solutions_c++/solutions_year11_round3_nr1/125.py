#include <stdio.h>
#include <map>
#include <string>
using namespace std;

char g[64][64];

void run(int fall){
	printf("Case #%d:\n", fall+1);
	int R,C;
	scanf("%d %d", &R, &C);
	for(int y=0;y<R;y++){
		scanf("%s", g[y]);
	}
	for(int y=0;y<R;y++){
		for(int x=0;x<C;x++){
			if(g[y][x] == '#'){
				if(y==R-1 || x==C-1){
					printf("Impossible\n");
					return;
				}
				if(g[y][x+1] != '#'
					|| g[y+1][x] != '#'
					|| g[y+1][x+1] != '#'){
					printf("Impossible\n");
					return;
				}
				g[y][x] = '/';
				g[y][x+1] = '\\';
				g[y+1][x] = '\\';
				g[y+1][x+1] = '/';
			}			
		}
	}
	
	for(int y=0;y<R;y++){
		printf("%s\n", g[y]);
	}
}


int main(){
	int N;
	scanf("%d", &N);
	for(int i=0;i<N;i++){
		run(i);
	}	
}