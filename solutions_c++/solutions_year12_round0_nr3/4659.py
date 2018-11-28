//
//  110a.cpp
//  
//
//  Created by Michael Cheng on 2/29/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <algorithm>

using namespace std;

char diu(char i)
{
  string r="yhesocvxduiglbkrztnwjpfmaq";
  return (char)r[i-'a'];
}

bool diu(int m,int n)
{
  if (n<10)
    return 0;
  if (n<100)
  {
    if (n/10==m%10)
      if (n%10==m/10)
        return 1;
    return 0;
  }
  if (m%100*10+m/100==n)
    return 1;
  if (m%10*100+m/10==n)
    return 1;
  return 0;
}


int main()
{
  int n;
  cin>>n;
  for (int i=1;i<=n;i++)
  {
    cout<<"Case #"<<i<<": ";
    int a,b;
    cin>>a>>b;
    int z=0;
    for (int j=a;j<b;j++)
      for (int k=j+1;k<=b;k++)
        if (diu(j,k)){//cout<<j<<' '<<k<<endl;
          z++;}
    cout<<z<<endl;
  }
    
    return 0;
}