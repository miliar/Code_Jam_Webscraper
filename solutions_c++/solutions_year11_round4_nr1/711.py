#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

double m, speed, rSpeed;
int t, n;
pair <pair <double, double>, double> a[1024];
double leftt; 

double magic (double dist, double someSpeed)
{
  double est_time = dist/ (someSpeed + rSpeed);
  
  if (leftt < est_time)
  {
    est_time = leftt;
    leftt -= est_time;
    dist -= est_time * (someSpeed + rSpeed);
    return est_time + dist/(someSpeed + speed);
    
  }
  else
  {
    leftt -= est_time;
    return est_time;
  }
    
  return 0.0;
  
}
bool cmp2 (pair <pair <double, double>, double> p1, pair <pair <double, double>, double> p2)
{
  return p1.second < p2.second;
  
}
void solve ()
{
  scanf ("%lf%lf%lf%d%d", &m, &speed, &rSpeed, &t, &n);
  int i;
  for (i = 0; i < n; i ++)
  {
    scanf ("%lf%lf%lf", &a[i].first.first, &a[i].first.second, &a[i].second);
  }
  
  sort (a, a + n);
  
  //double now = 0; 
  leftt = t;
  double res = 0.0;
  
  res += magic (a[0].first.first, 0);
  res += magic (m - a[n-1].first.second, 0);
  for (i =1; i < n; i ++)
    res += magic (a[i].first.first - a[i-1].first.second, 0);
  
  sort (a, a+ n, cmp2);
  
  for (i =0; i < n; i ++)
    res += magic (a[i].first.second - a[i].first.first, a[i].second);
  
    
  
  /*
  for (i = 0; i < n; i ++)
  {
    //cout << a[i].first.first << " " << a[i].first.second<< endl;
    res += magic (a[i].first.first - now, 0);
    res += magic (a[i].first.second - a[i].first.first, a[i].second);
    now = a[i].first.second; 
  }
  res += magic (m - now, 0);
  
  */
    
    printf ("%.9lf\n", res);
  
}
int main ()
{
  
  int T;
  scanf ("%d", &T);
  
  for (int i = 1; i <=T; i++)
  {
    printf ("Case #%d: ", i);
    solve ();
  }
    
  
}
