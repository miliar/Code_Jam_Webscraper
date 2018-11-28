#include <stdio.h>
char s[4][4];
int row(int r)
{
  int i,x=0,o=0,t=0;
  for(i=0;i<4;i++){
    if(s[r][i]=='.') return 0;
    if(s[r][i]=='X') x++;
    if(s[r][i]=='O') o++;
    else t++;}
    if(!o) return 1;
  if(!x) return 2;
  return 0;
}
int col(int r)
{
  int i,x=0,o=0,t=0;
  for(i=0;i<4;i++){
    if(s[i][r]=='.') return 0;
    if(s[i][r]=='X') x++;
    if(s[i][r]=='O') o++;
    else t++;}
    if(!o) return 1;
  if(!x) return 2;
  return 0;
}
int dig()
{
    int i,j,x=0,o=0,t=0;

  for(i=0;i<4;i++)
  {
    //if(s[i][i]=='.') return 0;
    if(s[i][i]=='X') x++;
    if(s[i][i]=='O') o++;
    if(s[i][i]=='T') t++;
  }
  if(x+o+t==4){
  if(!o) return 1;
  if(!x) return 2;}
  
  x=t=o=0;
  for(i=0,j=3;i<4;i++,j--)
  {
    if(s[i][j]=='.') return 0;
    if(s[i][j]=='X') x++;
    if(s[i][j]=='O') o++;
    else t++;
  }
  if(!o) return 1;
  if(!x) return 2;
  return 0;
  

}
int tri()
{
  int i,j;
  for(i=0;i<4;i++)
    for(j=0;j<4;j++)
      if(s[i][j]=='.') return 1;
    return 0;
}
int main()
{

int t,T,i,j,flag;
scanf("%d",&T);
for(t=1;t<=T;t++)
{
  printf("Case #%d: ",t) ;
  for(i=0;i<4;i++)
    scanf("%s",s[i]);
  flag=0;
  for(i=0;i<4&&!flag;i++)
  {
    if(row(i)&&!flag) flag=row(i);
    if(col(i)&&!flag) flag=col(i);
  }
  if(dig()&&!flag) flag=dig();
  if(flag==1) puts("X won");
  else if(flag==2) puts("O won");
  else{
  if(tri()) puts("Game has not completed");
  else puts("Draw");}
}

  return 0;

}