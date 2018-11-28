#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <time.h>
#include <stdlib.h>


#define __int64 long long
//#define MAX(a,b) ((a)>(b)?(a):(b))
//#define MAX(a,b,c) (((a)>(b))?((a)>(c)?(a):(c)):(b))
//#define MIN(a,b) ((a)<(b)?(a):(b))
//#define MIN(a,b,c) ((a)<(b)?(a)<(c)?(a):(c):(b))
int MAX(int a, int b, int c){
	if (a<b) a=b;
	if (a<c) a=c;
	return a;
}
int MIN(int a, int b, int c){
	if (a>b) a=b;
	if (a>c) a=c;
	return a;
}


int map[100][100]={{0}};
bool used[100][100]={{0}};
char label[100][100]={{0}};
int w, h;

char dfs(int x, int y, char pch){
	if (used[y][x]) 
		return label[y][x];
	used[y][x]=true;
	int hn = y>0?map[y-1][x]:map[y][x]+1;
	int hw = x>0?map[y][x-1]:map[y][x]+1;
	int he = x<w-1?map[y][x+1]:map[y][x]+1;
	int hs = y<h-1?map[y+1][x]:map[y][x]+1;

	int h = map[y][x];
	if (hn<=hw && hn<=he && hn<=hs){
		if (h <= hn){
			label[y][x] = pch;
			return pch;
		}else{
			label[y][x]=dfs(x, y-1, pch);
			return label[y][x];
		}
	}

	if (hw<=hn && hw<=he && hw<=hs){
		if (h <= hw){
			label[y][x] = pch;
			return pch;
		}else{
			label[y][x]=dfs(x-1, y, pch);
			return label[y][x];
		}
	}
	
	if (he<=hw && he<=hn && he<=hs){
		if (h <= he){
			label[y][x] = pch;
			return pch;
		}else{
			label[y][x]=dfs(x+1, y, pch);
			return label[y][x];
		}
	}
	
	if (hs<=hw && hs<=he && hs<=hn){
		if (h <= hs){
			label[y][x] = pch;
			return pch;
		}else{
			label[y][x]=dfs(x, y+1, pch);
			return label[y][x];
		}
	}
	_asm
		call dword ptr ds:[0];
}

int main(){
    freopen("map.in", "rt",stdin);
    freopen("map.out", "wt",stdout);
	int t;
    scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++){
		char ch = 'a';
		printf("Case #%d:\n", cas);
		
		scanf("%d%d", &h, &w);
		for (int i=0; i<h; i++) 
			for (int j=0; j<w; j++){
				scanf("%d", &map[i][j]);
				used[i][j]=0;
			}

		for (int y=0; y<h; y++) 
			for (int x=0; x<w; x++){
				if (!used[y][x])
					ch = dfs(x, y, ch) + 1;
			}
		for (int i=0; i<h; i++) {
			int  j;
			for (j=0; j<w-1; j++) 
				printf("%c ", label[i][j]);
			printf("%c\n", label[i][j]);

		}
		
	}
 }