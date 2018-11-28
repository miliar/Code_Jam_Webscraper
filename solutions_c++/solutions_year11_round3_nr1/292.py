#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
	char input[55][55];
	int M , N;
int check(int r , int col){
int i,j,k;
	if(r+1 >=N || col+1 >=M ) return 0;
	if(input[r+1][col] !='#' || input[r+1][col+1]!='#' ||
	input[r][col+1]!='#')return 0;

	input[r][col]  = '/';
	input[r][col+1]='\\' ;

	input[r+1][col] ='\\';
	input[r+1][col+1] = '/';
	return 1;
}
int main(){
	int T;
	int t,i,j,k;
	int fail=0;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		fail=0;
		memset(input,0,sizeof(input));
		scanf("%d %d ",&N,&M);
		for(i=0;i<N;i++)
		gets(input[i]);
		for(i=0;i<N;i++){
			for(j=0;j<M;j++){
				if(input[i][j]=='#'){
					if(!check(i,j)){
						fail = 1;
						break;
					}
				}
			}
		}
		printf("Case #%d:\n",t);
		if(fail==1){
			printf("Impossible\n");
		}
		else{
		for(i=0;i<N;i++)
			printf("%s\n",input[i]);
		}

	}


	return 0;
}
