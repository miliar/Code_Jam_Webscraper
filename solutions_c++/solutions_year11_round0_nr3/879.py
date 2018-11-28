#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <cstring>

using namespace std;

int A[1001];

int main()
{
  string ln;
  int T,N;

  getline(cin,ln);
  istringstream(ln)>>T;

  for(int test=1;test<=T;test++){

    getline(cin,ln);
    istringstream(ln)>>N;

    getline(cin,ln);
    istringstream in(ln);

    int t=0;
    int s=0;

    for(int i=0;i<N;i++){
      in>>A[i];
      t=(t|A[i])&(~(t&A[i]));
      s+=A[i];
    }

    sort(A,A+N);

    if(t==0) cout<<"Case #"<<test<<": "<<s-A[0]<<endl;
    else cout<<"Case #"<<test<<": NO"<<endl;

  }

  return 0;
}
