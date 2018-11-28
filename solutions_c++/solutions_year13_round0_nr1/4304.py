#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
 int t, T, i, j;
 char a[5][5];
 scanf("%d",&T);
 for(t=1;t<=T;++t)
 {
  for(i=0;i<4;++i) scanf("%s",a[i]);
  //For X
   if(a[0][0]=='X' || a[0][0] == 'T')
   {
    if((a[1][1]=='X' || a[1][1]=='T')&&(a[2][2]=='X' || a[2][2]=='T')&&(a[3][3]=='X' || a[3][3]=='T')){printf("Case #%d: X won\n",t);continue;}
    if((a[1][0]=='X' || a[1][0]=='T')&&(a[2][0]=='X' || a[2][0]=='T')&&(a[3][0]=='X' || a[3][0]=='T')){printf("Case #%d: X won\n",t);continue;}
    if((a[0][1]=='X' || a[0][1]=='T')&&(a[0][2]=='X' || a[0][2]=='T')&&(a[0][3]=='X' || a[0][3]=='T')){printf("Case #%d: X won\n",t);continue;}
   }
   if(a[0][3]=='X' || a[0][3]=='T')
   {
    if((a[1][2]=='X' || a[1][2]=='T')&&(a[2][1]=='X' || a[2][1]=='T')&&(a[3][0]=='X' || a[3][0]=='T')){printf("Case #%d: X won\n",t);continue;}
    if((a[1][3]=='X' || a[1][3]=='T')&&(a[2][3]=='X' || a[2][3]=='T')&&(a[3][3]=='X' || a[3][3]=='T')){printf("Case #%d: X won\n",t);continue;}
   }
   if((a[3][0]=='X' || a[3][0]=='T')&&(a[3][1]=='X' || a[3][1]=='T')&&(a[3][2]=='X' || a[3][2]=='T')&&(a[3][3]=='X' || a[3][3]=='T')){printf("Case #%d: X won\n",t);continue;}
   if((a[2][0]=='X' || a[2][0]=='T')&&(a[2][1]=='X' || a[2][1]=='T')&&(a[2][2]=='X' || a[2][2]=='T')&&(a[2][3]=='X' || a[2][3]=='T')){printf("Case #%d: X won\n",t);continue;}
   if((a[1][0]=='X' || a[1][0]=='T')&&(a[1][1]=='X' || a[1][1]=='T')&&(a[1][2]=='X' || a[1][2]=='T')&&(a[1][3]=='X' || a[1][3]=='T')){printf("Case #%d: X won\n",t);continue;}
   if((a[0][1]=='X' || a[0][1]=='T')&&(a[1][1]=='X' || a[1][1]=='T')&&(a[2][1]=='X' || a[2][1]=='T')&&(a[3][1]=='X' || a[3][1]=='T')){printf("Case #%d: X won\n",t);continue;}
   if((a[0][2]=='X' || a[0][2]=='T')&&(a[1][2]=='X' || a[1][2]=='T')&&(a[2][2]=='X' || a[2][2]=='T')&&(a[3][2]=='X' || a[3][2]=='T')){printf("Case #%d: X won\n",t);continue;}
  //For O
   if(a[0][0]=='O' || a[0][0] == 'T')
   {
    if((a[1][1]=='O' || a[1][1]=='T')&&(a[2][2]=='O' || a[2][2]=='T')&&(a[3][3]=='O' || a[3][3]=='T')){printf("Case #%d: O won\n",t);continue;}
    if((a[1][0]=='O' || a[1][0]=='T')&&(a[2][0]=='O' || a[2][0]=='T')&&(a[3][0]=='O' || a[3][0]=='T')){printf("Case #%d: O won\n",t);continue;}
    if((a[0][1]=='O' || a[0][1]=='T')&&(a[0][2]=='O' || a[0][2]=='T')&&(a[0][3]=='O' || a[0][3]=='T')){printf("Case #%d: O won\n",t);continue;}
   }
   if(a[0][3]=='O' || a[0][3]=='T')
   {
    if((a[1][2]=='O' || a[1][2]=='T')&&(a[2][1]=='O' || a[2][1]=='T')&&(a[3][0]=='O' || a[3][0]=='T')){printf("Case #%d: O won\n",t);continue;}
    if((a[1][3]=='O' || a[1][3]=='T')&&(a[2][3]=='O' || a[2][3]=='T')&&(a[3][3]=='O' || a[3][3]=='T')){printf("Case #%d: O won\n",t);continue;}
   }
   if((a[3][0]=='O' || a[3][0]=='T')&&(a[3][1]=='O' || a[3][1]=='T')&&(a[3][2]=='O' || a[3][2]=='T')&&(a[3][3]=='O' || a[3][3]=='T')){printf("Case #%d: O won\n",t);continue;}
   if((a[2][0]=='O' || a[2][0]=='T')&&(a[2][1]=='O' || a[2][1]=='T')&&(a[2][2]=='O' || a[2][2]=='T')&&(a[2][3]=='O' || a[2][3]=='T')){printf("Case #%d: O won\n",t);continue;}
   if((a[1][0]=='O' || a[1][0]=='T')&&(a[1][1]=='O' || a[1][1]=='T')&&(a[1][2]=='O' || a[1][2]=='T')&&(a[1][3]=='O' || a[1][3]=='T')){printf("Case #%d: O won\n",t);continue;}
   if((a[0][1]=='O' || a[0][1]=='T')&&(a[1][1]=='O' || a[1][1]=='T')&&(a[2][1]=='O' || a[2][1]=='T')&&(a[3][1]=='O' || a[3][1]=='T')){printf("Case #%d: O won\n",t);continue;}
   if((a[0][2]=='O' || a[0][2]=='T')&&(a[1][2]=='O' || a[1][2]=='T')&&(a[2][2]=='O' || a[2][2]=='T')&&(a[3][2]=='O' || a[3][2]=='T')){printf("Case #%d: O won\n",t);continue;}
  //Draw
   int flag=1;
   for(i=0;i<4;++i)
    for(j=0;j<4;++j)
     if(a[i][j]=='.'){flag=0;break;}
   if(flag){printf("Case #%d: Draw\n",t);continue;}
   
   //Not completed
    printf("Case #%d: Game has not completed\n",t);
  
  scanf("%c",&a[0][0]);
 }
 return 0;
}