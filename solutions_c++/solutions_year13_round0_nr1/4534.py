#include<iostream>
#include<cstdio>
#define gi(a) gar=scanf("%d",&a)
#define For(i,lb,ub) for(int i=lb;i<ub;i++)
int gar;
using namespace std;
int main()
{
  int test;
  int t;
  scanf("%d",&t);
  test = t;
  For(T,1,t+1) 
  {
    char arr[4][4];
    For(i,0,4){
      scanf("%s",arr[i]);
      //printf("%s\n",arr[i]);
    }
    int state = -1; //0-> X won 1-> O won 2-> draw 3-> not completed
    if(state==-1){
      For(i,0,4){
	bool chk = true;
	For(j,0,4)
	  chk = chk && (arr[i][j]=='X' || arr[i][j]=='T');
	if(chk)
	  state = 0;
      }
      For(j,0,4){
	bool chk = true;
	For(i,0,4)
	  chk = chk && (arr[i][j]=='X' || arr[i][j]=='T');
	if(chk)
	  state = 0;
      }
      bool chk = true;
      For(i,0,4){
	chk = chk && (arr[i][i]=='X' || arr[i][i]=='T');
      }
      if(chk)
	state = 0;
      chk = true;
      For(i,0,4){
	chk = chk && (arr[i][3-i]=='X' || arr[i][3-i]=='T');
      }
      if(chk)
	state = 0;
    }
    if(state==-1){
      For(i,0,4){
	bool chk = true;
	For(j,0,4)
	  chk = chk && (arr[i][j]=='O' || arr[i][j]=='T');
	if(chk)
	  state = 1;
      }
      For(j,0,4){
	bool chk = true;
	For(i,0,4)
	  chk = chk && (arr[i][j]=='O' || arr[i][j]=='T');
	if(chk)
	  state = 1;
      }
      bool chk = true;
      For(i,0,4){
	chk = chk && (arr[i][i]=='O' || arr[i][i]=='T');
      }
      if(chk)
	state = 1;
      chk = true;
      For(i,0,4){
	chk = chk && (arr[i][3-i]=='O' || arr[i][3-i]=='T');
      }
      if(chk)
	state = 1;
    }
    if(state == -1)
    {
      For(i,0,4){
	For(j,0,4){
	  if(arr[i][j] == '.')
	    state = 3;
	}
      }
    }
    if(state==-1)
      state=2;
    
    printf("Case #%d: ",T);
    switch(state)
    {
      case 0: printf("X won");break;
      case 1: printf("O won");break;
      case 2: printf("Draw");break;
      case 3: printf("Game has not completed");break;
      default: printf("Error");break;
    }
    printf("\n");
  }
  return 0;
}