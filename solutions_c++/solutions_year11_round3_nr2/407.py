#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;
int main(){
  int T;
  cin >> T;
  for(int cases=1;cases<=T;++cases){
    long long res=0;
    int L;
    long long t;
    int N;
    int C=0;
    
    cin >> L >> t >> N >> C;
    int a[C];
    for(int j=0;j<C;++j){
      cin >>  a[j];
    }
//    cout << L << t << N << C  <<endl;
//    for(int j=0;j<C;++j){
//      cout <<  a[j] << endl;
//    }
    t = t/2;
    int R=N/C;
    int r=N%C;
    long long cyc=0;
    long long nonB=0;
    for (int i=0;i<C;++i){
      cyc += a[i];
    }
    nonB = cyc*R;
    for (int i=0;i<r;++i){
      nonB +=a[i];
    }
    res = nonB*2;

    int B=0;
    B = t/cyc;
    int b =  t%cyc;
    int resid=0;
    for(int i =0;i< C;++i){
      b -= a[i];
      resid += 1;
      if(b < 0)break;
    }
//    cout << b << endl;
    B *= C;
    B += resid;
    
    vector<int> V;
    V.push_back(-b);
    for(int i=B;i<N;++i){
      V.push_back(a[i%C]);
    }
    int n = N-B;
    sort(V.begin(),V.end());
    L = min(L,n+1);
    for(int i=0;i<L;++i){
//      cout << V[n-i] << endl;
      res -= V[n-i];
    }
    
    cout << "Case #"<<cases<<": "<< res << endl;
  }
  
  return 0;
}