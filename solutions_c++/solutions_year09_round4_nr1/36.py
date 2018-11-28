#include <cstdio>
#include <set>
#include <string>
#include <cstring>

using namespace std;

int n;
char str[100];
int rt[100];

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn, t;
  scanf("%d", &tn);
  for (t=1; t<=tn; t++){
    printf("Case #%d: ", t);
    scanf("%d\n", &n);
    int i, j;
    for (i=1; i<=n; i++){
      gets(str);
      for (j=n-1; (j>=0)&&(str[j]=='0'); j--);
      rt[i] = j+1;
    }
    int ans = 0;
    for (i=1; i<=n; i++){
      for (j=i; rt[j]>i; j++);
      while (j > i){
        ans++;
        swap(rt[j], rt[j-1]);
        j--;
      }
    }
    printf("%d\n", ans);
  }
  return 0;
}
