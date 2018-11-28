#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <utility>
#include <algorithm>

using namespace std;

bool flag[5];
int p[5];
int k;
int res;
string s;

int calc()
{
  string t = "";
  int i, j;
  for (i=0; i<s.size(); i+=k)
    for (j=0; j<k; j++)	
      t = t+s[i+p[j]];
  int ret = 1;
  char now = t[0];
  for (i=1; i<t.size(); i++)
    {
      if (now != t[i])
	{
	  ret ++;
	  now = t[i];
	}      
    }
  return ret;
}

void solve( int cnt )
{
  if (cnt == k)
    {
      res = min(res, calc());
      return;
    }
  for (int i=0; i<k; i++)
    if (!flag[i]) 
      {
	p[cnt] = i;
	flag[i] = true;
	solve(cnt+1);
	flag[i] = false;
      }
}

int main()
{
  ifstream in("d.in");
  ofstream out("d.out");
  int n;in >> n;
  for (int lp=1; lp<=n; lp++)
    {
      in >> k >> s;
      for (int i=0; i<k; i++) flag[i] = false;
      res = s.size();
      solve(0);
      out << "Case #" << lp << ": " << res << endl;
    }
  in.close();
  out.close(); 
  return 0;
}
