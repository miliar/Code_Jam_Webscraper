#include <set>
#include<iostream>
#include<math.h>
#include<string>
#include<string>
#include<cstdio>
#include <stdio.h>
#include <stdlib.h>
#include<vector>
#include<algorithm>
#include<fstream>
#include <sstream>
using namespace std;

int main() {
  freopen("C-small-attempt1.in", "rt", stdin);
  freopen("C-small1.out", "wt", stdout);
  string s;
  int n;
  cin>> n;
  for (int nn = 1; nn <= n; nn++) {
      cout << "Case #" << nn << ": ";
      int x,y,sum,res=0;
      cin>>y>>x;
      string s1,s2;
      while (x>y)
      {
        stringstream out;
        out << x;
        s1 = out.str();

        for(int i=1;i<s1.size();i++)
        {string temp="";
            temp = s1.substr(i) + s1.substr(0, i);
            sum=atoi(temp.c_str());
            if(sum<x && sum>=y)
            res++;
        }
        x--;
      }
      cout<<res<<endl;

  }
 return 0;
}
