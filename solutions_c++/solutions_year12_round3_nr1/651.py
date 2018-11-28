//
//  c.cpp
//  
//
//  Created by Michael Cheng on 5/5/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main()
{
  int h,n,m,nn;
  
  cin>>nn;
  for (int ii=1;ii<=nn;ii++)
  {
    int n;
    cin>>n;
    int a[n][n];
    for (int i=0;i<n;i++)
      for (int j=0;j<n;j++)
        a[i][j]=0;
    for (int i=0;i<n;i++)
    {
      int m;
      cin>>m;
      for (int j=0;j<m;j++)
      {
        int t;
        cin>>t;
        a[i][t-1]=1;
      }
    }
    
    /*for (int i=0;i<n;i++){
      for (int j=0;j<n;j++)
        cout<<a[i][j]<<' ';
      cout<<endl;}  */
    
    for (int k=0;k<n;k++)
      for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
          a[i][j]=a[i][j]+a[i][k]*a[k][j];
    
   /* for (int i=0;i<n;i++){
        for (int j=0;j<n;j++)
          cout<<a[i][j]<<' ';
        cout<<endl;}*/
    
    bool z=0;
    for (int i=0;i<n;i++)
      for (int j=0;j<n;j++)
        if (a[i][j]>1)
          z=1;
    
    cout<<"Case #"<<ii<<": ";
    if (z)
      cout<<"Yes";
    else cout<<"No";
    cout<<endl;
  }
  return 0;
}