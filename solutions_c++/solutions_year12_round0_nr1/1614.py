#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;


#define REP(n) for (int i=0;i<(n);i++)
int main(void) {
  ifstream a1,a2;
  int T;
  string w1="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
  string w2="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
  char alf[256];
  
  REP(256) alf[i]=0;  
  for (int i=0;i<w1.length();i++) 
      alf[w1[i]] = w2[i];      
  alf['z'] = 'q';   
  alf['q'] = 'z';

//  REP(256) {
//    if (alf[i] != 0) {
//      printf("%c -> %c\n",i,alf[i]);
//    }
//  }
  
  cin >> T;
  char w[200];
  cin.getline(w,200);
  REP(T) {
    cin.getline(w,200);
    for (int j=0;j<strlen(w);j++) 
      w[j] = alf[w[j]];
    cout << "Case #" << i+1 << ": " << w << endl;    
  }
  
      
}
  