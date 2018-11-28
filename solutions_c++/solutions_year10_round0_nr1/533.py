#include<sstream>
#include<vector>
#include<list>
#include<limits>
#include<iostream>
#include<set>
#include<string>
#include<map>
#include<algorithm>
#include<cstdlib>
#include<cstring>
#include<iomanip>
#include<cmath>
#include<queue>

using namespace std;

typedef long long LL;
typedef pair<int,int> P;

int A[5001];

int main(){

  string ln;
  getline(cin,ln);
  int T,N,K;
  istringstream(ln)>>T;
  for(int t=1;t<=T;t++){
    getline(cin,ln);
    istringstream(ln)>>N>>K;
    cout<<"Case #"<<t<<": ";
    if((K%(1<<N))==(1<<N)-1){
      cout<<"ON"<<endl;
    }else{
      cout<<"OFF"<<endl;
    }
  }

  return 0;
}
