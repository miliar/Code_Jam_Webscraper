//
//  c.cpp
//  
//
//  Created by Michael Cheng on 5/5/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
  int nn;
  
  cin>>nn;
  for (int ii=1;ii<=nn;ii++)
  {
    int n,d;
    cin>>n;
        cout<<"Case #"<<ii<<": ";
    
    int w,l;
    cin>>w>>l;
    
    int r[n];
    int x=0,y=0,m=0;
    for (int i=0;i<n;i++)
      cin>>r[i];
    
    //sort(r,r+n);
    
    long long p[n],q[n];
    
    for (int i=0;i<n;i++)
    {
      cout<<' '<<x<<' '<<y;
      if (x>w)
        cout<<"diu\n";
      if (y>l)
        cout<<"diu\n";
      p[i]=x;
      q[i]=y;
      if (i<n-1)
        y+=r[i]+r[i+1];
        
      if (r[i]>m)
        m=r[i];
      
      if (y>l)
      {
        x+=m;
        y=0;
        m=0;
        int t=0;
        for (int j=i+1;j<n;j++)
        {
          if (r[j]>m)
            m=r[j];
          t+=r[j];
          if (t>l)
          {
            
            break;
          }
        }
        x+=m;//cout<<m
        if (x>w)
          cout<<"diu\n";
      }
      
    }
    
    cout<<endl;
    
  /* for (int i=0;i<n;i++)
      for (int j=i+1;j<n;j++)
      {
        double d=sqrt((q[j]-q[i])*(q[j]-q[i])+(p[j]-p[i])*(p[j]-p[i]));
        cout<<i<<' '<<j<<' '<<r[i]<<' '<<r[j]<<' ';
        cout<<p[i]<<' '<<q[i]<<' '<<p[j]<<' '<<q[j]<<' '<<d;
        cout<<' '<<r[i]+r[j]<<' ';
        if (d<r[i]+r[j])
          cout<<"DIU";
        cout<<endl;
      }*/
    
  }
  return 0;
}