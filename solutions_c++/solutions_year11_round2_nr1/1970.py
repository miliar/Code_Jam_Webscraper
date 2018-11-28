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
  int n;
  cin>>n;
  count++;
  res.clear();
  string str;
  for(int i=0;i<n;i++)
  {
          cin>>str;
          res.push_back(str);
  }
  double owp[n];
  for(int i=0;i<n;i++)
  owp[i] = -1.0;
  
  double wp[n];
  for(int i=0;i<n;i++)
  wp[i] = -1.0;
  
  cout<<"Case #"<<count<<":"<<endl;
  for(int i=0;i<n;i++)
  {
          int tot = 0;
          int wins = 0;
          for(int j=0;j<n;j++)
          {if(res[i][j] == '1' || res[i][j] == '0')tot++;
          if(res[i][j] == '1')wins++;
          }
          double a = wins*1.0/tot;
          wp[i] = a;
          
          int total = 0;
          double a1 = 0.0;
          double b = 0.0;
          for(int j=0;j<n;j++)
          if(i!=j && res[i][j]!='.')
          {
                  total++;
                  tot = 0;
                  wins = 0;
                  for(int k=0;k<n;k++)
                  if(i!=k)
                  {
                          if(res[j][k] == '1' || res[j][k] == '0')tot++;
                          if(res[j][k] == '1')wins++;
                  }
                  a1 += wins*1.0/tot;
                  
          }
          b = a1*1.0/total;
          
          owp[i] = b;
            
  }
  
  double oowp[n];
  for(int i=0;i<n;i++)
  oowp[i] = -1.0;
  
  for(int i=0;i<n;i++)
  {
          double a2 = 0.0;
          int to = 0;
          for(int j=0;j<n;j++)
          if(i!=j && res[i][j]!='.')
          {
                  to++;
                  a2 += owp[j];
          }
          oowp[i] = a2*1.0/to;
  }
  for(int i=0;i<n;i++)
  {
          double ans = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
          cout<<ans<<endl;
  }
}
 return 0;
 }

