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

int main()
{
  int n;
  cin>>n;
  n=1;
  string a;
  getline(cin,a);
  while (getline(cin,a))
  {
    cout<<"Case #"<<n++<<": ";
    for (int i=0;i<a.size();i++)
      if (a[i]==' ')
        cout<<' ';
    else
      cout<<diu(a[i]);
    cout<<endl;
  }
  return 0;
}