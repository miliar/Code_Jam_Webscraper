#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <queue>
#include <set>
#include <map>
#include <vector>

using namespace std;

char pic[52][52];

int main(){
	int cases,h,w;
	scanf("%d",&cases);
	
	for(int c=1; c<=cases; ++c){
		scanf("%d %d",&h,&w);
		for(int i=0; i<h; ++i){
			scanf("%s",pic[i]);
		}
		for(int i=0; i<h; ++i){
			for(int j=0; j<w; ++j){
				if(pic[i][j]=='#' && pic[i+1][j]=='#' && pic[i+1][j+1]=='#' && pic[i][j+1]=='#'){
					pic[i][j]='/';
					pic[i+1][j]='\\';
					pic[i+1][j+1]='/';
					pic[i][j+1]='\\';
				}
			}
		}
		bool good=true;
		for(int i=0; i<h; ++i){
			for(int j=0; j<w; ++j){
				if(pic[i][j]=='#') 
					good=false;
			}
		}
		printf("Case #%d:\n",c);
		if(good){
			for(int i=0; i<h; ++i){
				printf("%s\n",pic[i]);
			}
		}else{
			printf("Impossible\n");
		}
				
					
	}				



	return 0;
}
