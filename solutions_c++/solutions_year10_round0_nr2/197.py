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
#include<gmpxx.h>

using namespace std;

typedef long long LL;

mpz_class gcd(mpz_class a,mpz_class b){
  return a%b==0?b:gcd(b,a%b);
}

int main(){

  string ln;
  getline(cin,ln);
  int C,N;
  string t;
  istringstream(ln)>>C;
  for(int c=1;c<=C;c++){
    getline(cin,ln);
    istringstream in(ln);
    in>>N;
    vector<mpz_class> T(N,mpz_class(0));
    for(int i=0;i<T.size();i++){
      in>>t;
      T[i]=mpz_class(t);
    }
    sort(T.begin(),T.end());
    T.erase(unique(T.begin(),T.end()),T.end());
    mpz_class g=T[1]-T[0];
    for(int i=2;i<T.size();i++){
      g=gcd(g,T[i]-T[i-1]);
    }
    cout<<"Case #"<<c<<": ";
    if(T[0]%g==mpz_class(0)){
      cout<<"0"<<endl;
    }else{
      cout<<g-(T[0]%g)<<endl;
    }
  }

  return 0;
}



