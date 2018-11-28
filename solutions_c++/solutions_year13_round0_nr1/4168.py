#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
char M[5][5];
char tmp[4][4];
bool isWinner(char x);
int cont;
int main(){
	int t; scanf("%d\n",&t);
	for(int i=1;i<=t;i++){
		for(int j=0;j<4;j++) scanf("%s\n",M[j]);
		cont=0;
		if(isWinner('X')) printf("Case #%d: X won\n",i);
		else if(isWinner('O')) printf("Case #%d: O won\n",i);
		else if(cont)  printf("Case #%d: Game has not completed\n",i);
		else printf("Case #%d: Draw\n",i);
	}
return 0;}
bool isWinner(char x){
	for(int i=0;i<4;i++) for(int j=0;j<4;j++){
	 tmp[i][j]=M[i][j];
	 if(tmp[i][j]=='.') cont++; 
	}
	for(int i=0;i<4;i++) for(int j=0;j<4;j++)
	  if(tmp[i][j]=='T')
	  	tmp[i][j]=x;
	for(int i=0;i<4;i++){ 
		int num=4;
		for(int j=0;j<4;j++){
		   if(tmp[i][j]==x) num--;
		   
		}
		if(!num) return true;
	}
	for(int i=0;i<4;i++){ 
		int num=4;
		for(int j=0;j<4;j++){
		   if(tmp[j][i]==x) num--;
		}
		if(!num) return true;
	}
	int num1=4,num2=4;
	for(int i=0;i<4;i++){ 
		if(tmp[i][i]==x) num1--;
		if(tmp[i][3-i]==x) num2--;
	}
	if(!num1 or !num2) return true;
	return false;
}
