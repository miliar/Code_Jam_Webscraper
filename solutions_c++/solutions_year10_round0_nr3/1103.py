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
    long long ans = 0;
    int group[1000],loopcnt[1000],count[1000];
    int R=nextInt(),k=nextInt(),N=nextInt();
    REP(i,N) group[i] = nextInt();
    int cur = 0;
    int loop = 0;
    bool memo[1000] = {};
    while (R){
      //cout << cur << " " << R << " " << ans << endl;      
      if (!memo[cur]) loopcnt[cur] = loop,count[cur] = ans;;
      int j;
      long long v=0;
      if (memo[cur] && R >= loop-loopcnt[cur]){
        int t = R / (loop-loopcnt[cur]);
        ans += (ans - count[cur]) * t;
        R %= (loop-loopcnt[cur]);
        loop += t * (loop - loopcnt[cur]);
        continue;
      }
      for (j=cur;;j++){
        j %= N;
        if (v + group[j] > k) break;
        v += group[j];
        if ((j+1)%N == cur) break;
      }
      loop++;
      ans += v;
      memo[cur] = true;
      R--;
      
      cur = j;
    }

    printf("Case #%d: %lld\n",tt+1,ans);
  }
}
