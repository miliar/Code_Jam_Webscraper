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



bool G[500][500];
int M[500][22];

int main()
{
  ifstream inp("C-large.in");
  ofstream out("C-large.out");

  string x = "welcome to code jam";
  map <char, string > X;

  X['e'] = "wmd";
  X['l'] = "e";
  X['c'] = "l ";
  X['o'] = "ct";
  X['m'] = "oa";
  X[' '] = "eo";
  X['t'] = " ";
  X['d'] = "o";
  X['j'] = " ";
  X['a'] = "j";
  X['w'] = "";



  inp>>n;
  For(tests,n)
  {
    out<<"Case #"<<tests+1<<": ";

    getline(inp,s);
    if (s=="") getline(inp,s);


    vector <int> M1(s.length() + 1), M2(s.length() + 1);
    For(i,s.length()+1)
      M2[i]=1;

    For(i,x.length())
    {
      M1=M2;
      M2[0]=0;
      For(j,s.length())
      {
        if (s[j]==x[i])
          M2[j+1] = (M2[j] + M1[j]) % 10000;
        else
          M2[j+1] = M2[j];
      }
    }


    int res = M2[s.length()];

    if (res<10)
      out<<"000";
    else 
      if (res<100)
        out<<"00";
      else 
      if (res<1000)
        out<<"0";
    out<<res<<endl;
  }

 
  return 0;
} 

