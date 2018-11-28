#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
#include <cstring>
#include <string>

#define forloop(i,a,b) for(int i=(a);i<(b);i++)

char box[100][100];

int process(){
	char ch;
	int r,c;
	scanf("%d%d\n",&r,&c);
	forloop(i,0,r){
		forloop(j,0,c){
			scanf("%c",&box[i][j]);
//			printf("%c %d %d \n",box[i][j],i,j);
		}	
		ch=getchar();	
	}

	bool run=true;
	
	for(int i=0;i<r && run;i++){
		for(int j=0;j<c && run;j++){
			if(box[i][j]=='#'){
				run=(i<r-1 && j<c-1 && box[i+1][j]=='#' && box[i][j+1]=='#' && box[i][j+1]=='#');
				if(run){
					box[i][j]='/';
					box[i][j+1]='\\';
					box[i+1][j]='\\';
					box[i+1][j+1]='/';
				}
			}
		}
	}

	if(run){
		forloop(i,0,r){
			forloop(j,0,c){
				printf("%c",box[i][j]);
			}	
			putchar('\n');	
		}
	}else{
		printf("Impossible\n");
	}
	return 0;
}

int main(){
	int i,testcases;
	scanf("%d",&testcases);
	forloop(i,0,testcases){
		 printf("Case #%d:\n",i+1);
           process();
	}
}
