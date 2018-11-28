#include <cstdio>
#include <cstring>
#define MAXN 22
int N , T;
int s;
bool flag;
int h[MAXN] , a[MAXN];

void print() {
    int i;
    bool f;
    flag = true;
    f = false;
    for (i = 0;i < N;i++)
      if (h[i] == 1) if (!f) {
            printf("%d",a[i]);
            f = true;
        }
        else printf(" %d",a[i]);
    printf("\n");
    f = false;
    for (i = 0;i < N;i++)
      if (h[i] == 2) if (!f) {
            printf("%d",a[i]);
            f = true;
        }
        else printf(" %d",a[i]);
    printf("\n");
}

void dfs(int s1 , int s2, int step) {
    if (step == N) return ;
    if (s1 > s/2 || s2 > s2) return ;
    if (flag) return ;
    if (s1 == s2 && s1 != 0) print();
    for (int i = 0;i <= 2;i++) {
        h[step] = i;
        if (!i) dfs(s1,s2,step+1);
          else 
            if (i == 1) dfs(s1+a[step],s2,step+1);
              else dfs(s1,s2+a[step],step+1);
        h[step] = 0;
    }
}
               
int main () {
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    
    int p , i , j;
    scanf("%d\n",&T);
    for (p = 1;p <= T;p++) {
        printf("Case #%d:\n",p);
        s = 0;
        scanf("%d\n",&N);
        flag = false;
        for (i = 0;i < N;i++)
          scanf("%d\n",&a[i]) , s += a[i];
        memset(h,0,sizeof(h));
        dfs(0,0,0);
    }
    return 0;
}
