#include <iostream>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <map>
#include <queue>
#include <algorithm>
#include <complex>
#include <set>
#include <vector>
#include <bitset>

#define REP(i,N)for(int i=0;i<(int)N;i++)
#define MP(a,b) make_pair(a,b)
using namespace std;

int nextInt(){
  int ret=0,sign=1;
  char c=' ';
  while (!isdigit(c=getchar())){
    if (c==EOF) return -1;
    if (c=='-') sign=-1;
  }
  do{
    ret=ret*10+(c-'0');
  }while (isdigit(c=getchar()));
  return ret*sign;
}
void printlineInt(int num){
  char str[101];
  if (num<0) num=-num,putchar('-');
  else if (num==0) {puts("0");return;}
  str[100]='\0';
  int i=99;
  for (;num;i--){
    str[i]=num%10+'0';
    num/=10;
  }
  puts(&str[i+1]);
  return;
}
//template end

int R,C;
bool valid(int r,int c){
  return 0<= r && r < R && 0 <= c && c < C;
}
set<string> dir;
int makedir(string str){
  int ret = 0;
  if (dir.find(str) == dir.end()) ret=1;
  dir.insert(str);
  for (int i=1;i<str.size();i++){

    if (str[i] == '/'){
      string s = str.substr(0,i);
      if (dir.find(s) == dir.end()) ret++;
      dir.insert(s);
    }
  }
  return ret;
}
int main(){
  //here
  int T=nextInt();
  REP(tt,T){
    int N=nextInt(),M=nextInt();
    dir.clear();
    dir.insert("/");
        
    REP(i,N){
      string str;
      cin >> str;
      makedir(str);
    }
    int ans = 0;
    REP(i,M){
      string str;
      cin >> str;
      ans += makedir(str);
    }
    printf("Case #%d: %d\n",tt+1,ans);
  }
}
