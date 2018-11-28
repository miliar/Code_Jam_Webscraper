#include<iostream>
#include<algorithm>
#include<cmath>

using namespace std;

long long gcd(long long a, long long b){
  return b==0?a:gcd(b,a%b);
}

int main()
{
  int T;
  cin >> T;
  for(int tc=1;tc<=T;++tc){
    string res;

    long long N,PD,PG;
    cin >> N >> PD >> PG;
    

    bool dflag = false;
    if( N >= 100 ){
      dflag = true;
    }else{
      for(int D = 1; D <= N; ++D){
        for(int wd = 0; wd <= D; ++wd){
          if( wd * 100 % D == 0 ){
            if( PD == wd * 100 / D ) dflag = true;
          }
        }
      }
    }

    if( dflag ){
      if( PG == 100 && PD < 100 ) res = "Broken";
      else if( PG == 0 && PD > 0) res = "Broken";
      else res = "Possible";
    }else{
      res = "Broken";
    }
    
    cout << "Case #"<<tc<<": " << res << endl;
  }
  return 0;
}
