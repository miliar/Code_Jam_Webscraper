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

int main(){
  //here
  int T=nextInt();
  REP(tt,T){
    int N=nextInt(),K=nextInt();
    printf("Case #%d: %s\n",tt+1
           ,__builtin_popcount(K % (1 << N)) == N ? "ON":"OFF");
  }
}
