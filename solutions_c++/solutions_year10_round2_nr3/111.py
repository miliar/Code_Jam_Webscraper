#include<iostream>
#include<vector>
#include<algorithm>
#include<gmp.h>
#define MOD 100003

using namespace std;

vector<vector<int> > memo;

int binom(int a,int b){
  if (a<b) 
    return 0;
  mpz_t result;
  mpz_init(result);
  mpz_set_ui(result,1);
  for(int i=2;i<=a;i++){
    mpz_mul_ui(result,result,i);
  }
  for(int i=2;i<=b;i++){
    mpz_tdiv_q_ui(result,result,i);
  }
  for(int i=2;i<=a-b;i++){
    mpz_tdiv_q_ui(result,result,i);
  }
  mpz_tdiv_r_ui(result,result,MOD);
  return mpz_get_si(result);
}

int func(int n,int r){
  if (memo[n][r]!=-1)
    return memo[n][r];
  if (r==1)
    return 1;
  long long total=0;
  int rest=r-1;
  for(int i=1;i<=rest;i++){
    int first = rest-i;
    long long mult = binom(n-r-1,first);
    if (mult)
      mult*=func(r,i);
    total+=mult;
    total%=MOD;
  }
  memo[n][r]=total;
  return total;
}

int main(){
  memo.resize(600);
  for (int i=0;i<600;i++){
    memo[i].resize(600);
    for (int j=0;j<600;j++){
      memo[i][j] = -1;
    }
  }
  int T;
  cin>>T;
  for (int t=1;t<=T;t++){
    int n;
    int total=0;
    cin>>n;
    for (int i=1;i<n;i++){
      total+=func(n,i);
      total%=MOD;
    }
    cout<<"Case #"<<t<<": "<<total<<endl;
  }
}
