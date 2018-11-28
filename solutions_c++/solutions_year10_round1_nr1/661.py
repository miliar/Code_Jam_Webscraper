#include<stdio.h>
#include<stdlib.h>
char board[60][60];
char newboard[60][60];
int n,K;
int red;
int blue;
void gra(){
	int lo[60];
	for(int i=0;i<60;i++)
		lo[i] = 0;
	for(int i=n+1;i>0;i--){
		for(int j=1;j<n+1;j++){
			if(newboard[i][j] != '.'){
				newboard[n + 1 - lo[j]][j] = newboard[i][j];
				if(n + 1 - lo[j] != i)newboard[i][j] = '.';
				lo[j]++;
			}
		}
	}
	return ;
}


void check_v(int x,int y){
	int k;
	for(k=0;k<K;k++){
		if(x + k > n + 1)break;
		if(newboard[x + k][y] != 'R'){
			break;
		}
	}
	if(k == K)red=1;
	for(k=0;k<K;k++){
		if(x + k > n + 1)break;
		if(newboard[x + k][y] != 'B'){
			break;
		}
	}
	if(k == K)blue=1;
	
}
void check_h(int x,int y){
	int k;
	for(k=0;k<K;k++){
		if(y + k > n + 1)break;
		if(newboard[x][y + k] != 'R'){
			break;
		}
	}
	if(k == K)red=1;
	for(k=0;k<K;k++){
		if(y + k > n + 1)break;
		if(newboard[x][y + k] != 'B'){
			break;
		}
	}
	if(k == K)blue=1;
	
}

void check_rd(int x,int y){
	int k;
	for(k=0;k<K;k++){
		if(y - k < 1 || x + k > n + 1)break;
		if(newboard[x + k][y - k] != 'R'){
			break;
		}
	}
	if(k == K)red=1;
	for(k=0;k<K;k++){
		if(y - k < 1 || x + k > n + 1)break;
		if(newboard[x + k][y - k] != 'B'){
			break;
		}
	}
	if(k == K)blue=1;
	
}
void check_cd(int x,int y){
	int k;
	for(k=0;k<K;k++){
		if(y + k > n + 1 || x + k > n + 1)break;
		if(newboard[x + k][y + k] != 'R'){
			break;
		}
	}
	if(k == K)red=1;
	for(k=0;k<K;k++){
		if(y + k > n + 1 || x + k > n + 1)break;
		if(newboard[x + k][y + k] != 'B'){
			break;
		}
	}
	if(k == K)blue=1;
	
}

void check_win(){
	for(int i=1;i<n + 1;i++){
		for(int j=1;j<n+1;j++){
			check_h(i,j);
			check_v(i,j);
			check_cd(i,j);
			check_rd(i,j);
		}
	}
}

int main(){
	int t,ca;
	scanf("%d\n",&t);
	for(ca=0;ca<t;ca++){
		scanf("%d %d",&n,&K);
		red = blue = 0;
		for(int i=0;i<60;i++)
			for(int j=0;j<60;j++)
				board[i][j] = newboard[i][j] = 0;
		for(int i=1;i<n + 1;i++){
			scanf("%s",board[i] + 1);
		}
		for(int i=1;i<n+1;i++){
			for(int j=1;j<n+1;j++){
				newboard[i][j] = board[n + 1 - j][i];
			}
		}/*
		for(int i=1;i<n+1;i++){
			printf("%s\n",newboard[i] + 1);
		}*/
		gra();
		/*
		for(int i=1;i<n+1;i++){
			printf("%s\n",newboard[i] + 1);
		}*/
		check_win();
		printf("Case #%d: ",ca + 1);
		if(red == 1 && blue == 1){
			printf("Both\n");
		}else if(red == 1){
			printf("Red\n");
		}else if(blue == 1){
			printf("Blue\n");
		}else{
			printf("Neither\n");
		}
	}
	return 0;
}
