#include<stdio.h>
int main(){
int T, cases = 0;
scanf("%d",&T);
while(T--){
	cases++;
	int R,C;
	scanf("%d%d",&R,&C);
	char mat[100][100];
	for(int i = 0; i < R; i++){
		scanf("%s", mat[i]);
	}
	
	for(int i = 0; i < R; i++){
		for(int j = 0; j < C; j++){
			if( i < R - 1 && j < C - 1 && mat[i][j] == '#' && mat[i][j+1] == '#' && mat[i+1][j] == '#' && mat[i+1][j+1] == '#'){
				mat[i][j] = '/';
				mat[i][j+1] = '\\';
				mat[i+1][j] = '\\';
				mat[i+1][j+1] = '/';
			}
		}
	}
	bool isPos = true;
	for(int i = 0; i < R; i++){
		for(int j = 0; j < C; j++){
			if(mat[i][j] == '#'){
				isPos = false;
				break;
			}
		}
		if(!isPos){
			break;
		}
	}
	printf("Case #%d:\n",cases);
	if(isPos){
		for(int i = 0; i < R; i++){
			printf("%s\n", mat[i]);
		}
	}else{
		printf("Impossible\n");
	}
}
return 0;
}
