#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

char map[52][52];
int hash[52][52];

int main(){
	int i,j;
	int T;
	int r,c;
	int flag,cas = 1;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
		while(T --){
			scanf("%d%d",&r,&c);
			for(i = 0; i < r; i ++)
				scanf("%s",map[i]);
			flag = 1;
			for(i = 0; i < r;i ++){
				for(j = 0; j < c; j ++){
					if(map[i][j] == '#'){
						if(i+1 >= r || j+1 >= c)
							flag = 0;
						if(map[i][j] == '#' && map[i+1][j] == '#' && map[i][j+1] == '#' && map[i+1][j+1] == '#'){
						map[i][j] = '/';
						map[i+1][j] = '\\';
						map[i][j+1] = '\\';
						map[i+1][j+1] = '/';
						}else{
							flag = 0;
						}
					}
				}
			}
			printf("Case #%d:\n",cas++);
			if(!flag){
				printf("Impossible\n");
			}else{
				for(i = 0; i < r;i ++)
					printf("%s\n",map[i]);
			}
		}
	return 0;
}