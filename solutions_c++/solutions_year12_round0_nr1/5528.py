#include<iostream>
#include<math.h>
#include<string>
#include<cstdio>
#include <stdio.h>
#include <stdlib.h>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;

int main() {
  freopen("A-small-attempt1.in", "rt", stdin);
  freopen("A-small1.out", "wt", stdout);
  int n;
  string s;
  cin>> n;
   getline(cin,s);
  for (int nn = 1; nn <= n; nn++) {
    cout << "Case #" << nn << ": ";
      string s, s1="";
      getline(cin,s);

      for(int i=0;i<s.size();i++)
      {
          if(s[i]=='e')
            s1+='o';
          if(s[i]=='j')
            s1+='u';
          if(s[i]=='p')
            s1+='r';
            if(s[i]=='m')
            s1+='l';
            if(s[i]=='y')
            s1+='a';
            if(s[i]=='s')
            s1+='n';
            if(s[i]=='l')
            s1+='g';
            if(s[i]=='c')
            s1+='e';
            if(s[i]=='k')
            s1+='i';
            if(s[i]=='d')
            s1+='s';
            if(s[i]=='x')
            s1+='m';
            if(s[i]=='v')
            s1+='p';
            if(s[i]=='n')
            s1+='b';
            if(s[i]=='r')
            s1+='t';
            if(s[i]=='i')
            s1+='d';
            if(s[i]=='b')
            s1+='h';
            if(s[i]=='t')
            s1+='w';
            if(s[i]=='h')
            s1+='x';
            if(s[i]=='a')
            s1+='y';
            if(s[i]=='w')
            s1+='f';
            if(s[i]=='f')
            s1+='c';
            if(s[i]=='z')
            s1+='q';
            if(s[i]=='o')
            s1+='k';
            if(s[i]=='g')
            s1+='v';
            if(s[i]=='q')
            s1+='z';
            if(s[i]=='u')
            s1+='j';
            if(s[i]==' ')
            s1+=s[i];
      }
      cout<<s1<<endl;
  }
 return 0;
}
