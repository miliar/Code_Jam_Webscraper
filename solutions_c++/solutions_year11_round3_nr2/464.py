#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int L, t, n, C;
long long c[1001000];
long long distances[1001000], br;

bool cmp (int p1, int p2)
{
  return p1 > p2;
}
void solve ()
{
  
  scanf ("%d%d%d%d\n", &L, &t, &n, &C);
  br = 0;
  int i, j, k;
  
  for (i =0; i < C; i ++)
    scanf ("%lld", &c[i]);
  t/=2;
  long long cur = 0;
  long long res = 0;
  for (i = 0; i < n; i ++)
  {
    long long tonext = c[i%C];
    //cout << tonext <<" " ;
    if (cur + tonext >= t)
    {
      if (cur < t)
	distances[br++] = cur + tonext - t;
      else
	distances[br++] = tonext;
    }
    cur += tonext;
    res += 2*tonext;
  }
 // cout << endl;
  
  sort (distances, distances + br, cmp);
  
 // for (i = 0 ; i < br; i ++)
 // cout << distances[i] << " ";
 // cout << endl;
  
  for (i = 0 ; i < L && i < br; i ++)
    res -= distances[i];
  
  printf ("%lld\n", res);
    
}

int main ()
{
  int t; 
  scanf ("%d", &t);
  
  for (int i = 1; i <=t; i ++)
  {
    printf ("Case #%d: ", i);
    solve ();
  }
  
  
  return 0;
}