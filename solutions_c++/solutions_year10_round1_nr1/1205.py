#include "iostream"
#include "cstring"
#include "cstdio"
#include "algorithm"
#include "queue"
#include "vector"
#include "stack"
#include "cmath"
#include "map"
#include "set"
using namespace std;
#define LLD long long
const int N = 101;
const int inf = 1 << 29;
int n,m;
int winr,winb;
char net[N][N],str[N][N];
int iabs(int t){
  if(t>0) return t;
  return -t;
}
int min(int a,int b){
  return a>b?b:a;
}
int max(int a,int b){
  return a>b?a:b;
}
void print(){
  int i,j;
  for(i=1;i<=n;i++){
    for(j=1;j<=n;j++){
      printf("%c",str[i][j]);
    }
    puts("");
  }
  puts("");
}
void rotate(){
  int i,j;
  for(i=1;i<=n;i++)
   for(j=1;j<=n;j++){
     str[j][i]=net[n-i+1][j];
   }
   //print();
}
int judge(int x,int y){
 if(x>=1&&y>=1&&x<=n&&y<=n) return 1;
 return -1;
}
int dir[8][2]={{-1,0},{1,0},{0,-1},{0,1},{1,-1},{-1,1},{1,1},{-1,-1}};
void gravity(){
    int i,j,k;
    int xx,yy;
    for(i=n;i>0;i--){
      for(j=1;j<=n;j++){
        if(str[i][j]=='.'){
           for(k=1;k<=n;k++){
             xx=i+k*dir[0][0];
             yy=j;
             if(judge(xx,yy)==-1) break;
             if(str[xx][yy]!='.'){
                str[i][j]=str[xx][yy];
                str[xx][yy]='.';
			//	print();
				break;
             }
           }
        }
      }
    }
    //puts("after grav");
    //print();
}
void cal(int x,int y,int k,char ch,int tot){
    int xx=x+dir[k][0];
    int yy=y+dir[k][1];
    if(winr==1&&ch=='R') return;
    if(winb==1&&ch=='B') return;
    if(tot>=m) {
      if(ch=='R') winr=1;
      if(ch=='B') winb=1;
      return ;
    }
    if(judge(xx,yy)==-1) return;
    if(str[xx][yy]==ch) {
      cal(xx,yy,k,ch,tot+1);
    }
}
void  win(){
  int i,j,k;
  char ch;
  for(i=n;i>=1;i--)
  for(j=n;j>=1;j--){
	  if(winr==1&&winb==1) break;
      for(k=0;k<8;k++){
          if(winr==0){
          ch='R';
		  if(str[i][j]==ch)
          cal(i,j,k,ch,1);
          }
          if(winb==0){
          ch='B';
		  if(str[i][j]==ch)
          cal(i,j,k,ch,1);
          }
      }
  }
  if(winr==1&&winb==1){
    puts("Both");
  }else if(winr==1){
    puts("Red");
  }else if(winb==1){
      puts("Blue");
  }else {
    puts("Neither");
  }
}
int main(){
  // freopen("R:\in.txt","r",stdin);
  // freopen("R:\out.txt","w",stdout);
   int T,i;
   int cases=1;
   scanf("%d",&T);
   while(T--){
     scanf("%d %d",&n,&m);
     for(i=1;i<=n;i++){
       scanf("%s",&net[i][1]);
     }
     rotate();
     gravity();
     winr=0,winb=0;
     printf("Case #%d: ",cases++);
     win();
   }
}
