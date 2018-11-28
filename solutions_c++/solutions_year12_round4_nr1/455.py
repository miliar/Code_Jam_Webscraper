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
  int nn;
  
  cin>>nn;
  for (int ii=1;ii<=nn;ii++)
  {
    int n,d;
    cin>>n;
    int a[n],b[n],p[n];
    for (int i=0;i<n;i++)
      cin>>a[i]>>b[i];
    cin>>d;
    bool z=0;
    
    for (int i=0;i<n;i++)
      p[i]=-1;
    p[0]=0;
    
    if (d<=a[0]+a[0])
      z=1;
    
    for (int i=1;i<n;i++)
      if (a[i]<=a[0]+a[0])
        p[i]=0;
    for (int i=1;i<n;i++){//cout<<i<<p[i]<<endl;
     // for (int j=i+1;j<n;j++)
        if (p[i]>=0)
        {
          
          int r=a[i]-a[p[i]];
          if (b[i]<r)
            r=b[i];
          cout<<i<<' '<<p[i]<<' '<<r<<endl;
          if (r+a[i]>=d)
          {
            z=1;
            break;
          }
          for (int j=i+1;j<n;j++)
            if (a[j]<=r+a[i])
              if (p[j]==-1)
              p[j]=i;
        }//cout<<i<<"d\n";
    
    }
    
    cout<<"Case #"<<ii<<": ";
    if (z)
      cout<<"YES";
    else cout<<"NO";
    cout<<endl;
  }
  return 0;
}