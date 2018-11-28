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

int main()
{
  int n;
  cout.precision(10);
  cin>>n;
  for (int i=1;i<=n;i++)
  {
    cout<<"Case #"<<i<<":";
    int m;
    cin>>m;
    int a[m];
    for (int j=0;j<m;j++)
      cin>>a[j];
    
    int t=0;
    for (int j=0;j<m;j++)
      t+=a[j];
    
    int g=0;
    
    for (int j=0;j<m;j++)
    {
      double r=(t*2.0/m-a[j])*100/t;
      if (r<0) g++;
    }
    
    if (g==0)
    for (int j=0;j<m;j++)
    {
      double r=(t*2.0/m-a[j])*100/t;
      if (r>0) cout<<' '<<r;
      else cout<<" 0";
    }
    else
    {
      int tt=0;
      for (int j=0;j<m;j++)
      {
        double r=(t*2.0/m-a[j])*100/t;
        if (r>0) tt+=a[j];
      }
      for (int j=0;j<m;j++)
      {
        //cout<<t<<' '<<tt<<' '<<m<<' '<<g<<endl;
        double r=(t*2.0/m-a[j])*100/t;
        if (r<0) cout<<" 0";
        else
          //cout<<' '<<100.0/(m-g);
          //cout<<' '<<(t+tt)/(m-g)-a[j];
          cout<<' '<<((t+tt)*1.0/(m-g)-a[j])*100.0/t;
      }
    }
      
    cout<<endl;
  }
  return 0;
}