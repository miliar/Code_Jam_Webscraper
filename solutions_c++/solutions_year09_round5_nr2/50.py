#include <cstdio>
#include <set>
#include <string>
#include <cstring>

using namespace std;

const int MOD = 10009;

int n, K, len;
char str[100];
char dict[128][128];
int occ[30];
int ans[12];

void add_val(int wh){
  int r=1;
  int i;
  for (i=0; i<=len; i++){
    if(i==len || str[i]=='+'){
      ans[wh]+=r;
      ans[wh] %= MOD;
      r=1;
    }
    else{
      r *= occ[str[i]-'a'];
      r %= MOD;
    }
  }
}

void add(char * str, int sgn){
  int i;
  for (i=0; str[i]; i++){
    occ[str[i]-'a'] += sgn;
  }
}

void calc(int pos){
  if (pos > K) return;
  int i;
  for (i=0; i<n; i++){
    add(dict[i], 1);
    add_val(pos);
    calc(pos+1);
    add(dict[i], -1);
  }
}

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn, t;
  scanf("%d", &tn);
  for (t=1; t<=tn; t++){
    scanf("%s%d", &str, &K);
    len = (int)strlen(str);
    scanf("%d\n", &n);
    int i;
    for (i=0; i<n; i++){
      gets(dict[i]);
    }
    memset(ans, 0, sizeof(ans));
    calc(1);
    printf("Case #%d:", t);
    for (i=1; i<=K; i++) printf(" %d", ans[i]);
    printf("\n");
    fflush(stdout);
  }
  return 0;
}
