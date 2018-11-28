#include <fstream>
#include <vector>
#include <utility>

using namespace std;

int c, n, t, m;
int milk[10], sol;
int a[10];
vector < pair <int, int> > ppl[100];

void recur( int v, int cnt )
{
  if (v == n)
    {
      if (sol>cnt)
	{
	  int i, j;
	  for (i=0; i<m; i++)
	    {
	      for (j=0; j<ppl[i].size(); j++)
		{
		  if (a[ppl[i][j].first-1] == ppl[i][j].second) break;
		}
	      if (j == ppl[i].size()) return;
	    }
	  sol = cnt;
	  for (i=0; i<n; i++) milk[i] = a[i];
	}
      return;
    }
  a[v] = 0; recur(v+1, cnt);
  a[v] = 1; recur(v+1, cnt+1);
}

int main()
{
  int i, j;
  ifstream in("b.in");
  ofstream out("b.out");
  in >> c;
  for (int loop = 1; loop<=c; loop++)
    {
      in >> n;
      sol = n+1;
      in >> m;
      for (i=0; i<m; i++)
	{
	  int x, y;
	  in >> t;
	  ppl[i].clear();
	  for (j=0; j<t; j++)
	    {
	      in >> x >> y;	      
	      ppl[i].push_back(make_pair(x, y));
	    }
	}
      recur(0, 0);
      out << "Case #" << loop << ":";
      if (sol <= n)
	{
	  for (i=0; i<n; i++)
	    out << ' ' << milk[i];	  
	  out << endl;
	}
      else out << " IMPOSSIBLE" << endl;      
    }

  in.close();
  out.close(); 
  return 0;
}
