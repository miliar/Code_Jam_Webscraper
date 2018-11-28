#include <iostream>
#include <iomanip>
#include <sstream>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

typedef long long LL;

int A[1001];

int main()
{
  int T,S,N,p;
  cin>>T;

  for(int t=0;t<T;t++){

    cin>>N>>S>>p;
    for(int i=0;i<N;i++){
      cin>>A[i];
    }
    sort(A,A+N);

    int res=0;

    for(int i=N-1;i>=0;i--){
      if(A[i]<p) continue;
      if(A[i]>=3*p-2) res+=1;
      else if(A[i]>=3*p-4 && S>0){
        res+=1;
        S-=1;
      }
    }

    cout<<"Case #"<<t+1<<": "<<res<<endl;
  }

  return 0;
}
