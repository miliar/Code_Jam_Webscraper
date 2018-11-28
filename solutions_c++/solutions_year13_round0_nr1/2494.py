#include<iostream>
using namespace std;
#include<cstdio>
#include<vector>
#include<string>
#include<map>
vector<string> board;
map<char,int> mymap;
void initmap()
{
mymap['X']=0;
mymap['O']= 1;

}
int check()
{

for(int i =0;i<4;i++)
{
int j =0;
if(board[i][0] == '.')
   continue;
for(;j<3;j++)
{
if(board[i][j]!='.' && board[i][j+1]!='.' && (board[i][j]=='T'|| board[i][j+1]== 'T' || board[i][j+1]==board[i][j] ))
  continue;
 else 
  break;
}
if(j==3)
  {
   if(board[i][j] == 'T')
    return mymap[board[i][j-1]];
    else
    return mymap[board[i][j]];
  }
}

//check column

 for(int i =0;i<4;i++)
  {
   int j =0;
   if(board[0][i] == '.')
   continue;
  for(;j<3;j++)
   {
    if(board[j][i]!='.' && board[j+1][i] != '.' && (board[j][i] == 'T' || board[j+1][i] == 'T' ||(board[j+1][i] == board[j][i])))
      continue;
     else
     break;
    

    }
    if(j == 3)
      {
        if(board[j][i] == 'T')
          return mymap[board[j-1][i]];
         else
          return mymap[board[j][i]];

      }
}


 
int i =0;
if(board[0][0] !='.') {
 for(;i<3;i++)
    {
     if(board[i][i]!='.' && board[i+1][i+1]!='.' && (board[i][i]== board[i+1][i+1] || board[i][i]=='T' || board[i+1][i+1] == 'T'))
       continue;
else 
  break;
    }
   if(i==3) 
    {
    if(board[i][i] == 'T')
     return mymap[board[i-1][i-1]];
     else 
     return mymap[board[i][i]];

    }}

//check minor diagonal

   i =0;
  if(board[0][3] != '.')
    {
  for(;i<3;i++)
    {
      
     if(board[i][3-i]!='.' && board[i+1][3-i-1]!='.' &&(board[i][3-i] == board[i+1][3-i-1] ||board[i][3-i] == 'T' || board[i+1][3-i-1] == 'T'))
       continue;
     else
	break;
	

     }
     if(i==3)
      {
	if(board[i][0] == 'T')
          return mymap[board[i-1][1]];
         else
           return mymap[board[i][0]];

      }
}

//cehck draw
  
  for( i =0;i<4;i++)
   {
    int j;
    for(j=0;j<4;j++)
      if(board[i][j] == '.')
        break;
     if(j<4)
      return 3;
   }
  return -1;
}
int main()
{
initmap();
int test;
cin>>test;
int t =1;
while(t<=test)
{
board.clear(); 
string temp;
for(int i =0;i<4;i++)
{
cin >> temp;
board.push_back(temp);
}
int out = check();
cout << "Case #"<<t<<": ";
if(out == 0)
  cout << "X won"<<endl;
 else if(out == 1)
   cout << "O won"<<endl;
  else if (out == -1)
     cout << "Draw" <<endl;
   else
   cout <<"Game has not completed" << endl;
 t++;
}

return 0;
}
