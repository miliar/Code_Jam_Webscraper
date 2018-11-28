#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
using namespace std;

#define EXT 5
#define MAX_N 100
#define MAX_LEN 512
#define NCHARS 256
#define STLEN 19
#define XMOD 10000

#define JOIN(a,b) a##b
#define FORX(i,c) for( __typeof( (c).begin() ) i = (c).begin(), JOIN(i,__end) = (c).end(); i != JOIN(i,__end); i++)

int N;
int LEN;
char input[MAX_LEN+EXT];
bool mat[NCHARS+EXT][NCHARS+EXT];
bool matp[STLEN][NCHARS+EXT][NCHARS+EXT];
vector<int> adj[MAX_LEN+EXT];
char text[STLEN+1] = "welcome to code jam";
int dp[MAX_LEN+EXT][STLEN+EXT];

void build_links(const char *str){
  int n = strlen(str);
  for(int i = 0; i < n-1; i++){
    int u = str[i];
    int v = str[i+1];
    mat[u][v] = true;
    matp[i][u][v] = true;
  }
}

void print_links(){
  for(int i = 'a'; i <= 'z'; i++){
    printf("'%c':",i);
    for(int k = 0; k < NCHARS; k++){
      if(mat[i][k]){
        printf(" '%c'",k);
      }
    }
    putchar('\n');
  }
  printf("' ':");
  for(int k = 0; k < NCHARS; k++){
    if(mat[' '][k]){
      printf(" '%c'",k);
    }
  }
  putchar('\n');
}

void build_graph(const char *str){
  for(int i = 0; i < LEN; i++){
    adj[i].clear();
  }
  for(int i = 0; i < LEN; i++){
    for(int k = i+1; k < LEN; k++){
      int u = str[i];
      int v = str[k];
      if(mat[u][v]){
        adj[i].push_back(k);
        //printf("%d -> %d\n",i,k);
        //printf("%c <-> %c\n",u,v);
      }
    }
  }
}

int go(int u, int pos){
  if(pos==STLEN-1) return 1;
  int &res = dp[u][pos];
  if(res>=0) return res;
  res = 0;
  FORX(v,adj[u]){
    int x = input[u];
    int y = input[*v];
    if(matp[pos][x][y]){
      res += go(*v,pos+1);
      res %= XMOD;
    }
  }
  return res;
}

int main(){
  scanf("%d\n",&N);
  build_links(text);
  //print_links();
  for(int i = 1; i <= N; i++){
    memset(dp,-1,sizeof(dp));
    fgets(input,sizeof(input),stdin);
    LEN = strlen(input)-1;
    //printf(">>%s",input);
    build_graph(input);
    int res = 0;
    for(int k = 0; k < LEN; k++){
      if(input[k]=='w'){
        int t = go(k,0);
        //printf("%d\n",t);
        res += t;
        res %= XMOD;
      }
    }
    printf("Case #%d: %.4d\n",i,res);
    //printf("Case #%d: %d\n",i,res);
  }
  return 0;
}
