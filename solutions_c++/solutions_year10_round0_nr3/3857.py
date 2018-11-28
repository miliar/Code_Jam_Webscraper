#include <algorithm>
#include <bitset>
#include <cassert>
#include <complex>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;

int main() {
  int i,j,l,t,r,k,n,count,temp;
  deque<int> g;
  cin>>t;
  for(i=0;i<t;i++){
    cout<<"Case #"<<i+1<<": ";
    cin>>r>>k>>n;
    g.resize(n);
    for(j=0;j<n;j++)cin>>g[j];
    count=0;
    for(j=0;j<r;j++){
      temp=0;
      for(l=0;l<n;l++){
        temp+=g[0];
        count+=g[0];
        if(temp>k){
          count -= g[0];
          break;
        }
        if(g.size()!=1)rotate(g.begin(),g.begin()+1,g.end());
      }
    }
    cout<<count<<endl;
  }

  return 0;
}

