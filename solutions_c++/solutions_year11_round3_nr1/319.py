#include<iostream>
#include<vector>
using namespace std;
int R,C,T;
string temp;
char map[51][51];

int main()
{
cin>>T;
bool find;
for(int q=0;q<T;q++)
{
cin>>R>>C;
find=true;
for(int i=0;i<R;i++)
{
 cin>>temp;
  for(int j=0;j<C;j++)
   map[i][j]=temp[j];
}

for(int i=0;i<R-1;i++)
{
 for(int j=0;j<C-1;j++)
 {
   if(map[i][j]=='#')
   {
     if(map[i+1][j]=='#' && map[i][j+1]=='#' && map[i+1][j+1]=='#')
     {
       map[i][j]='/';
       map[i+1][j]='\\';
       map[i][j+1]='\\';
       map[i+1][j+1]='/';  
     }
   }       
 }
}

for(int i=0;i<R;i++)
{
  for(int j=0;j<C;j++)
   if(map[i][j]=='#')
   {
    find=false;
    break;
   }
}



cout<<"Case #"<<q+1<<":"<<endl;
if(!find)
{
  cout<<"Impossible"<<endl;
}
else
{
for(int i=0;i<R;i++)
{

  for(int j=0;j<C;j++)
   cout<<map[i][j];
   cout<<endl;
}
}
}
return 0;
}
