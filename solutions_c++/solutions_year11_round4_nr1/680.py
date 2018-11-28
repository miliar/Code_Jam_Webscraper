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

double s, x, r, t;
int n;
double total;
vector< double > len;
vector< double > w;
vector< bool > used;
double totallen;

inline void Solve(int testnum)
{
  cin >> x >> s >> r >> t >> n;

  len.resize(n + 1);
  w.resize(n + 1);
  used.assign(n + 1, false);  
  
  totallen = 0;
  total = 0;

  for (int i=0; i<n; i++)
  {
    double b, e;
    cin >> b >> e;
    len[i] = e - b;
    totallen += len[i];
    cin >> w[i];
    w[i] += s;
  }
  
  len[n] = x - totallen;
  w[n] =  s;
  
  for (int qw=0; qw<n+1; qw++)
  {
    int cur = -1;
    double mins = 1000;
    for (int i=0; i<n+1; i++)
      if (!used[i] && w[i] < mins)
	mins = w[i], cur = i;
      
    used[cur] = true;
    int i = cur;
    
    double needtime = len[i] / (w[i] + r - s);
    
    if (needtime <= t)
    {
      t -= needtime;
      total += needtime;
    }
    else
    {  
      double gorun = t * (w[i] + r - s);
      t = 0;
      total += gorun / (w[i] + r - s) + (len[i] - gorun) / (w[i]);
    }
  }
  
  cout.precision(30);
  cout.setf(ios::fixed);
  cout << "Case #" << testnum+1 <<": " << total << endl;
}

int main()
{
  int kol;
  scanf("%d\n", &kol);
  for (int i=0; i<kol; i++)
    Solve(i);
}