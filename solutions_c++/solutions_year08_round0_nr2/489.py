#include "debug.h"
#include <iostream>
#include <cstdio>
#include <queue>

struct event {
  char gdje, sto;
  int vrijeme;
  //gdje = A, B... sto = D, O
  event(char gdje, char sto, int vrijeme) {
    this->gdje = gdje;
    this->sto = sto;
    this->vrijeme = vrijeme;
  }  
  
  friend bool operator < (const event &a, const event &b) {
    if (a.vrijeme != b.vrijeme) return a.vrijeme > b.vrijeme;
    else return a.sto > b.sto; //dolazak prije odlaska
  }  
};  

using namespace std;

pair<int,int> solve( priority_queue< event > &events ) {
  int sA = 0, sB = 0, rA = 0, rB = 0;
  while( events.size() ) {
    event tren = events.top(); events.pop();
//    cout << tren.vrijeme << " " << tren.gdje <<  " " << tren.sto << endl;
    
    if (tren.sto == 'D') {
      if (tren.gdje == 'A') sA ++;
      if (tren.gdje == 'B') sB ++;
      continue;
    }  
    
    if (tren.sto == 'O') {
      if (tren.gdje == 'A') {
         if (sA > 0) sA --;
         else rA ++;
       }
       if (tren.gdje == 'B') {
         if (sB > 0) sB --;
         else rB ++;
       }    
    }  
  }  
  return make_pair( rA, rB );
}  

int main(void) {
  int n, na, nb, t, ph, pm, kh, km;
  cin >> n;
  for(int i=0; i<n; i++) {
     cin >> t;
     scanf("%d %d\n", &na, &nb);
     
    priority_queue < event > events;
    
     for(int i=0; i<na; i++) {
        scanf("%d:%d %d:%d", &ph, &pm, &kh, &km);
        int poc = ph * 60 + pm;
        int kraj = kh * 60 + km;
        
        events.push( event('A', 'O', poc ) );
        events.push( event('B', 'D', kraj + t) );
     }
     
     for(int i=0; i<nb; i++) {
        scanf("%d:%d %d:%d", &ph, &pm, &kh, &km);
//        cout << ph << ":" << pm << " " << kh << ":" << km << endl;
        int poc = ph * 60 + pm;
        int kraj = kh * 60 + km;
        
        events.push( event('B', 'O', poc ) );
        events.push( event('A', 'D', kraj + t) );
     }
     
     pair<int,int> r = solve( events );
     cout << "Case #" << (i + 1) << ": " << r.first << " " << r.second << endl;    
  }  
  
  return 0;
}

