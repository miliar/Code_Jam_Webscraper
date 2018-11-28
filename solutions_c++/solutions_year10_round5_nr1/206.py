#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <complex>
#include <cstdlib>
using namespace std;

typedef complex<double> pt;
typedef long long ll;

int main()
{
  int plim=11000;
  vector<bool> f(plim, true);
  vector<int> ps;

  for (int i=2; i<plim; i++){
    if (f[i]){
      ps.push_back(i);
      for (int j=i+i; j<plim; j+=i)
	f[j]=false;
    }
  }

  int cases; cin>>cases;
  for (int cn=1; cn<=cases; cn++){
    int d, k; cin>>d>>k;
    vector<int> v(k);
    for (int i=0; i<k; i++) cin>>v[i];

    if (k==1){
      cout<<"Case #"<<cn<<": I don't know."<<endl;
      continue;
    }

    int lim=1;
    for (int i=0; i<d; i++) lim*=10;

    int ans=-1;

    int maxv=0;
    for (int i=0; i<k; i++)
      maxv=max(maxv, v[i]);

    for (int pi=0; /*pi < ps.size() && */ ps[pi]<=lim; pi++){
      int p=ps[pi];
      if (p<=maxv) continue;

      for (int a=0; a<=p; a++){

	int s=v[0];
	int t=v[1];

	int b=(t-a*s)%p;
	while(b<0) b+=p;
	while(b>=p) b-=p;

	bool ok=true;
	for (int i=0; i+1<k; i++){
	  int s=v[i];
	  int t=v[i+1];

	  if (t != (a*s+b)%p){
	    ok=false;
	    break;
	  }
	}

	if (!ok) continue;
	int next=(a*v.back()+b)%p;

	if (ans<0){
	  //cout<<a<<", "<<b<<", "<<p<<endl;
	  ans=next;
	}
	else if (ans==next);
	else{
	  cout<<"Case #"<<cn<<": I don't know."<<endl;
	  goto _next;
	}
      }
    }    
    cout<<"Case #"<<cn<<": "<<ans<<endl;
  _next:;
  }
  return 0;
}
