#include <iostream>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <set>
#include <string>
#include <map>

using namespace std;

vector< string > p;

struct square
{
  double cmx, cmy, mass;
  
  square()
  {
    mass = 0;
  }
};

vector< vector< vector< square > > > S;
int maxsize = 1;
int r, c, d;

const double eps = 1e-7;

inline double myabs(double x)
{
  return (x<0?-x:x);
}

inline void Solve(int testnum)
{
  maxsize = 1;
  scanf("%d%d%d\n", &r, &c, &d);
  p.resize(r);
  for (int i=0; i<r; i++)
    getline(cin, p[i]);
  
  S.assign(r, vector< vector< square > >(c, vector< square >(min(r, c) + 1)));
  
  for (int i=0; i<r; i++)
    for (int j=0; j<c; j++)
    {
      S[i][j][1].cmx = i*1.0 + 0.5;
      S[i][j][1].cmy = j*1.0 + 0.5;
      S[i][j][1].mass = double(p[i][j] - '0') + 1;
    }
    
  for (int k=2; k<=min(r,c); k++)
    for (int x = 0; x <= r - k; x++)
      for (int y = 0; y <= c - k; y++)
      {
	S[x][y][k].cmx = S[x][y][k-1].cmx*S[x][y][k-1].mass
		   + S[x+1][y+1][k-1].cmx*S[x+1][y+1][k-1].mass
		   - S[x+1][y+1][k-2].cmx*S[x+1][y+1][k-2].mass
		   + S[x+k-1][y][1].cmx*S[x+k-1][y][1].mass
		   + S[x][y+k-1][1].cmx*S[x][y+k-1][1].mass;
		   
	S[x][y][k].cmy = S[x][y][k-1].cmy*S[x][y][k-1].mass
		   + S[x+1][y+1][k-1].cmy*S[x+1][y+1][k-1].mass
		   - S[x+1][y+1][k-2].cmy*S[x+1][y+1][k-2].mass
		   + S[x+k-1][y][1].cmy*S[x+k-1][y][1].mass
		   + S[x][y+k-1][1].cmy*S[x][y+k-1][1].mass;
		  
	S[x][y][k].mass = S[x][y][k-1].mass
		   + S[x+1][y+1][k-1].mass
		   - S[x+1][y+1][k-2].mass
		   + S[x+k-1][y][1].mass
		   + S[x][y+k-1][1].mass;
		   
	S[x][y][k].cmx /= S[x][y][k].mass;
	S[x][y][k].cmy /= S[x][y][k].mass;
	
	if (k < 3)
	  continue;
	
	double mass = S[x][y][k].mass
		    - S[x][y][1].mass
		    - S[x+k-1][y][1].mass
		    - S[x][y+k-1][1].mass
		    - S[x+k-1][y+k-1][1].mass;
		    
	double cmx =  S[x][y][k].cmx*S[x][y][k].mass
		    - S[x][y][1].cmx*S[x][y][1].mass
		    - S[x+k-1][y][1].cmx*S[x+k-1][y][1].mass
		    - S[x][y+k-1][1].cmx*S[x][y+k-1][1].mass
		    - S[x+k-1][y+k-1][1].cmx*S[x+k-1][y+k-1][1].mass;
		    
	cmx /= mass;
		    
	double cmy =  S[x][y][k].cmy*S[x][y][k].mass
		    - S[x][y][1].cmy*S[x][y][1].mass
		    - S[x+k-1][y][1].cmy*S[x+k-1][y][1].mass
		    - S[x][y+k-1][1].cmy*S[x][y+k-1][1].mass
		    - S[x+k-1][y+k-1][1].cmy*S[x+k-1][y+k-1][1].mass; 
	cmy /= mass;
	
	if (testnum == 17)
	  cerr << cmx << ' ' << cmy << endl;
		
	if ( myabs(cmx - (x+x+k)*1.0/2) <= eps && myabs(cmy - (y+y+k)*1.0/2) <= eps)
	{
	  maxsize = max(maxsize, k);
	}
      }
  
  cout << "Case #" << testnum+1 << ": ";
  if (maxsize < 3)
    cout << "IMPOSSIBLE\n";
  else
    cout << maxsize << endl;
};

int main()
{
  int kol;
  scanf("%d\n", &kol);
  for (int i=0; i<kol; i++)
    Solve(i);
}