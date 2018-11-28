#include <stdio.h>

int t;
char T[4][5];

int checkRow(int i)
{
 int cx=0, co=0, ct=0, cp=0;
 for(int j=0;j<4;j++)
  if(T[i][j]=='.') cp++;
  else if(T[i][j]=='X') cx++;
  else if(T[i][j]=='O') co++;
  else /*if(T[i][j]=='T') */ ct++;
  if(cp) return 3;
  if(cx==0) return 1;
  if(co==0) return 0;
  return 2;
}

int checkCol(int j)
{
 int cx=0, co=0, ct=0, cp=0;
 for(int i=0;i<4;i++)
  if(T[i][j]=='.') cp++;
  else if(T[i][j]=='X') cx++;
  else if(T[i][j]=='O') co++;
  else /*if(T[i][j]=='T') */ ct++;
  if(cp) return 3;
  if(cx==0) return 1;
  if(co==0) return 0;
  return 2;
}

int checkD1()
{
 int cx=0, co=0, ct=0, cp=0;
 for(int i=0;i<4;i++)
  if(T[i][i]=='.') cp++;
  else if(T[i][i]=='X') cx++;
  else if(T[i][i]=='O') co++;
  else /*if(T[i][j]=='T') */ ct++;
  if(cp) return 3;
  if(cx==0) return 1;
  if(co==0) return 0;
  return 2;
}

int checkD2()
{
 int cx=0, co=0, ct=0, cp=0;
 for(int i=0;i<4;i++)
  if(T[i][3-i]=='.') cp++;
  else if(T[i][3-i]=='X') cx++;
  else if(T[i][3-i]=='O') co++;
  else /*if(T[i][j]=='T') */ ct++;
  if(cp) return 3;
  if(cx==0) return 1;
  if(co==0) return 0;
  return 2;
}

void dale()
{
 int pos[10];
 pos[0] = checkRow(0);
 pos[1] = checkRow(1);
 pos[2] = checkRow(2);
 pos[3] = checkRow(3);
 pos[4] = checkCol(0);
 pos[5] = checkCol(1);
 pos[6] = checkCol(2);
 pos[7] = checkCol(3);
 pos[8] = checkD1();
 pos[9] = checkD2();
 
 int vacios = 0;
 
 for(int i=0;i<10;i++)
 {
  if(pos[i]==0){printf("X won\n");return;}
  if(pos[i]==1){printf("O won\n");return;}
  if(pos[i]==3) vacios++;
  
 }
 if(vacios)printf("Game has not completed\n");
 else printf("Draw\n");
}

int main()
{
 //freopen("A-large.in", "r", stdin);
 //freopen("A-large.out", "w", stdout);
 scanf("%d", &t);
 for(int i=1;i<=t;i++)
 {
  scanf("%s %s %s %s", &T[0], &T[1], &T[2], &T[3]);
  printf("Case #%d: ", i);
  dale();
 }
}
