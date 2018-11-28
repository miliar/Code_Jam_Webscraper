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

int n, m;
vector< int > v;
vector< int > u;
vector< int > poly;

inline bool isinside(vector<int> &poly, int u, int v)
{
  bool haveu = false;
  bool havev = false;
  int posu, posv;
  
  for (int i=0; i<poly.size(); i++)
  {
    haveu = haveu || (poly[i] == u);
    if (poly[i] == u)
      posu = i;
    havev = havev || (poly[i] == v);
    if (poly[i] == v)
      posv = i;
  }
  
  return haveu && havev && !(posu == (posv+1)%poly.size() || posv == (posu+1)%poly.size());
}

inline void split(vector<int> &poly, vector<int> &a, vector<int> &b, int u, int v)
{
  a.clear();
  b.clear();
  int upos = 0;
  int vpos = 0;
  
  for (int i=0; i<poly.size(); i++)
  {
    if (poly[i] == v)
      vpos = i;
    if (poly[i] == u)
      upos = i;
  }  
  
  //cerr << upos << ' ' << vpos << endl;

  int cur = upos;
  while (1)
  {
    a.push_back(poly[cur]);
    
    if (cur == vpos)
      break;
    
    cur = (cur+1)%poly.size();
  }
  
  cur = upos;
  while (1)
  {
    b.push_back(poly[cur]);
    
    if (cur == vpos)
      break;
    
    cur = (cur-1 + poly.size())%poly.size();
  }
}

vector< vector<int> > P;
vector< int > color;
vector< int > bestdraw;
int curcolors;
int bestans;

inline void check()
{
  if (curcolors < bestans)
    return;
  
  for (int j=0; j<P.size(); j++)
  {
    vector<bool> was(curcolors, false);
    for (int i=0; i<P[j].size(); i++)
      was[color[P[j][i]]] = true;
    
    for (int i=0; i<curcolors; i++)
      if (!was[i])
	return;
  }
  
  bestans = curcolors;
  bestdraw = color;
}

void Draw(int x)
{
  if (x == n)
  {
    check();
    return;
  }
  
  color[x] = curcolors++;
  Draw(x+1);
  curcolors--;
  
  for (color[x] = 0; color[x] < curcolors; color[x]++)
  {
    Draw(x+1);
  }
}

inline void solve(int testnum)
{
  //cerr << "fsdfsdfsdfsdf\n";
  cin >> n >> m;
  v.resize(m);
  u.resize(m);
  for (int i=0; i<m; i++)
  {
    cin >> v[i];
    v[i]--;
  }
  
  for (int i=0; i<m; i++)
  {
    cin >> u[i];
    u[i]--;
  }
    
    //cerr << "olololo\n";
  P.clear();
  P.push_back(vector<int>(n));
  for (int i=0; i<n; i++)
    P[0][i] = i;
  

  for (int i=0; i<m; i++)
    for (int j=0; j<P.size(); j++)
      if (isinside(P[j], v[i], u[i]))
      {
	vector<int> A, B;
	split(P[j], A, B, v[i], u[i]);
	P.erase(P.begin() + j);
	P.push_back(A);
	P.push_back(B);
      }
      
          //cerr << "AAAAAAAAAAAAA\n";

        
  curcolors = 0;
  color.resize(n);
  bestans = 1;
  bestdraw.assign(n, 0);

  
  Draw(0);
  
  cout << "Case #" << testnum + 1 << ": " << bestans << endl;
  for (int i=0; i<n; i++)
    cout << bestdraw[i] + 1 << ' ';
  cout << endl;
}

int main()
{
  int testnum;
  scanf("%d\n", &testnum);
  for (int i=0; i<testnum; i++)
    solve(i);
}