#include <cstdio>
#include <cstring>
#include <algorithm>
#define REP(i,n) for(int i = 0; i<n; i++)
#define FOR(i,a,b) for(int i = a; i<b; i++)
#define FORD(i,b,a) for(int i = b-1; i>=a; i--)
using namespace std;

int gcd(int a, int b){
  if(!b)return a; else return gcd(b,a%b);
} 

char words[10005][15];
int signatures[10005][27];
int ok1[10005], ok2[10005];
int temp[10005];
char order[100];

bool cmp(int u, int v){
  if(u == v)return false;
  if(signatures[u][0] != signatures[v][0])return signatures[u][0]<signatures[v][0];
  REP(i,26)
    if(signatures[u][order[i]-'a'+1] != signatures[v][order[i]-'a'+1])
      return signatures[u][order[i]-'a'+1] < signatures[v][order[i]-'a'+1];
}

void scase(int CID){
  int N,M;
  scanf("%d%d",&N,&M);
  REP(i,N)scanf("%s",words[i]);
  REP(i,N){
    int L = strlen(words[i]);
    signatures[i][0] = L;
    FOR(j,1,27) signatures[i][j] = 0;
    REP(j,L)
      signatures[i][words[i][j]-'a'+1] |= (1<<j);
  } 
  printf("Case #%d:",CID);
  REP(i,M){
    scanf("%s",order);
    REP(i,N)temp[i] = i;
    sort(temp, temp+N,cmp);
    ok1[temp[0]] = 0;
    FOR(i,1,N){
      int u = temp[i-1];
      int v = temp[i];
      if(signatures[u][0] != signatures[v][0])
        ok1[v] = 0;
      else{
        int count = 0;
        while(signatures[u][order[count]-'a'+1] == signatures[v][order[count]-'a'+1])count++;
        int MASK = 1<<count;
        ok1[v] = MASK | (ok1[u]&(MASK-1));
      }
    } 
    ok2[temp[N-1]] = 0;
    FORD(i,N-1,0){
      int u = temp[i+1];
      int v = temp[i];
      if(signatures[u][0] != signatures[v][0])
        ok2[v] = 0;
      else{
        int count = 0;
        while(signatures[u][order[count]-'a'+1] == signatures[v][order[count]-'a'+1])count++;
        int MASK = 1<<count;
        ok1[v] = MASK | (ok1[u]&(MASK-1));
      }
    }
    int maxi = -1,maxw;
    REP(j,N){
      int temp = 0;
      int ok = ok1[j]|ok2[j];
      REP(k,26)
        if((ok & (1<<k)) && !signatures[j][order[k]-'a'+1]){temp++;}
      if(temp > maxi){
        maxi = temp;
        maxw = j;
      } 
    }
    printf(" %s",words[maxw]);
  } 
  printf("\n");
}

int main(){
  int cases;
  scanf("%d",&cases);
  REP(CID,cases)scase(CID+1);
}
