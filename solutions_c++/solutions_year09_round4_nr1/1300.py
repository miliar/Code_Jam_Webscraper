

#include <iostream>
#include <vector>
#include <boost/dynamic_bitset.hpp>
#include <queue>
#include <map>
#include <utility>

using namespace std;
using namespace boost;

int doit();

int main(int,char**)
{
  int N=0;
  cin >> N;

  for(int n=0;n<N;++n)
    cout << "Case #" << (n+1) << ": " << doit() << '\n';

  return 0;
}

typedef unsigned long long row_type;
typedef vector<int> point;

int estimate(const point& p,int N)
{
  int res = 0;
  for(int i=0;i<N;++i)
    res += max(0,p[i]-i);
  return res;
}

void dump(point& p,int N)
{
  for(int i=0;i<N;++i)
    cout << p[i]<<'\n';
  cout << "\n";
}


int doit()
{
  int N;
  cin >> N;

  point start;

  for(int j=0;j<N;++j)
  {
    row_type row = 0;
    for(int i=0;i<N;++i)
    {
      char c;
      cin >> c;
      row = (row<<1) | ((c=='1')?1:0);
    }

    for(int k=0;k<N;++k)
    {
      const row_type mask = ~((~0)<<N);
      if(!(row&(mask>>(k+1))))
      {
	start.push_back(k);
	break;
      }
    }
  }

  priority_queue<pair<int,point> > open;
  map<point,int> closed;

  open.push(make_pair(-estimate(start,N),start));
  while(!open.empty())
  {
    int e = -open.top().first;
    point p = open.top().second;
    open.pop();

    int pe = estimate(p,N);
    int d = e-pe;
    if(pe==0)
      return d;

    //cout << "d=" << d << '\n';
    //dump(p,N);

    {
      map<point,int>::iterator itr = closed.find(p);
      if(itr!=closed.end() && itr->second<=e)
	continue;

      closed[p] = e;
    }

    for(int i=1;i<N;++i)
    {
      point adj = p;
      swap(adj[i],adj[i-1]);
      open.push(make_pair(-(d+1+estimate(adj,N)),adj));
      //dump(adj,N);
    }
  }

  return -1;
}
