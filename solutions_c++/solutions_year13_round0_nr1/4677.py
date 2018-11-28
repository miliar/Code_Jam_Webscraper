#include<stdio.h>
char t[4][4];
int ton(char c){
	if(c=='T')return 0;
	if(c=='X')return 1;
	if(c=='O')return 2;
	return 3;
}
int check(char a,char b,char c,char d){
	int cnt[4]={0,0,0,0};
	cnt[ton(a)]++;
	cnt[ton(b)]++;
	cnt[ton(c)]++;
	cnt[ton(d)]++;
	if(cnt[0]+cnt[1]==4)return 0;
	if(cnt[0]+cnt[2]==4)return 1;
	return 2;
}
int min(int a,int b){return a<b?a:b;}
int main(){
	int nd;
	scanf("%d",&nd);
	for(int ni=0;ni<nd;ni++){
		int i,j;
		bool fill=true;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf(" %c",&t[i][j]);
				if(t[i][j]=='.')fill=false;
			}
		}
		int outcome=2;
		for(i=0;i<4;i++){
			outcome=min(outcome,check(t[i][0],t[i][1],t[i][2],t[i][3]));
			outcome=min(outcome,check(t[0][i],t[1][i],t[2][i],t[3][i]));
		}
		outcome=min(outcome,check(t[0][0],t[1][1],t[2][2],t[3][3]));
		outcome=min(outcome,check(t[3][0],t[2][1],t[1][2],t[0][3]));
		printf("Case #%d: ",ni+1);
		if(outcome==0)printf("X won\n");
		if(outcome==1)printf("O won\n");
		if(outcome==2){
			if(fill)printf("Draw\n");
			else printf("Game has not completed\n");
		}
	}
	return 0;
}