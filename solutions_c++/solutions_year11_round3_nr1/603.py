#include <stdio.h>
char data[100][100];
char tiles[5];

int lines, columns;
int dx[5];
int dy[5];

bool change(int i,int j){
	if(i >= lines-1) return false;
	if(j >= columns-1) return false;
	for(int k = 0;k<4;k++){
		char * val = &(data[i+dx[k]][j+dy[k]]);
		if(*val != '#')
			return false;
		*val = tiles[k];
	}
	return true;	
}
int main(){
	int cases;
	scanf("%d",&cases);
	tiles[0] = '/';
	tiles[1] = '\\';
	tiles[2] = '/';
	tiles[3] = '\\';
	dx[0] = 0; dy[0] = 0;
	dx[1] = 1; dy[1] = 0;
	dx[2] = 1; dy[2] = 1;
	dx[3] = 0; dy[3] = 1;
	for(int c = 1;c<=cases;c++){

		scanf("%d %d",&lines,&columns);
		for(int i = 0;i<lines;i++){
			scanf(" %s",data[i]);
		}
		bool FUUU = false;
		for(int i = 0;i<lines;i++){
			for(int j = 0;j<columns;j++){
				if(data[i][j] == '#'){
					if(!change(i,j)){
						FUUU = true;
					}
				}
				if(FUUU) 
					break;
			}
			if(FUUU)
				break;
		}
		printf("Case #%d:\n",c);
		if(FUUU){
			printf("Impossible\n");
		}else{
			for(int i = 0;i<lines;i++){
				printf("%s\n",data[i]);
			}
		}
	}
	return 0;
}
