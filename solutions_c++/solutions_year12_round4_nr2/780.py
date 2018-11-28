#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <map>
#include <bitset>
#include <numeric> //accumulate

typedef double DL;
using namespace std;
const DL PI = 3.1415926;

struct point
{
  point(int i, DL _x, DL _y, DL _r)
    :id(i), x(_x), y(_y), r(_r) {}
  int id;
  DL x;
  DL y;
  DL r;
};

DL dist(point p1, point p2)
{
  return sqrt(pow(p1.x-p2.x, 2) + pow(p1.y-p2.y, 2));
}

bool comp(point p1, point p2)
{
  return p1.r>p2.r;
}

bool comp2(point p1, point p2)
{
  return p1.id < p2.id;
}

DL binSearch(point p1, point p2, double r, bool left)
{
  DL min = 0;
  DL max = PI;
  max = left?max:-max;
  while(fabs(min-max) > .0000001)
    {
      DL mid = (min + max) / 2;
      DL x = p1.x + (p1.r+r) * cos(mid);
      DL y = p1.y + (p1.r+r)*sin(mid);
      point temp(0, x, y, r);
      if(dist(temp, p2) > (p2.r+r))
	{max = mid; }
      else
	{min = mid; }
    }
  return (min+max)/2;
}

bool cut(point p1,point p2)
{
  if(dist(p1, p2) > (p1.r+p2.r))
    {return 0;}
  else
    {return 1;}
}

int main()
{
  int totCase;
  cin >> totCase;
  for(int i = 0; i < totCase; ++i)
    {
      cout << setprecision(6) << fixed << "Case #" << (i+1) << ": ";
      int num, wid, len;
      cin >> num >> wid >> len;
      if(num == 1)
	{
	  int temp;
	  cin >> temp;
	  cout << 0 << " " << 0 << endl; continue;
	}
      if(num == 2)
	{
	  int temp;
	  cin >> temp >> temp;
	  cout << 0 << " " << 0 << " " << wid << " " << len << endl; continue;
	}
      vector<point> points;
      for(int j = 0; j < num; ++j)
	{
	  int r;
	  cin >> r;
	  points.push_back(point(j,0,0,r));
	}
      sort(points.begin(), points.end(), comp);
      int curr = 1;
      for(; curr < num; ++curr)
	{
	  if(points[curr].r+points[curr-1].r + points[curr-1].x <= wid)
	    {
	      points[curr].x = points[curr-1].x+points[curr-1].r+points[curr].r;
	      points[curr].y = 0;
	      //cerr << points[curr].x << endl;
	    }
	  else
	    {break;}
	}
      bool cond = 0;
      if(points[curr].r+points[0].r + points[0].y <= len)
	    {
	      points[curr].y = points[0].r+points[curr].r;
	      points[curr].x = 0;
	      ++curr;
	      cond = 1;
	    }
      for(; cond && curr < num; ++curr)
	{
	  if(points[curr].r+points[curr-1].r + points[curr-1].y <= len)
	    {
	      points[curr].y = points[curr-1].y+points[curr-1].r+points[curr].r;
	      points[curr].x = 0;
	    }
	  else
	    {break;}
	}
      for(; curr < num; ++curr)
	{
	  DL xmin, ymin, xmax, ymax;
	  xmin = ymin = 0;
	  xmax = wid;
	  ymax = len;
	  DL xmid = (xmin+xmax)/2;
	  DL ymid = (ymin+ymax)/2;
	  int c = 0;
	  vector<point> cand;
	  for(int k = 0; k < points.size(); ++k)
	    {
	      if(cut(points[k], points[curr]))
		{
		  if(k != curr)
		    {
		      cand.push_back(points[k]);
		    }
		  ++c;
		}
	    }
	  if(c > 3)
	    {xmin = xmid; ymin = ymid;}
	  if(c < 3)
	    {xmax = xmid; ymax = ymid;}
	  if(c == 3)
	    {
	      DL temp1 = binSearch(cand[0], cand[1], points[curr].r, 0);
	      DL temp2 = binSearch(cand[0], cand[1], points[curr].r, 1);
	      DL rad = cand[0].r+points[curr].r;
	      if(cand[0].x+cos(temp1) > 0 && cand[0].x+cos(temp1) < wid && cand[0].y+sin(temp1)>0 && cand[0].y+sin(temp1)<len)
		{
		  points[curr].x=cand[0].x+cos(temp1);
		  points[curr].y=cand[0].y+sin(temp1);
		  continue;
		}
	      if(cand[0].x+cos(temp2) > 0 && cand[0].x+cos(temp2) < wid && cand[0].y+sin(temp2)>0 && cand[0].y+sin(temp2)<len)
		{
		  points[curr].x=cand[0].x+cos(temp2);
		  points[curr].y=cand[0].y+sin(temp2);
		  continue;
		}
	      cerr << "ERROR" << endl;
	    }
	}
      sort(points.begin(), points.end(), comp2); 
      for(int j = 0; j < points.size(); ++j)
	{cout << points[j].x << " " << points[j].y << " ";}
      cout << endl;
    }
}
