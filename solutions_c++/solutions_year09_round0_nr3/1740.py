#include<iostream>
using namespace std;

const int N = 501;
const int K = 20;
const int MOD = 10000;
string wz;
string tab;
int dyn[N];

int licz(string y){
  int a = 0;
  int poz = 0;
  while(poz < y.size()){
    a *= 10;
    a += y[poz] - '0';
    poz++;
  }
  return a;
}

main(){
  wz = "0welcome to code jam";
  int n,y;
  getline(cin,tab);
  n = licz(tab);
  for(int i=1;i<=n;i++){
    getline(cin,tab);
    int roz = tab.size();
    for(int j=0;j<K;j++) dyn[j] = 0;
    dyn[0] = 1;
    for(int j=0;j<roz;j++){
      for(int k=1;k<K;k++)
        if(wz[k] == tab[j]){
          dyn[k] += dyn[k-1];
          dyn[k] %= MOD;
        }
    }
    printf("Case #%d: %04d\n",i,dyn[K-1]);
  }
}
