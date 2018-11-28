#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
using namespace std;

struct Elem{
  int time;
  bool krenuo;
  int loc;
  
  Elem(int _t, bool _iza, int _l):time(_t), krenuo(_iza), loc(_l){}
  
  friend bool operator<(const Elem &a, const Elem &b){
    return a.time > b.time || (a.time == b.time && a.krenuo);
  }
};


int main(){
  FILE *f;
  f = fopen("B-large.in", "r");
  
  FILE *fout;
  fout = fopen("B-large.out", "w");
  
  char lajna[15];
  
  int test;
  fscanf(f, "%d\n", &test);
  for (int tt = 1; tt <= test; tt++){
    priority_queue<Elem> heap;
    
    int t;
    fscanf(f, "%d\n", &t);
    
    int na, nb;
    fscanf(f, "%d %d\n", &na, &nb);
    
    for (int i = 0; i < na; i++){
      fgets(lajna, 15, f);
      
      int dep = (10 * (lajna[0] - '0') + (lajna[1] - '0')) * 60 + (lajna[3] - '0') * 10 + (lajna[4] - '0');
      int arr = (10 * (lajna[6] - '0') + (lajna[7] - '0')) * 60 + (lajna[9] - '0') * 10 + (lajna[10] - '0');
      
      heap.push(Elem(dep, true, 0));
      heap.push(Elem(arr + t, false, 1));
    }
    
    for (int i = 0; i < nb; i++){
      fgets(lajna, 15, f);
      
      int dep = (10 * (lajna[0] - '0') + (lajna[1] - '0')) * 60 + (lajna[3] - '0') * 10 + (lajna[4] - '0');
      int arr = (10 * (lajna[6] - '0') + (lajna[7] - '0')) * 60 + (lajna[9] - '0') * 10 + (lajna[10] - '0');
      
      heap.push(Elem(dep, true, 1));
      heap.push(Elem(arr + t, false, 0));
    }
    
    int ulevo = 0, udesno = 0;
    int cL = 0, cD = 0;
    
    while (!heap.empty()){
      Elem vrh = heap.top(); heap.pop();
      if (vrh.loc == 0){
        if (vrh.krenuo){
          if (cL == 0) ulevo++;
          else cL--;
        }
        else cL++;
      }
      else{
        if (vrh.krenuo){
          if (cD == 0) udesno++;
          else cD--;
        }
        else cD++;
      }
    }
    
    fprintf(fout, "Case #%d: %d %d\n", tt, ulevo, udesno);
  }
  
  fclose(f);
  fclose(fout);
  
  return 0;
}
    
