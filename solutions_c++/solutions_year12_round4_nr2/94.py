#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>

using namespace std;

vector< int > xans;
vector< int > yans;
int n, w, l;

vector< pair<int, int> > r;


struct node
{
  long long x, y;
  long long r;
  
  node(long long _x, long long _y, long long _r)
  {
    x = _x;
    y = _y;
    r = _r;
  }
};

inline bool haveInter(const node &a, const node &b)
{
  return (a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y) < (a.r+b.r)*(a.r+b.r);
}

inline void solve(int testnum)
{
  scanf("%d%d%d", &n, &w, &l);
  r.resize(n);
  xans.resize(n);
  yans.resize(n);
  
  for (int i = 0; i < n; i++)
    scanf("%d", &r[i].first), r[i].second = i;
  
  sort(r.rbegin(), r.rend());
  
  for (int i = 0; i < r.size(); i++)
  {
    node mynode(0, 0, r[i].first);
    int id = r[i].second;
    
    long long step = 1<<30;
    while (step > 0)
    {
      mynode.x+=step;
      bool good = true;
      
      if (mynode.x > w)
	good = false;
      
      for (int j= 0; j < i && good; j++)
	if (haveInter(mynode, node(xans[r[j].second], yans[r[j].second], r[j].first)))
	  good = false;
	
      if (!good)
      {
	mynode.x-= step;
	step/=2;
      }
    }
    
    step = 1<<30;
    while (step > 0)
    {
      mynode.y+=step;
      bool good = true;
      
      if (mynode.y > l)
	good = false;
      
      for (int j= 0; j < i && good; j++)
	if (haveInter(mynode, node(xans[r[j].second], yans[r[j].second], r[j].first)))
	  good = false;
	
      if (!good)
      {
	mynode.y-= step;
	step/=2;
      }
    }
    
    xans[id] = mynode.x;
    yans[id] = mynode.y;
  }
  
  printf("Case #%d: ", testnum+1);
  for (int i = 0; i < n; i++)
    printf("%d %d ", xans[i], yans[i]);
  printf("\n");
}

int main()
{
  int testkol;
  scanf("%d\n", &testkol);
  for (int i = 0; i < testkol; i++)
    solve(i);
}