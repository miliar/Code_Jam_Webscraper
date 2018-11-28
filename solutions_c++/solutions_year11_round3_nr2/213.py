#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;

long long dist[10000000];
priority_queue<int> kju;


int main(){

  int TT;
  scanf("%d", &TT);
  for(int T = 0; T < TT; T++){
    
    long long  l, t, n,c ;
    scanf("%lld %lld %lld %lld", &l, &t, &n, &c);
    for(long long i =0; i<c; i++){
      scanf("%lld", &dist[i]);
    }
    
    long long pos;
    pos = 0;
    long long razd = 0;
    long long kje = -1;
    long long kjer;
    
    for(long long i=0; i<n; i++){
      razd += dist[pos]*2;
      if(razd>=t && kje == -1){
	kje = i;
	kju.push(razd-t);
      } else if(kje > -1){
	kju.push(dist[pos]*2);
      }
      pos++;
      if(pos == c) pos = 0;
    }    
    
    for(int i=0; i<l; i++){
      if(kju.empty()) break;
      razd -= kju.top()/2;
      kju.pop();
    }
    
    printf("Case #%d: %lld\n", T+1, razd);
    
    kju = priority_queue <int>();
    while(!kju.empty()) kju.pop(); // stupid, i know
  }
  
  return 0;
}