#include <cstdio>
#include <iostream>
#include <cmath>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <complex>
#include <algorithm>
#include <functional>
#include <fstream>
#include <numeric>
#include <string>
#include <valarray>


using namespace std;

typedef pair<int,int> Pair;

template<class a,class b>
ostream & operator << (ostream & tout,const pair<a,b> &c){
  return(tout<<'('<<c.first<<','<<c.second<<')');
}
template<class t>
ostream & operator << (ostream & tout,const vector<t> &s){
  tout<<'[';
  for (int i=0;i<s.size();i++)
    if (i+1 == s.size())
      tout<<s[i];
    else
      tout<<s[i]<<',';
  tout<<']';
  return(tout);
}

const double EPS=1e-8;


int main(){
  cout<<fixed;
  cout.precision(10);

  int ttime;
  cin>>ttime;
  for (int ccount=1;ccount<=ttime;ccount++){
    cerr<<ccount<<endl;
    int x,s,r,t;
    cin>>x>>s>>r>>t;
    int n;
    cin>>n;
    vector<Pair> all;
    for (int i=1;i<=n;i++){
      int x,y,c;
      cin>>x>>y>>c;
      all.push_back(Pair(s+c,y-x));
    }
    int sum=0;
    for (int i=0;i<all.size();i++)
      sum+=all[i].second;
    if (sum)
      all.push_back(Pair(s,x-sum));
    sort(all.begin(),all.end());
    double time=0;
    double rm=t;
    double rp=r-s;
    for (int i=0;i<all.size();i++){
      double a=0,b=all[i].second;
      for (int cc=1;cc<=100;cc++){
	double mid=(a+b)/2;
	if (mid/(all[i].first+rp) > rm)
	  b=mid;
	else
	  a=mid;
      }
      time+=a/(all[i].first+rp);
      rm -= a/(all[i].first+rp);
      time+=(all[i].second-a)/(all[i].first);
    }
    cout<<"Case #"<<ccount<<": "<<time<<endl;
  }
}
