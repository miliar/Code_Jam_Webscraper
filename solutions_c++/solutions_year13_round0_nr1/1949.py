#include<iostream>
#include<algorithm>
#include<cstdio>
#include<string>
#include<cctype>
#include<cstdio>
using namespace std;
char arr[5][5];

int f(int x,int y,char ch){
  bool flag = true;
  for(int i=0;i<4;i++){
    if(i+x>=4 || (arr[i+x][y]!=ch && arr[i+x][y]!='T')){flag = false;break;}
  }
  if(flag)return 1;
  flag = true;
  for(int i=0;i<4;i++){
    if(i+x>=4||i+y>=4|| (arr[i+x][i+y]!=ch && arr[i+x][i+y] != 'T')) {flag = false;break;}
  }
  if(flag)return 1;
  flag = true;
  for(int i=0;i<4;i++){
    if(i+y >=4 || (arr[x][i+y]!=ch && arr[x][i+y]!='T')){flag = false;break;}
  }
  if(flag)return 1; 
  flag = true;
  for(int i=0;i<4;i++){
    if(i+y>=4 || x-i<0 || (arr[x-i][i+y]!=ch && arr[x-i][i+y] != 'T')){flag = false;break;}
  }
  return flag?1:0;
}
int main(){
	int cases;
	bool draw,won; 
	scanf("%d",&cases);
	for(int t = 1; t<= cases;t++){
		for(int i=0;i<4;i++)scanf("%s",arr[i]);
		won = false;
		draw = true;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(arr[i][j]=='.')draw = false;
		
		printf("Case #%d: ",t);
		for(int i=0;i<4;i++){
			if(f(i,0,'X') || f(0,i,'X')){
				printf("X won\n");
				won = true;
				break;
			}
			else if(f(i,0,'O') || f(0,i,'O')){
				printf("O won\n");
				won = true;
				break;
			}
		}
		if(!won){
			if(draw)printf("Draw\n");
			else printf("Game has not completed\n");
		}
	}
} 
