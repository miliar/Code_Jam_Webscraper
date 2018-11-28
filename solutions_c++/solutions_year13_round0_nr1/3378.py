//"Tic-Tac-Toe-Tomek" by Shintero
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

int N, i;
char TAB[4][4];

int play()
{
int count_X=0, count_O=0, count_T=0, empty=0, a, b;
//Wiersze
for(a=0; a<4; a++)
  {for(b=0; b<4; b++)
     {if(TAB[a][b]=='X')
        count_X++;
     if(TAB[a][b]=='O')
        count_O++;
     if(TAB[a][b]=='T')
        count_T++;
     if(TAB[a][b]=='.')
        empty++;}
  if(count_O + count_T>=4)
     return 2;
  if(count_X + count_T>=4)
     return 1;
  count_X=count_O=count_T=0;
  }
count_X = count_O = count_T = 0;
//Kolumny
for(a=0; a<4; a++)
  {for(b=0; b<4; b++)
     {if(TAB[b][a]=='X')
        count_X++;
     if(TAB[b][a]=='O')
        count_O++;
     if(TAB[b][a]=='T')
        count_T++;
     if(TAB[b][a]=='.')
        empty++;}
  if(count_O + count_T>=4)
     return 2;
  if(count_X + count_T>=4)
     return 1;
  count_X=count_O=count_T=0;
  }
count_X=count_O=count_T=0;
//Skos Lewa-Prawa
for(a=0; a<4; a++)
   {if(TAB[a][a]=='X')
      count_X++;
   if(TAB[a][a]=='O')
      count_O++;
   if(TAB[a][a]=='T')
      count_T++;}
if(count_O + count_T>=4)
     return 2;
if(count_X + count_T>=4)
     return 1;
count_X=count_O=count_T=0;
//Skos Prawa-Lewa
b=3;
   for(a=0; a<4; a++)
      {if(TAB[a][b]=='X')
        count_X++;
     if(TAB[a][b]=='O')
        count_O++;
     if(TAB[a][b]=='T')
        count_T++;
      b--;}
if(count_O + count_T>=4)
     return 2;
if(count_X + count_T>=4)
     return 1;
if(empty>0)
   return -1;
return 0;
}

void game()
{
int state;
state=play();
if(state==-1)
   cout << "Case #" << i << ": Game has not completed" << endl; 
else if(state==0)
   cout << "Case #" << i << ": Draw" << endl; 
else if(state==1)
   cout << "Case #" << i << ": X won" << endl; 
else if(state==2)
   cout << "Case #" << i << ": O won" << endl; 
}

int main()
{
ios_base::sync_with_stdio(0);
cin >> N;
for(i=1; i<=N; i++)
   {cin >> TAB[0][0] >> TAB[0][1] >> TAB[0][2] >> TAB[0][3];
   cin >> TAB[1][0] >> TAB[1][1] >> TAB[1][2] >> TAB[1][3];
   cin >> TAB[2][0] >> TAB[2][1] >> TAB[2][2] >> TAB[2][3];
   cin >> TAB[3][0] >> TAB[3][1] >> TAB[3][2] >> TAB[3][3];
   game();}
return 0;   
}
