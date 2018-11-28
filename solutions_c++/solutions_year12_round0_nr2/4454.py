#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <map>
#include <algorithm>
#include <vector>
#include <cassert>

using namespace std;

#define D(x) cout << #x " is " << x << endl

void debug(int score, int avg, int p, int s){
  D(score);
  D(avg);
  D(p);
  D(s);
}

int main(){
  int T, s, p, n;
  int g[200];
  scanf("%d", &T);
  for(int C = 0; C<T;C++){
    scanf("%d%d%d", &n, &s, &p);
    int ans = 0;
    for(int i=0;i<n;++i) scanf("%d", &g[i]);
    for(int i=0;i<n;++i){
      int score = g[i];
      int avg = score / 3;
      int res = score % 3;
      //debug(score, avg, p, s);
      if(score == 0 && p > 0) continue;
      if(avg >= p){
        //puts("avg >= p");
        ans++;
      }
      else{
        int falta = p - avg;
        if(falta == 1 && 3*avg + 1 == score && avg+1>=p){
          //puts("solo es 1");
          ans++;
        }else if(falta <= 2 && 3*avg+2 == score && avg+1>=p && score > 0){
          //puts("Le subo 1 a 2");
          ans++;
        }else if(falta == 2 && s > 0 && 3*avg + 2 == score && avg+2>=p && score > 0){
          //puts("Faltan 2 y tengo sorpresas");
          ans++;
          s--;
        }else if(falta == 1 && s>0 && 3*avg == score && avg+2>=p && score > 0){
          //puts("Le quito 1 del avg a alguien y sorprendo");
          ans++;
          s--;
        }
      }
    }
    printf("Case #%d: %d\n", C + 1, ans);
  }
  return 0;
}
