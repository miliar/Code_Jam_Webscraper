#include <iostream>
#include <queue>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long LL;

string A[51];

int main(){

  string ln;
  int T;

  getline(cin,ln);
  istringstream(ln)>>T;

  for(int test=1;test<=T;test++){
    int R,C;

    getline(cin,ln);
    istringstream(ln)>>R>>C;

    for(int i=0;i<R;i++){
      getline(cin,A[i]);
    }

    bool ok=1;

    for(int i=0;i<R&&ok;i++){
      for(int k=0;k<C&&ok;k++){
        if(A[i][k]!='#') continue;

        if(i+1<R&&k+1<C&&A[i][k+1]=='#'&&A[i+1][k]=='#'&&A[i+1][k+1]=='#'){
          A[i][k]='/';
          A[i][k+1]='\\';
          A[i+1][k]='\\';
          A[i+1][k+1]='/';
          continue;
        }

        ok=0;
      }
    }

    cout<<"Case #"<<test<<":"<<endl;
    if(ok){
      for(int i=0;i<R;i++) cout<<A[i]<<endl;
    }else cout<<"Impossible"<<endl;

  }

  return 0;
}
