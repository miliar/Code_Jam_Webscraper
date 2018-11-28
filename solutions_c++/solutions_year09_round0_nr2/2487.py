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
typedef struct DOT_INFO
{
  int x;
  int y;
} dot;



vector <dot> around(int j, int k, int h, int w)
{
  vector <dot> vd;
  if((j-1)>=0) { dot td; td.x=j-1; td.y=k; vd.PB(td); }
  if((k-1)>=0) { dot td; td.x=j; td.y=k-1; vd.PB(td); }
  if((k+1)<w) { dot td; td.x=j; td.y=k+1; vd.PB(td); }
  if((j+1)<h) { dot td; td.x=j+1; td.y=k; vd.PB(td); }
  return vd;
}

dot down(vector<VI> alt, int j, int k, int h, int w)
{
  int tj=j,tk=k;
  int ta=alt[tj][tk];
  int m;
  vector <dot> vd;
  vd=around(tj,tk,h,w);
  REP(m,vd.size())
  {
    if(alt[vd[m].x][vd[m].y]<ta) 
    { tj=vd[m].x; tk=vd[m].y; ta=alt[vd[m].x][vd[m].y]; }
  }
  dot td;
  td.x=tj; td.y=tk;
  return td;
}

void label(vector<VI> alt, int** bas, int initj, int initk, int h, int w, int basidx, vector < vector<dot> > downlist)
{
  int m,n,o;
  //down;
  int j=initj,k=initk;
  while(1)
  {
    bas[j][k]=basidx;
    //dot td=down(alt,j,k,h,w);
    dot td=downlist[j][k];
    if(td.x==j && td.y==k) break;
    j=td.x; k=td.y;
  }
  //cout<<"down: "<<j<<","<<k<<endl;
  //up;
  vector <dot> dots;
  dot td1; td1.x=j; td1.y=k; dots.PB(td1);
  while(dots.size()!=0)
  {
    int x=dots[0].x;
    int y=dots[0].y;
    vector <dot> dots2;
    dots2=around(x,y,h,w);

    //cout<<"(";
    //REP(o,dots.size()) { cout<<dots[o].x<<","<<dots[o].y<<" ";  }
    //cout<<")"<<endl;

    REP(n,dots2.size())
    {
      if(bas[dots2[n].x][dots2[n].y]!=0 && bas[dots2[n].x][dots2[n].y]!=basidx) continue;
      //dot td2=down(alt,dots2[n].x,dots2[n].y,h,w);
      dot td2=downlist[dots2[n].x][dots2[n].y];
      if(td2.x==x && td2.y==y) {
        bas[dots2[n].x][dots2[n].y]=basidx;
        dot td; td.x=dots2[n].x; td.y=dots2[n].y;
        dots.PB(td);
      }
    } 
    //REP(o,dots.size()) { cout<<dots[o].x<<","<<dots[o].y<<" ";  }
    //cout<<endl;
    dots.erase(dots.begin());
  }
}

int main(int argc, char** argv)
{
  int i,j,k;
  ifstream in(argv[1]);
  ofstream out(argv[2]);
  int t;
  in>>t;
  REP(i,t)
  {
    vector<VI> alt;
    vector < vector <dot> > downlist;
    int h,w;
    in>>h;in>>w;
    REP(j,h)
    {
      VI tvi;
      REP(k,w)
      {
        int ti;
        in>>ti;
        tvi.PB(ti);
      }
      alt.PB(tvi);
    }

    int** bas=new int* [h];
    REP(j,h) { 
      bas[j]=new int [w];
      REP(k,w) bas[j][k]=0;
    }

    REP(j,h)
    {
      vector <dot> vd;
      REP(k,w)
      {
        dot td=down(alt,j,k,h,w);
        vd.PB(td);
        //cout<<j<<","<<k<<"="<<td.x<<","<<td.y<<endl;
      }
      downlist.PB(vd);
    }

    int basidx=1;
    REP(j,h)
      REP(k,w)
      {
        if(bas[j][k]==0) 
        {  
          label(alt,bas,j,k,h,w,basidx,downlist);
          basidx++;
        }
      }

    out<<"Case #"<<(i+1)<<":"<<endl;
    REP(j,h)
    {
      REP(k,w-1)
      {
        out<<char(96+bas[j][k])<<" ";
      }
      out<<char(96+bas[j][w-1])<<endl;
    }

    REP(j,h) delete [] bas[j];
    delete [] bas;
  }
  in.close();
  out.close();
  return 0;
}
