#include <cstdio>
#include <cstring>

int L, d, n;

char str[5020][20];
int plen;
char pat[100100];
char can[500][30];

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int i, j, h;
  scanf("%d%d%d\n", &L, &d, &n);
  for (i=0; i<d; i++){
    gets(str[i]);
  }
  for (i=0; i<n; i++){
    gets(pat);
    //printf("%s\n", pat);
    memset(can, 0, sizeof(can));
    int k = 0;
    for (j=0; pat[j]; j++){
      if (pat[j]=='('){
        for (h=j+1; pat[h]!=')'; h++){
          can[k][pat[h]-'a'] = 1;
        }
        j = h;
      }
      else{
        can[k][pat[j]-'a'] = 1;
      }
      k++;
    }
    int ans = 0;
    for (j=0; j<d; j++){
      for (h=0; h<L; h++){
        if (!can[h][str[j][h]-'a']) break;
      }
      ans += (h==L);
    }
    printf("Case #%d: %d\n", i+1, ans);
  }
  return 0;
}
