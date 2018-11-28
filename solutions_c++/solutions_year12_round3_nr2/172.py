//
//  c.cpp
//  
//
//  Created by Michael Cheng on 5/5/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <queue>

using namespace std;

int main()
{
  int h,n,m,nn;
  cout.precision(10);
  cout.setf(ios::fixed);
  cin>>nn;
  for (int ii=1;ii<=nn;ii++)
  {
     double d;
    int a,b;
    cin>>d>>a>>b;
    
    cout<<"Case #"<<ii<<": ";
    cout<<endl;
    
     double t[a],x[a];
    for (int i=0;i<a;i++)
      cin>>t[i]>>x[i];
    
    for (int i=0;i<b;i++)
    {
       double z;
      cin>>z;
      if (a==1)
        cout<<sqrt(2*d/z)<<endl;
      else
      {
        double xx=sqrt(2*d/z);
        double y=(x[1]-x[0])/(t[1]-t[0]);
        y=(d-x[0])/y;
        if (y>xx)
          xx=y;
        cout<<xx<<endl;
      }
    }
    
  }
  return 0;
}