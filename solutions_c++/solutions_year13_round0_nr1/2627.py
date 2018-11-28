#include<iostream>
#include<string.h>
#include<algorithm>
#include<cmath>
#include<stdio.h>
#include<stack>
#include<queue>
#include<map>
#include<set>
#define ll long long 
#define oo 1000000000
using namespace std; 
char arc[6][6]; 
int f[2][2]={{1,0},{0,1}};
void judge()
{
      int i,j,t,k1,k2;
      for (i=1;i<=4;i++)
      {
           k1=k2=0;
           for (j=1;j<=4;j++)
           {
                if (arc[i][j]=='X' || arc[i][j]=='T') k1++;
                if (arc[i][j]=='O' || arc[i][j]=='T') k2++;
           }
           if (k1==4) {  printf("X won\n");  return;   } 
           if (k2==4) {  printf("O won\n");  return;   } 
      }
      for (j=1;j<=4;j++)
      {
           k1=k2=0;
           for (i=1;i<=4;i++)
           {
                if (arc[i][j]=='X' || arc[i][j]=='T') k1++;
                if (arc[i][j]=='O' || arc[i][j]=='T') k2++;
           }
           if (k1==4) {  printf("X won\n");  return;   } 
           if (k2==4) {  printf("O won\n");  return;   } 
      }    
      i=j=k1=k2=0;  
      for (t=1;t<=4;t++)
      {
            i++; j++;
            if (arc[i][j]=='X' || arc[i][j]=='T') k1++;
            if (arc[i][j]=='O' || arc[i][j]=='T') k2++;
      }    
      if (k1==4) {  printf("X won\n");  return;   } 
      if (k2==4) {  printf("O won\n");  return;   } 
      i=0; j=5; k1=k2=0;
      for (t=1;t<=4;t++)
      {
            i++; j--;
            if (arc[i][j]=='X' || arc[i][j]=='T') k1++;
            if (arc[i][j]=='O' || arc[i][j]=='T') k2++;
      }    
      if (k1==4) {  printf("X won\n");  return;   } 
      if (k2==4) {  printf("O won\n");  return;   } 
      for (i=1;i<=4;i++)
        for (j=1;j<=4;j++)
          if (arc[i][j]=='.') { printf("Game has not completed\n"); return; }
      printf("Draw\n");
      return;
}
int main()
{
    //  freopen("A-large.in","r",stdin);
    //  freopen("output.txt","w",stdout);
      int T,t,i,j;
      scanf("%d",&T);
      for (t=1;t<=T;t++)
      {  
            for (i=0;i<=4;i++) gets(arc[i]+1); 
            printf("Case #%d: ",t);
            judge();
      }
      return 0;
}
