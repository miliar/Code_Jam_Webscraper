#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdlib>
using namespace std;

void process()
{
  long long n,a,b,c,d,x0,y0,m;
  cin>>n>>a>>b>>c>>d>>x0>>y0>>m;
  vector<pair<long long,long long> > ps;

  long long x=x0,y=y0;
  for (int i=0;i<n;i++){
    ps.push_back(make_pair(x,y));
    x=(a*x+b)%m;
    y=(c*y+d)%m;
  }

  int ans=0;
  for (int i=0;i<n;i++){
    for (int j=i+1;j<n;j++){
      for (int k=j+1;k<n;k++){
	long long cx=ps[i].first+ps[j].first+ps[k].first;
	long long cy=ps[i].second+ps[j].second+ps[k].second;
	if ((cx%3)!=0) continue;
	if ((cy%3)!=0) continue;
	ans++;
      }
    }
  }
  cout<<ans<<endl;
}

int main()
{
  string line;
  getline(cin,line);
  int cases=atoi(line.c_str());
  for (int c=1;c<=cases;c++){
    cout<<"Case #"<<c<<": ";
    process();
  }
}
