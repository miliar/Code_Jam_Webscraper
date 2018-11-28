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
  int cases; cin>>cases;
  for (int cn=1; cn<=cases; cn++){
    int c; cin>>c;

    map<int, int> mm;
    for (int i=0; i<c; i++){
      int p, v; cin>>p>>v;
      mm[p]=v;
    }

    int ans=0;
    for (;;){
      int pos=0;
      for (map<int, int>::iterator p=mm.begin();
	   p!=mm.end(); p++){
	if (p->second>=2){
	  pos=p->first;
	  goto _found;
	}
      }

      break;
    _found:;

      int stp=mm[pos]/2;
      mm[pos]-=stp*2;
      mm[pos-1]+=stp;
      mm[pos+1]+=stp;
      ans+=stp;
    }
    
    cout<<"Case #"<<cn<<": "<<ans<<endl;
  }
  return 0;
}
