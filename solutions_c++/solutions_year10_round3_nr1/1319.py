#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <iterator>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <queue>
#include <vector>
using namespace std;
 
typedef long long LL;
 
#define MP make_pair
#define ST first
#define ND second
#define ALL(k) k.begin(),k.end()
#define PB push_back
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOREACH(i,v) for(__typeof((v).begin())i=(v).begin();i!=v.end();++(i))
#define SZ(a) (int)((a).size())

class fig
{
  public:
  int x1,x2,y1,y2;
  fig(int _x1, int _y1, int _x2, int _y2):x1(_x1),y1(_y1),x2(_x2),y2(_y2) {; }
};

int det(int x1, int y1, int x2, int y2)
{
  return x1*y2 - x2*y1;
}

int direction(int xi1, int xi2, int xj1, int xj2, int xk1, int xk2)
{
  return det(xk1-xi1,xk2-xi2 ,xj1-xi1, xj2 -xi2 );
}

bool onsegment(pair<int,int> pi, pair <int,int> pj, pair<int,int> pk)
{
  if(min(pi.ST,pj.ST) <= pk.ST && pk.ST <= max(pi.ST,pj.ST) && min(pi.ND,pj.ND) <= pk.ND && pk.ND <= max(pi.ND,pj.ND))
  	return true;
  return false;
}

bool intersect(pair <int, int > p1, pair <int,int> p2, pair <int,int> p3, pair<int,int> p4)
{
  int d1 = direction(p3.ST,p3.ND,p4.ST,p4.ND,p1.ST,p1.ND );
  int d2 = direction(p3.ST,p3.ND,p4.ST,p4.ND,p2.ST,p2.ND );
  int d3 = direction(p1.ST,p1.ND,p2.ST,p2.ND,p3.ST,p3.ND );
  int d4 = direction(p1.ST,p1.ND,p2.ST,p2.ND,p4.ST,p4.ND );
  if(((d1 > 0 && d2 <0) || (d1 < 0 && d2 > 0)) && 
     (( d3 > 0 && d4 < 0) || ( d3 < 0 && d4 > 0 )) )
     return true;
  else if( d1 == 0 && onsegment(p3,p4,p1)) return true;
  else if(d2 == 0 && onsegment(p3,p4,p2)) return true;
  else if(d3 == 0 && onsegment(p1,p2,p3)) return true;
  else if(d4 == 0 && onsegment(p1,p2,p4)) return true;
  return false;
}



int main()
{
  int tst,tstn;
  cin >> tstn;
  REP(tst,tstn)
  {
    cout << "Case #" << tst+1 << ": ";
    int n;
    cin >> n;
    vector < pair<int, int> > P(n);
    REP(i,n) { cin >> P[i].ST >> P[i].ND; }
    int intersects = 0;
    for(int i=0;i<n;i++)
    {
      for(int j=i+1;j<n;j++)
      {
        if( intersect(MP(P[i].ST,0), MP(P[i].ND,1), MP(P[j].ST,0), MP(P[j].ND,1)))
          intersects++;
      }
    }
    cout << intersects << endl;
    
  }
  return 0;
}
