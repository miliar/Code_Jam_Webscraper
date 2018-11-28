#include<cstdio>
#include<iostream>
#include<cmath>
#include<stack>
#include<queue>
#include<string>
#include<cstring>
#include<sstream>
#include<vector>
#include<utility>
#include<map>
#include<cstdlib>
#include<limits.h>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
 int t,count=0;
 freopen("A-large.in","r",stdin);
 freopen("output.out","w",stdout);
 cin>>t;
 vector <string> res;
 
 while(t--)
 {
  int r,c;
  cin>>r>>c;
  count++;
  bool visit[r][c];
  int i,j;
  res.clear();
  
  string str;
  for(i=0;i<r;i++)
  {
          cin>>str;
          res.push_back(str);
  }
  for(i=0;i<r;i++)
  for(j=0;j<c;j++)
  visit[i][j] = false;
  
  int flag = 0;
  for(i=0;i<r;i++)
  for(j=0;j<c;j++)
  {
                  if(res[i][j] == '#')
                  if(i+1 < r && res[i+1][j] == '#' && 
                  j+1 < c && res[i][j+1] == '#' &&
                  i+1 < r && j+1 < c && res[i+1][j+1] == '#')
                  {
                         res[i][j] = '/';
                         res[i+1][j] = '\\';
                         res[i][j+1] = '\\';
                         res[i+1][j+1] = '/';
                  }
                  else
                  {
                      flag = 1;
                      break;
                  }
  }
  if(flag == 1)
  {cout<<"Case #"<<count<<":\n"<<"Impossible\n";continue;}
  
  cout<<"Case #"<<count<<":\n";
  for(i=0;i<r;i++)
  {
                  for(j=0;j<c;j++)
                  cout<<res[i][j];
                  cout<<endl;
  }
  }
 return 0;
 }

