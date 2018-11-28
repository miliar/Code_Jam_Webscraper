#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define len 60
char s[len][len];
int R,C,num;
int d[len][len];
void init(){
	int i,j,m;
	scanf("%d%d",&R,&C);
	for(i=num=0;i<R;i++){
		scanf("%s",s[i]);
		m=(int)strlen(s[i]);
		for(j=0;j<m;j++){
			if(s[i][j]=='#')
				num++;
		}
	}
}
void deal(){
	int i,j;
	bool flag;
	if(num%4){
		printf("Impossible\n");
		return ;
	}
	flag=false;
	for(i=0;i<R;i++){
		for(j=0;j<C;j++){
			if(s[i][j]=='#'){
				if((j+1<C&&s[i][j+1]=='#')&&(i+1<R&&s[i+1][j]=='#')&&(i+1<R&&j+1<C&&s[i+1][j+1]=='#')){
					s[i][j]='/';
					s[i+1][j]='\\';
					s[i][j+1]='\\';
					s[i+1][j+1]='/';
					j++;
				}
				else{
					flag=true;
					break;
				}
			}
		}
		if(flag)
			break;
	}
	if(!flag)
		for(i=0;i<R;i++)
			puts(s[i]);
	else
		printf("Impossible\n");
}
int main(void){
	//freopen("12.in","r",stdin);
	//freopen("12.out","w",stdout);
	int ncase,i;
	scanf("%d",&ncase);
	for(i=1;i<=ncase;i++){
		init();
		printf("Case #%d:\n",i);
		deal();
	}
	return 0;
}
