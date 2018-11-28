#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <cstring>

using namespace std;

char A[256][256];
char B[256][256];

int main()
{
  string ln;
  int T;

  getline(cin,ln);
  istringstream(ln)>>T;

  for(int test=1;test<=T;test++){

    bzero(A,sizeof(A));
    bzero(B,sizeof(B));

    getline(cin,ln);
    istringstream in(ln);
    int C,D,N;
    char c1,c2,c3;
    string S;
    vector<char> v;

    in>>C;
    for(int i=0;i<C;i++){
      in>>c1>>c2>>c3;
      A[c1][c2]=c3;
      A[c2][c1]=c3;
    }

    in>>D;
    for(int i=0;i<D;i++){
      in>>c1>>c2;
      B[c1][c2]=1;
      B[c2][c1]=1;
    }

    in>>N;
    in>>S;

    for(int i=0;i<N;i++){

      v.insert(v.begin(),S[i]);

      while(v.size()>1){
        char c=A[v[0]][v[1]];
        if(!c) break;
        v.erase(v.begin());
        v.erase(v.begin());
        v.insert(v.begin(),c);
      }

      for(int k=1;k<v.size();k++)
        if(B[v[0]][v[k]]) v.clear();

    }


    cout<<"Case #"<<test<<": [";
    for(int i=v.size()-1,k=0;i>=0;i--,k++)
      { if(k>0) cout<<", "; cout<<v[i]; }
    cout<<"]"<<endl;
  }

  return 0;
}
