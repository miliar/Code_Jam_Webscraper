#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
vector<int> num;

int main() {
  int num_case;
  cin>>num_case;
  for (int count=0;count<num_case;count++) {
    int r,k,n;
    cin>>r>>k>>n;
    num.resize(n);
    for (int i=0;i<n;i++) {
      cin>>num[i]; 
    }
    int euro = 0;
    int p = 0;
    for(int i=0;i<r;i++) {
      int np = 0;
      int p_start = p;
      while(np+num[p]<=k) {
        np+=num[p];
        if (++p==n) p = 0;
        if (p==p_start)break;
      }
      euro += np;
    }
    cout<<"Case #"<<count+1<<": "<<euro;
    cout<<endl;
  }
  return 0;
}
