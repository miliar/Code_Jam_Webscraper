#include "stdafx.h"

#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
#include <map>

//#define OMP

#ifdef OMP
#include <omp.h>
#endif

using namespace std;

ifstream fi;
ofstream fo;
typedef long long ull;

class Csolve
{
public:
  int t;
  int R, C;
  ull D;
  ull *dt;
  ull *xtbl;
  ull *ytbl;
  ull *dtbl;
  int ans;

  Csolve()
  {
	  dt = new ull[512*512];
	  xtbl = new ull[512*512];
	  ytbl = new ull[512*512];
	  dtbl = new ull[512*512];
  }
  ~Csolve()
  {
	  delete [] dt;
	  delete [] xtbl;
	  delete [] ytbl;
	  delete [] dtbl;
  }
  
  void solve()
  {
	  ans = -1;
	  memset(xtbl, 0, 512*512*sizeof(ull));
	  memset(ytbl, 0, 512*512*sizeof(ull));
	  memset(dtbl, 0, 512*512*sizeof(ull));
	  for (int x=0;x<=C;x++)
	  {
		  xtbl[x] = 0;
		  ytbl[x] = 0;
		  dtbl[x] = 0;
	  }
	  for (int y=1;y<=R;y++)
	  {
		  xtbl[(y<<9)] = 0;
		  ytbl[(y<<9)] = 0;
		  dtbl[(y<<9)] = 0;
		  ull sx = 0;
		  ull sy = 0;
		  ull sd = 0;
		  for (int x=0;x<=C-1;x++)
		  {
			  sx += (dt[x+((y-1)<<9)])*(x+1);
			  sy += (dt[x+((y-1)<<9)])*(y+1);
			  sd += (dt[x+((y-1)<<9)]);
			  xtbl[x+(y<<9)+1] = sx + xtbl[x+((y-1)<<9)+1];
			  ytbl[x+(y<<9)+1] = sy + ytbl[x+((y-1)<<9)+1];
			  dtbl[x+(y<<9)+1] = sd + dtbl[x+((y-1)<<9)+1];
		  }
	  }

	  int mx = min(R, C);
	  for (int y1=0;y1<R;y1++)
		  for (int x1=0;x1<C;x1++)
		  {
			  for (int k=mx-1;k>=2 && k>ans;k--)
			  {
				  int x2 = x1 + k;
				  int y2 = y1 + k;
				  if (x2<C && y2<R)
				  {
					  x2++; y2++;
					  ull pdx = xtbl[x2+(y2<<9)] + xtbl[x1+(y1<<9)] - xtbl[x1+(y2<<9)] - xtbl[x2+(y1<<9)];
					  ull pdy = ytbl[x2+(y2<<9)] + ytbl[x1+(y1<<9)] - ytbl[x1+(y2<<9)] - ytbl[x2+(y1<<9)];
					  ull cd = dtbl[x2+(y2<<9)] + dtbl[x1+(y1<<9)] - dtbl[x1+(y2<<9)] - dtbl[x2+(y1<<9)];
					  x2--; y2--;
					  ull area = (k+1)*(k+1);
					  double cx = 1.0 + (double)(x2+x1) * 0.5;
					  double cy = 1.0 + (double)(y2+y1) * 0.5;
					  double massx = (double)pdx - cx * cd;
					  double massy = (double)pdy - cy * cd;

					  massx = 0;
					  massy = 0;
					  for (int yy=y1;yy<=y2;yy++)
						  for (int xx=x1;xx<=x2;xx++)
						  {
							  massx += dt[xx+(yy<<9)] * (xx+1.0 - cx);
							  massy += dt[xx+(yy<<9)] * (yy+1.0 - cy);
						  }
					  

					  massx -= dt[x1+(y1<<9)]*(x1+1.0-cx);
					  massy -= dt[x1+(y1<<9)]*(y1+1.0-cy);
					  massx -= dt[x2+(y1<<9)]*(x2+1.0-cx);
					  massy -= dt[x2+(y1<<9)]*(y1+1.0-cy);
					  massx -= dt[x1+(y2<<9)]*(x1+1.0-cx);
					  massy -= dt[x1+(y2<<9)]*(y2+1.0-cy);
					  massx -= dt[x2+(y2<<9)]*(x2+1.0-cx);
					  massy -= dt[x2+(y2<<9)]*(y2+1.0-cy);
					  if (fabs(massx)<0.000000001 && fabs(massy)<0.000000001)
					  {
						  ans = max(ans, k);
						  //cout << ans << endl;
					  }
				  }
			  }
		  }



  }
  
  void readInput(int _t)
  {
	  memset(dt, 0, 512*512*sizeof(ull));
	  ans = -1;
    t = _t;
	fi >> R >> C >> D;
	char ch;
	for (int i=0;i<R;i++)
	{
		for (int x=0;x<C;x++)
		{
			fi >> ch;
			ull v = D + (ch-'0');
			dt[x+(i<<9)] = v;
		}
	}
  }
  
  void writeOutput()
  {
    fo << "Case #" << (t+1) << ": ";
	ans++;
	if (ans<3)
		fo << "IMPOSSIBLE";
	else 
		fo << ans;
    fo << endl;
  }
};


int main(int argc, char *argv[])
{
  //fi.open("test.in");  fo.open("test.out");
  fi.open("B0.in");  fo.open("B0.out");
  //fi.open("B1.in");  fo.open("B1.out");
   
  //Csolve solv[8];
  int T;
  fi >> T;
  int si = 0;
  for (int i=0;i<T;i++)
  {
	  Csolve solv;
      solv.readInput(i);
      solv.solve();
	  solv.writeOutput();
  }      
  
  fo.close();
  fi.close();


 return 0;
}

