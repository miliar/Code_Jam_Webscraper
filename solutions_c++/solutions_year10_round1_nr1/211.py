#include<stdio.h>
#include<string.h>
char s[100][100],rs[100][100],top[100];
int times,n,k;
bool k_in_a_rd(int x,int y){
	for(int i=1;i<k;i++){
		if(rs[x+i][y+i]!=rs[x][y])
			return false;
	}
	return true;
}
bool k_in_a_ld(int x,int y){
	if(y<k-1)return false;
	for(int i=1;i<k;i++){
		if(rs[x+i][y-i]!=rs[x][y])
			return false;
	}
	return true;
}
bool k_in_a_col(int x,int y){
	for(int i=1;i<k;i++){
		if(rs[x+i][y]!=rs[x][y])
			return false;
	}
	return true;
}
bool k_in_a_row(int x,int y){
	for(int i=1;i<k;i++){
		if(rs[x][y+i]!=rs[x][y])
			return false;
	}
	return true;
}
int main(){
	scanf("%d",&times);
	for(int tm=1;tm<=times;tm++){
		printf("Case #%d: ",tm);
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;i++)
			scanf("%s",s[i]);
		for(int i=0;i<n;i++)top[i]=0;
		for(int i=0;i<100;i++)
			for(int j=0;j<100;j++)
				rs[i][j]='.';
		for(int i=0;i<n;i++){
			for(int j=n-1;j>=0;j--){
				if(s[i][j]!='.'){
					rs[i][top[i]++]=s[i][j];
				}
			}
		}
		bool red=0,blue=0;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if(rs[i][j]=='.')continue;
				if(k_in_a_row(i,j) || k_in_a_col(i,j) ||
				k_in_a_ld(i,j) || k_in_a_rd(i,j)){
					if(rs[i][j]=='R')red=true;
					else blue=true;
				}	
			}
		}
		if(red && blue)printf("Both\n");
		else if(red)printf("Red\n");
		else if(blue)printf("Blue\n");
		else printf("Neither\n");
	}
	return 0;
}
