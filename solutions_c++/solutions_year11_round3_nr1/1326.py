 #include<iostream>
#include<vector>
#include<string>
#define pb push_back
#define mp make_pair
using namespace std;
bool vald(int i,int j,int r, int c)
{
   if(i<r && j<c) return true;
   return false; 
}
int main()
{
  int nt;
  cin>>nt;
  for(int cas=0;cas<nt;cas++)
  {
    int r,c;
    cin>>r>>c;
    vector<string> grid;
    string str;
    for(int i=0;i<r;i++)
    {
         cin>>str;
         grid.pb(str);
    }
    bool possib=true;
    bool ex=false;
    for(int i=0;i<r;i++)
    {
      for(int j=0;j<c;j++)
      {
        possib=true;
        if(grid[i][j]=='#')
        {
           possib=false;
           if(vald(i,j+1,r,c) && grid[i][j+1]=='#')
             if(vald(i+1,j,r,c) && grid[i+1][j]=='#')
              if(vald(i+1,j+1,r,c) && grid[i+1][j+1]=='#')
                possib=true;
            if(possib)
            {
              grid[i][j]='/';
              grid[i][j+1]='\\';
              grid[i+1][j]='\\';
              grid[i+1][j+1]='/';
              
            }else{ ex=true; break; }
        }
      }
      if(ex) break;
    }

   cout<<"Case #"<<(cas+1)<<":"<<endl;
   if(ex) cout<<"Impossible"<<endl;
   else
   {
    for(int i=0;i<r;i++)
     cout<<grid[i]<<endl;
   }
     
  }
  return 0;
}
