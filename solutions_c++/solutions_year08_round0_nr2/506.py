#include <iostream>
using namespace std;

const int maxN = 2048, maxV = 100000;

int As[maxN], At[maxN], Bs[maxN], Bt[maxN];

void doit(){
  char c;
  int t, i, j, x, y, la, lb, ta = 0, tb = 0, ra = 0, rb = 0;
  cin >> t >> la >> lb;
  for(i = 0; i < la; i++){
    cin >> x >> c >> y;
    As[i] = 60*x+y;
    cin >> x >> c >> y;
    At[i] = 60*x+y+t;
  }
  for(i = 0; i < lb; i++){
    cin >> x >> c >> y;
    Bs[i] = 60*x+y;
    cin >> x >> c >> y;
    Bt[i] = 60*x+y+t;
  }
  sort(As, As+la);
  sort(At, At+la);
  sort(Bs, Bs+lb);
  sort(Bt, Bt+lb);
  At[la] = maxV;
  Bt[lb] = maxV;
  
  i = 0; j = 0;
  while(i < la){
    if(Bt[j] <= As[i]){
      ta++;
      j++;
    }else{
      i++;
      ta--;
      if(ta == -1){ta = 0; ra++;}
    }
  }
  
  i = 0; j = 0;
  while(i < lb){
    if(At[j] <= Bs[i]){
      tb++;
      j++;
    }else{
      i++;
      tb--;
      if(tb == -1){tb = 0; rb++;}
    }
  }
  
  cout << ra << ' ' << rb << endl;
  
}

int main(){
  int tst, tc;
  cin >> tst;
  for(tc = 1; tc <= tst; tc++){
    cout << "Case #" << tc << ": ";
    doit();
  }
  return 0;
}
