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

void Rotate(vector<string >& v){
  int N=v.size();
  vector<string > ret(N,string(N,' '));
  REP(i,N){
    REP(j,N){
      ret[i][j] = v[N-j-1][i];
    }
  }
  
  for (int i=0;i<N;i++){
    for (int j=N-1,k=N-1;;){
      while (0 <= j && ret[j][i] != '.')j--;
      k = j;
      while (0 <= k && ret[k][i] == '.')k--;
      if (j == -1 || k == -1) break;
      swap(ret[j][i],ret[k][i]);
    }
  }
  v = ret;
  return;
}

int N,K;

bool valid(int r,int c){
  return 0<= r && r < N && 0 <= c && c < N;
}

int main(){
  //here
  int T=nextInt();
  REP(tt,T){
    N=nextInt(),K=nextInt();
    vector<string>table(N);
    REP(i,N) {
      string s;
      cin >> s;
      table[i] = s;
    }

    Rotate(table);
    int dr[8] = {1,1,1,0,0,-1,-1,-1};
    int dc[8] = {1,-1,0,1,-1,1,0,-1};
    bool red = false,blue = false;
    REP(i,N){
      REP(j,N){
        REP(k,8){
          int cnt = 0;
          char c = table[i][j];
          if (c == '.') continue;
          for (int l=0;l<K;l++){
            int nr = i + dr[k] * l;
            int nc = j + dc[k] * l;
            if (!valid(nr,nc)) break;
            if (table[nr][nc] == c){
              cnt++;
            }else{
              break;
            }
          }
          if (cnt == K){
            if (c == 'R') red = true;
            else if (c == 'B') blue = true;
          }
        }
      }
    }
    if (blue && red)
      printf("Case #%d: Both\n",tt+1);
    else if (blue)
      printf("Case #%d: Blue\n",tt+1);
    else if (red)
      printf("Case #%d: Red\n",tt+1);
    else
      printf("Case #%d: Neither\n",tt+1);
      
  }
}
