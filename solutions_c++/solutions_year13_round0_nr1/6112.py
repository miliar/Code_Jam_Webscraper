#include<iostream>
#include<string>
#include<cstring>
#include<cstdio>
using namespace std;
string solveGame()
{
    string won=" won"/*1-X,2-O*/, draw="Draw"/*0*/,notc="Game has not completed"/*-1*/;
    int status=0,j;
    char matrix[4][4],x;
   ///read input
   for(int i=0;i<4;i++)
     {
       for(j=0;j<4;j++)
       {
        scanf("%c",&matrix[i][j]);
        if(matrix[i][j]=='.')
            {
                status=-1;
            }
       }
       scanf("%c",&x);
     }


   ///rows
   for(int i=0;i<4;i++)
   {
     int br1=0,br2=0;
     for(int j=0;j<4;j++)
     {
       if(matrix[i][j]=='X') br1++;
       else if(matrix[i][j]=='O') br2++;
       else if(matrix[i][j]=='T') {br1++; br2++;}

     }
     if(br1==4) return "X"+won;
     else if(br2==4) return "O"+won;
   }

   ///columns
   for(int j=0;j<4;j++)
   {
     int br1=0,br2=0;
     for(int i=0;i<4;i++)
     {
       if(matrix[i][j]=='X') br1++;
       else if(matrix[i][j]=='O') br2++;
       else if(matrix[i][j]=='T') {br1++; br2++;}

     }
     if(br1==4) return "X"+won;
     else if(br2==4) return "O"+won;
   }

  ///diagonal - main
   int br1=0,br2=0;
   for(int i=0;i<4;i++)
   {

       if(matrix[i][i]=='X') br1++;
       else if(matrix[i][i]=='O') br2++;
       else if(matrix[i][i]=='T') {br1++; br2++;}
     if(br1==4) return "X"+won;
     else if(br2==4) return "O"+won;
   }

    ///diagonal - secondary
    br1=0,br2=0;
   for(int i=0;i<4;i++)
   {
       if(matrix[i][3-i]=='X') br1++;
       else if(matrix[i][3-i]=='O') br2++;
       else if(matrix[i][3-i]=='T') {br1++; br2++;}
     if(br1==4) return "X"+won;
     else if(br2==4) return "O"+won;

   }
if (status==0) return draw;
else if(status==-1) return notc;
}
int main()
{
    char c;
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        scanf("%c",&c);
      cout<<"Case #"<<i<<": "<<solveGame()<<endl;
    }
return 0;
}
