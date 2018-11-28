#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
#include <algorithm>

#define For(i,n) for(int i=0;i<(n);i++)
#define For1(i,n) for(int i=1;i<=(n);i++)

using namespace std;

bool match(const char *p, char *s){
  while(*p && *s){
    if(*p=='('){
      bool matched=false;
      p++;
      for(;*p!=')';p++){
        if(*p==*s){
          matched = true;
          break;
        }
      }
      if(!matched)
        return false;

      for(;*p!=')';p++);
      p++;
      s++;
      continue;
    }
    else{
      if(*p==*s){
        p++;
        s++;
        continue;
      }
      else
        return false;
    }
  }
  if(*p==0 && *s==0)
    return true;
  else
    return false;
}

int main(){
  char DIC[5005][20];
  int L, D, N;
  cin >> L >> D >> N;
  string str;
  For1(i,D){
    cin >> str;
    strcpy(DIC[i], str.c_str());
  }
  For1(CI,N){
    string p;
    cin >> p;
    int res = 0;
    For1(i,D){
      if(match(p.c_str(),DIC[i]))
        res++;
    }
    cout << "Case #" << CI << ": " << res << endl;
  }
}
