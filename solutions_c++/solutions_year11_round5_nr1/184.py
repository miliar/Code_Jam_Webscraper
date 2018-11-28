#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

typedef long long ll;
typedef complex<double> pt;

double area(vector<pair<int,int> > &ls,
            vector<pair<int,int> > &us,
            double xl,
            double xr)
{
  double yll = 0, ylu = 0;
  double yrl = 0, yru = 0;

  for (int i=0; i+1<(int)ls.size(); i++){
    double x1 = ls[i].first;
    double x2 = ls[i+1].first;
    double y1 = ls[i].second;
    double y2 = ls[i+1].second;
    if (x1 <= xl && xl <= x2){
      yll = ((xl-x1)/(x2-x1)) * (y2-y1) + y1;
    }
    if (x1 <= xr && xr <= x2){
      yrl = ((xr-x1)/(x2-x1)) * (y2-y1) + y1;
    }
  }
  for (int i=0; i+1<(int)us.size(); i++){
    double x1 = us[i].first;
    double x2 = us[i+1].first;
    double y1 = us[i].second;
    double y2 = us[i+1].second;
    if (x1 <= xl && xl <= x2){
      ylu = ((xl-x1)/(x2-x1)) * (y2-y1) + y1;
    }
    if (x1 <= xr && xr <= x2){
      yru = ((xr-x1)/(x2-x1)) * (y2-y1) + y1;
    }
  }

  return ((ylu-yll)+(yru-yrl))*(xr-xl)/2;
}

double solve(vector<pair<int,int> > &ls,
             vector<pair<int,int> > &us,
             vector<int> &xs,
             int gi,
             int g,
             int w)
{
  double tot = 0;

  for (int i=0; i+1<(int)xs.size(); i++){
    int x1=xs[i];
    int x2=xs[i+1];
    tot += area(ls, us, x1, x2);
  }

  double ll = 0, rr = w;

  for (int i=0; i<100; i++){
    double mm = (ll+rr) / 2;
    int j;
    double cur = 0;
    for (j=0; j+1<(int)xs.size() && xs[j+1] < mm; j++)
      cur += area(ls, us, xs[j], xs[j+1]);
    if (j < (int)xs.size())
      cur += area(ls, us, xs[j], mm);

    double th = tot * gi / g;
    if (cur > th) rr = mm;
    else ll = mm;
  }
  return (ll+rr)/2;
}

int main(int argc, char *argv[])
{
  cout<<setiosflags(ios::fixed)<<setprecision(10);
  int cases; cin>>cases;
  for (int cn=1; cn<=cases; cn++){
    int w, l, u, g;
    cin>>w>>l>>u>>g;

    vector<pair<int, int> > ls(l);
    for (int i=0; i<l; i++)
      cin>>ls[i].first>>ls[i].second;
    vector<pair<int, int> > us(u);
    for (int i=0; i<u; i++)
      cin>>us[i].first>>us[i].second;

    set<int> xss;
    for (int i=0; i<(int)ls.size(); i++)
      xss.insert(ls[i].first);
    for (int i=0; i<(int)us.size(); i++)
      xss.insert(us[i].first);

    vector<int> xs(xss.begin(), xss.end());
    
    cout<<"Case #"<<cn<<":"<<endl;
    for (int i=0; i<g-1; i++){
      cout<<solve(ls, us, xs, i+1, g, w)<<endl;
    }
  }
  
  return 0;
}

