//
//  c.cpp
//  
//
//  Created by Michael Cheng on 5/5/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;
bool u[2000000];
int a[20];
int zz;
bool d;


void dfs(int t,int lv,vector<int> z)
{
  //cout<<t<<' '<<lv<<endl;
  
  if (d) return;
  if (lv==20)
  {/*cout<<t<<endl;
    if (z.size()>0)
    cout<<z[0];
    for (int i=1;i<z.size();i++)
      cout<<' '<<z[i];
    cout<<endl;*/
    if (u[t])
    {
      zz=t;
      cout<<z[0];
      for (int i=1;i<z.size();i++)
        cout<<' '<<z[i];
      cout<<endl;
      d=1;
    }
    else
      u[t]=1;
    return;
  }
  dfs(t,lv+1,z);
  z.push_back(a[lv]);
  dfs(t+a[lv],lv+1,z);
}

void ddfs(int t,int lv,vector<int> z)
{
  if (d)
    return;
  if (lv==20)
  {
    if (t==zz)
    {
      cout<<z[0];
    for (int i=1;i<z.size();i++)
      cout<<' '<<z[i];
    cout<<endl;
      d=1;
    }
    return;
  }
  ddfs(t,lv+1,z);
  z.push_back(a[lv]);
  ddfs(t+a[lv],lv+1,z);
}

int main()
{
  int n;
  cin>>n;
  for (int i=1;i<=n;i++)
  {
    d=0;
    cout<<"Case #"<<i<<":\n";
    cin>>a[0];
    for (int j=0;j<20;j++)
      cin>>a[j];
    for (int j=0;j<2000000;j++)
      u[j]=0;
    vector<int> z;
    dfs(0,0,z);
    d=0;
    //cout<<zz<<endl;
    ddfs(0,0,z);
  }
  return 0;
}