#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <queue>
#include <stack>
#define mp(a,b) make_pair(a,b)

using namespace std;

char g[60][60];

int main(){
	freopen("out.txt","w",stdout);
	int casos, r, c;
	scanf("%d",&casos);
	for(int u=1; u<=casos; u++){
		if(u != 1)
			printf("\n");
		scanf("%d %d",&r,&c);
		for(int i=0; i<r; i++)
			scanf("%s",&g[i]);
		bool resp = true;
		for(int i=0; i<r && resp; i++){
			for(int j=0; j<c && resp; j++){
				if(g[i][j] == '#'){
					g[i][j] = '/';
					if(i+1 < r && g[i+1][j] == '#'){
						g[i+1][j] = '\\';
						if(j+1 < c && g[i][j+1] == '#' && g[i+1][j+1] == '#'){
							g[i][j+1] = '\\';
							g[i+1][j+1] = '/';
						}else
							resp = false;							
					}else
						resp = false;
				}
			}
		}
		printf("Case #%d:\n",u);
		if(resp){
			for(int i=0; i<r-1; i++){
				printf("%s",g[i]);
				printf("\n");
			}
			printf("%s",g[r-1]);
		}else
			printf("Impossible");
	}
}
