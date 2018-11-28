#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <iostream>
using namespace std;
int L,D,N,i,c;
char dict[1000000];
char buf[100000];
int mark[5010];
char ch;
bool p;
char* dictptr;
char* startptr;
int main() {
  scanf("%d %d %d\n", &L, &D, &N);
  fread(dict,(L+1)*D,1,stdin);

  for(int i=0;i<N;i++) {
    p=false;
    for(int j=0;j<5010;j++ ) mark[j] = 0;
    startptr=dict;

    while(1) {
      ch = getchar();
      if(ch=='\n') break;
      switch(ch) {
        case '(': p=true; break;
        case ')': p=false; startptr++; break;
        default:
          dictptr = startptr;
          for(int z=0;z<D;z++) {
            if(*dictptr==ch) mark[z]++;
            dictptr+=L+1;
          }
          if(!p) startptr++;
      }
    }
    c=0;
    for(int z=0;z<D;z++) {
      if(mark[z]==L) c++;
    }

    cout << "Case #"<<i+1<<": "<<c<<"\n";
  }
  return 0;
};
