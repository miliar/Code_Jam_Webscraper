#include<cstdio>
#include<cstring>
using namespace std;
char brd[5][5];
char row(int r)
{
   int i,x,o,t;
   x=o=t=0;
   for(i=0; i<4; i++)
   {
      if(brd[r][i]=='X') x++;
      else if(brd[r][i]=='O') o++;
      else if(brd[r][i]=='T') t++;      
   }
   if(x==4) return 'X';
   if(x==3 && t==1) return 'X';
   if(o==4) return 'O';
   if(o==3 && t==1) return 'O';
   return 0;
}
char col(int c)
{
   int i,x,o,t;
   x=o=t=0;
   for(i=0; i<4; i++)
   {
      if(brd[i][c]=='X') x++;
      else if(brd[i][c]=='O') o++;
      else if(brd[i][c]=='T') t++;      
   }
   if(x==4) return 'X';
   if(x==3 && t==1) return 'X';
   if(o==4) return 'O';
   if(o==3 && t==1) return 'O';
   return 0;  
}
char diag1()
{
   int i,x,o,t;
   x=o=t=0;
   for(i=0; i<4; i++)
   {
      if(brd[i][i]=='X') x++;
      else if(brd[i][i]=='O') o++;
      else if(brd[i][i]=='T') t++;       
   }
   if(x==4) return 'X';
   if(x==3 && t==1) return 'X';
   if(o==4) return 'O';
   if(o==3 && t==1) return 'O';
   return 0;  
}
char diag2()
{
   int i,x,o,t;
   x=o=t=0;
   for(i=0; i<4; i++)
   {
      if(brd[i][3-i]=='X') x++;
      else if(brd[i][3-i]=='O') o++;
      else if(brd[i][3-i]=='T') t++;       
   }
   if(x==4) return 'X';
   if(x==3 && t==1) return 'X';
   if(o==4) return 'O';
   if(o==3 && t==1) return 'O';
   return 0;  
}
bool INC()
{
    int i,j;
    for(i=0; i<4; i++)
      for(j=0; j<4; j++)
         if(brd[i][j]=='.')  return true;
    return false; 
}
char determine()
{
   int i;char ch;
   for(i=0; i<4; i++)
   {
      ch=row(i);
      if(ch!=0) return ch;      
   }
   for(i=0; i<4; i++)
   {
      ch=col(i);
      if(ch!=0) return ch;      
   }
   ch=diag1();
   if(ch!=0) return ch;
   ch=diag2();
   if(ch!=0) return ch;
   bool inc=INC();
   if(inc) return 0;
   else return 1;
}
int main()
{
    int T,i,j,k,l,c=0;
    //freopen("A-large.in","r",stdin);
    //freopen("output1.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
       for(i=0; i<4; i++) scanf("%s",brd[i]);
       char ch=determine();
       if(ch=='X')
         printf("Case #%d: X won\n",++c);
       else if(ch=='O')
         printf("Case #%d: O won\n",++c);
       else if(ch==1)
         printf("Case #%d: Draw\n",++c);
       else if(ch==0)
         printf("Case #%d: Game has not completed\n",++c);
    }
    return 0;
}
