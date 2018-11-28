#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <cstring>

using namespace std;

char R[101];
int P[101];

int main()
{
  string ln;
  int T;

  getline(cin,ln);
  istringstream(ln)>>T;

  for(int test=1;test<=T;test++){

    getline(cin,ln);
    istringstream in(ln);
    int N;

    in>>N;
    for(int i=0;i<N;i++)
      in>>R[i]>>P[i];

    int t=0,t1=0,t2=0;
    int p1=1,p2=1;

    for(int i=0;i<N;i++){
      if(R[i]=='O'){
        t=max(t+1,t1+abs(P[i]-p1)+1);
        t1=t;
        p1=P[i];
      }else{
        t=max(t+1,t2+abs(P[i]-p2)+1);
        t2=t;
        p2=P[i];
      }
    }

    cout<<"Case #"<<test<<": "<<t<<endl;
  }

  return 0;
}
