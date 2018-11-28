#include <iostream>
#include <string.h>
#include <string>
#include <cstdio>
#include <algorithm>
using namespace std;
char graph[100][100];
int main(){
	int t;
	int i,r,c,j,k;
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&t);
	bool flag;
	for(i = 1;i <= t;i++){
		flag = true;
		scanf("%d%d",&r,&c);
		for (j = 0;j < r;j++){
			scanf("%s",graph[j]);
		}
		for (j = 0;j < r&& flag;j++){
			for (k = 0;k < c&& flag;k++){
				if (graph[j][k] == '#'){
					if (j == r-1 || k == c-1){
						flag = false;
						break;
					}
					if (graph[j][k+1] == '#' && graph[j+1][k]=='#'&& graph[j+1][k+1] == '#'){
						graph[j][k] = '/';
						graph[j][k+1] = '\\';
						graph[j+1][k] = '\\';
						graph[j+1][k+1] = '/';
					}
					else{
						flag = false;
						break;
					}
				}
			}
		}
		printf("Case #%d:\n",i);
		if (!flag){
			printf("Impossible\n");
		}
		else{
			for (j = 0;j < r;j++){
				printf("%s\n",graph[j]);
			}
		}
	}
	return 0;
}