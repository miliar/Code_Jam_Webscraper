#include <iostream>
#include <vector>
#include <numeric>
#include <map>
#include <set>
#include <queue>

#define REP(i,e) for(int i=0;i<(int)(e);i++)

using namespace std;

void gen(long long n,long long m,long long x,long long y,long long z,vector<long long> &v){
  vector<long long> a(m,0);
  REP(i,m) cin >> a[i];
  REP(i,n) {
    v.push_back(a[i%m]);
    a[i%m]=(x*a[i%m]+y*(i+1))%z;
    //A[i mod m] = (X * A[i mod m] + Y * (i + 1)) mod Z
  }
}

long long compute(vector<long long> &v){
  const long long limit=1000000007;

  long long result[v.size()];
  REP(i,v.size()) result[i]=1;

  REP(i,v.size()){
    REP(j,i){
      if (v[j]<v[i])
	result[i]+=result[j], result[i]%=limit;
    }
  }
  return accumulate(result,result+v.size(),0ll)%limit;
}

main(){
  long long CT;
  cin >> CT;
  REP(C,CT){
    cout << "Case #" << C+1 << ": ";
    long long n,m,x,y,z;
    vector<long long> v;
    cin >> n >> m >> x >> y >> z;
    gen(n,m,x,y,z,v);
    //REP(i,n) cout << v[i] << ' '; cout << endl;
    cout << compute(v) << endl;
  }
}
