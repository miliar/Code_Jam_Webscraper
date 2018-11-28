#include <stdio.h>
#define MAX 516

int m,n,processed;
int size[MAX];
int bark[MAX][MAX];
int searched;
int is_chestboard(int r1, int c1, int win){
	int i,j;
	if(bark[r1][c1]^1 != bark[r1+1][c1]) 	return 0;
	for(j=c1+1;j<c1+win;j++){
		if(bark[r1][j] ==3) 	return 0;
		if(bark[r1][j]^1 != bark[r1][j-1]) 		return 0;
	}
	for(i=r1+2;i<r1+win;i+=2){
		for(j=c1;j<c1+win;j++)
			if(bark[i][j]!=bark[r1][j]) return 0;
	}
	for(i=r1+1;i<r1+win;i+=2){
		for(j=c1;j<c1+win;j++){
			if(bark[i][j]==3) 			return 0;
			if(bark[i][j]==bark[r1][j]) return 0;
		}
	}
	return 1;
}
void find_largest_chestboard(){
	int cur;
	int i,j,win,k,max=1, ti=-1,tj;
	for(i=0;i<m;i++){
		for(j=0;j<n;j++){
			if(bark[i][j]!=3 && ti==-1){
				ti=i; tj=j;
			}
			for(win=max+1; i+win-1<m && j+win-1<n ;win++){
				if(is_chestboard(i,j,win)){
					max = win;
					ti = i;
					tj = j;
				}
			}
		}
	}
	for(i=ti;i<ti+max;i++){
		for(j=tj;j<tj+max;j++){
			bark[i][j] = 3;
			processed++;
		}
	}
	size[max]++;
}
char char2num(char c){
	if('0'<=c && c<='9')
		return c-'0';
	else
		return c-'A'+10;
}
void printboard(){
	int i,j;
	printf("----------------\n");
	for(i=0;i<m;i++){
		for(j=0;j<n;j++)
			printf("%d", bark[i][j]);
		printf("\n");
	}
	printf("----------------\n");
}
void solve(){
	int i,j,k;
	char num;
	char str[500];
	processed = 0;
	scanf("%d %d", &m, &n);
	for(i=0;i<n;i++)
		size[i]=0;
	for(i=0;i<m;i++){
		scanf("%s", str);
		for(k=0,j=0;str[k]!='\0';k++,j+=4){
			num = char2num(str[k]);
			bark[i][j]   = (num & 8)!=0;
			bark[i][j+1] = (num & 4)!=0;
			bark[i][j+2] = (num & 2)!=0;
			bark[i][j+3] = (num & 1)!=0;
		}
	}
	while(processed < m*n){
		find_largest_chestboard();
	}
	for(i=0,k=0;i<n;i++)
		if(size[i]>0) k++;
	printf("%d\n", k);
	for(i=n-1;i>=0;i--){
		if(size[i]>0)
			printf("%d %d\n", i, size[i]);
	}
}
int main(){
	int i,T;
	scanf("%d", &T);
	for(i=1;i<=T;i++){
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
