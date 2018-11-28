#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

void count(vector < VI > idx, int si, int vi, int &num, int last)
{
  int i,j,k;
  if(vi==idx.size()) {
    num++;
    if(num==10000) num=0;
    return;
  }
  REP(i,idx[vi].size())
  {
    if(idx[vi][i]>si && (idx.size()-vi)<=(last-si))
      count(idx,idx[vi][i],vi+1,num,last);  
  }
}

int main(int argc, char** argv)
{
  int x,y,z;
  ifstream in(argv[1]);
  ofstream out(argv[2]);
  int n;
  in>>n;
  string str;
  getline(in,str);
  REP(x,n)
  {
    getline(in,str);
    int sl=str.length()-1;
    FORD(y,sl,0) 
    {
      if(str[y]!='w' 
          && str[y]!='e'
          && str[y]!='l'
          && str[y]!='c'
          && str[y]!='o'
          && str[y]!='m'
          && str[y]!=' '
          && str[y]!='t'
          && str[y]!='d'
          && str[y]!='j'
          && str[y]!='a') str.erase(y,1);
    }
    vector <VI> idx;
    VI w,e,l,c,o,m,bl,t,d,j,a;
    REP(y,str.length()) 
    {
      if(str[y]=='w') w.PB(y);
      else if(str[y]=='e') e.PB(y);
      else if(str[y]=='l') l.PB(y);
      else if(str[y]=='c') c.PB(y);
      else if(str[y]=='o') o.PB(y);
      else if(str[y]=='m') m.PB(y);
      else if(str[y]==' ') bl.PB(y);
      else if(str[y]=='t') t.PB(y);
      else if(str[y]=='d') d.PB(y);
      else if(str[y]=='j') j.PB(y);
      else if(str[y]=='a') a.PB(y);
    }
    idx.PB(w);
    idx.PB(e);
    idx.PB(l);
    idx.PB(c);
    idx.PB(o);
    idx.PB(m);
    idx.PB(e);
    idx.PB(bl);
    idx.PB(t);
    idx.PB(o);
    idx.PB(bl);
    idx.PB(c);
    idx.PB(o);
    idx.PB(d);
    idx.PB(e);
    idx.PB(bl);
    idx.PB(j);
    idx.PB(a);
    idx.PB(m);

    /*REP(y,idx.size())
    {
      REP(z,idx[y].size()) cout<<idx[y][z]<<" ";
      cout<<endl;
    }*/

    int num=0;
    int last=idx[5][idx[5].size()-1];
    count(idx,-1,0,num,last);

    out<<"Case #"<<(x+1)<<": ";
    out << setfill('0');
    out << setw(4) << num << endl;
  }
  in.close();
  out.close();
  return 0;
}
