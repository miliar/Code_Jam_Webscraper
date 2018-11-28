#include <functional>
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <deque>
#include <memory.h>
#include <set>
#include <list>
#include <sstream>
#include <math.h> 
#include <vector>
#include <queue>
#include <cassert>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

typedef long long int64;


int i,j,k1,k2,tests,t,ii,jj,p,newp,v,i1,n,m,a,b,l,d;

string s;

#define eps 1e-8
#define For(i,n) for (i=0;i<n;i++) 



set<string> Initial, Work, Work2;


int main()
{
  ifstream inp("A-large.in");
  ofstream out("A-large.out");

  inp>>l>>d>>n;
  For(i,d){
    inp>>s;
    Initial.insert(s);
  }

  For(i,n)
  {
    Work = Initial;
    out<<"Case #"<<i+1<<": ";
    inp>>s;

    int state=1, num = 0;
    set<char> Chars;
    For(j,s.length())
    {
      if (state==1)
        if (s[j]=='(')
          state=2;
        else
          Chars.insert(s[j]);
      else
        if (s[j]==')')
          state=1;
        else
          Chars.insert(s[j]);

      if (state==1)
      {
        set<string>::iterator it = Work.begin();
        set<string>::iterator it2;
        Work2.clear();
        while (it!=Work.end())
        {
          char c = (*it)[num];
          if  ( Chars.find(c)!=Chars.end()){
            Work2.insert(*it);
          }
          it++;
        }
        Chars.clear();
        num++;
        Work=Work2;
      }
    }

    out<<Work.size()<<endl;
  }

  return 0;
} 

