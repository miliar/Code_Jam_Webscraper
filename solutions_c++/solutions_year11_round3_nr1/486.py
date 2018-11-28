#include<stdio.h>
#include<stdlib.h>
char map[60][60];
int check(char c){
	if(c == '.') return 1;
	if(c == '/') return 1;
	if(c == '\\')return 1;
	return 0;
}
int main(){
	int T;
	scanf("%d",&T);
	int R,C;
	for(int t=0;t<T;t++){
		scanf("%d %d",&R,&C);
		for(int i=0;i<60;i++)for(int j=0;j<60;j++)map[i][j] = 0;
		for(int i=0;i<R;i++){
			scanf("%s",&(map[i + 1][1]));
		}
		int flag = 0;
		for(int i=1;i<=R;i++){
			for(int j=1;j<=C;j++){
				if(check(map[i][j]) == 1)continue;
				if(map[i][j] == '#'){
					if(i == R || j == C){
						flag = 1;
						break;
					}
					for(int k=0;k<2;k++){
						for(int l=0;l<2;l++){
							if(check(map[i + k][l + j]) == 1){
								flag = 1;
								break;
							}
						}
					}
					if(flag == 0){
						map[i][j] = '/';
						map[i][j + 1] = '\\';
						map[i + 1][j + 1] = '/';
						map[i + 1][j] = '\\';
					}
				}
			}
			if(flag == 1)break;
		}
		printf("Case #%d:\n",t + 1);
		if(flag == 1){
			printf("Impossible\n");
		}else{
			for(int i=1;i<=R;i++){
				for(int j=1;j<=C;j++){
					printf("%c",map[i][j]);
				}
				printf("\n");
			}
		
		}
	}
	return 0;
}
