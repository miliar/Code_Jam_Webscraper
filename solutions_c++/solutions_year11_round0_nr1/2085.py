#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>

using namespace std;

//#define SMALL
#define LARGE

int main() {
#ifdef SMALL
  ifstream datain("A-small-attempt0.in");
  ofstream dataout("A-small-attempt0.out");
//  freopen("A-small-attempt0.in", "rt", stdin);
//  freopen("A-small.out", "wt", stdout);
#endif
#ifdef LARGE
  ifstream datain("A-large.in");
  ofstream dataout("A-large.out");
#endif
#ifdef SMALL
  int seq[15];
  int o[15];
  int b[15];
#endif
#ifdef LARGE
  int seq[110];
  int o[110];
  int b[110];
#endif
  int t, n;
  datain >> t;
  for (int ii=1; ii<=t; ii++)
  {
    datain >> n;
    char c;
    int m;
    int io=0,ib=0;
    for (int i=0; i<n; i++)
    {
      datain>>c>>m;
      if (c=='O')
      {
        seq[i]=0;
        o[io++]=m;
      }
      else if (c=='B')
      {
        seq[i]=1;
        b[ib++]=m;
      }
    }
    dataout<<"Case #"<<ii<<": ";
    int curo=1, curb=1, min=0, dest, preo=0,preb=0;
    int iio=0,iib=0;
    for (int i=0; i<n; i++)
    {
      int cur,pre;
      if(seq[i]==0)
      {
        dest=o[iio];
        cur=curo;
        curo=o[iio++];
        pre=preb;
        preb=0;
      }
      else
      {
        dest=b[iib];
        cur=curb;
        curb=b[iib++];
        pre=preo;
        preo=0;
      }
      int move = abs(dest-cur);
      int cost;
      if(move+1 > pre)
        cost = move+1-pre;
      else
        cost = 1;
      min += cost;
      if(seq[i]==0)
        preo+=cost;
      else
        preb+=cost;
    }
    dataout<<min<<endl;
  }
  return 0;
}
