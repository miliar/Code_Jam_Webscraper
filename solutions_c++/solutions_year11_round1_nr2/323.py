#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
using namespace std;

#define maxn 10007

struct atype
{
    int num;
    char t[12];
    int len;
    int a[30];
};

int cases;
atype a[maxn];
char b[28];
int n,m;
char ch;
int w;
int f[maxn];
int ans;
char c[maxn][12];

bool cmp(atype p, atype q)
{
    if (p.len < q.len) return true;
    if (p.len > q.len) return false;
    for (int i = 0; i < 26; ++i){
      if (p.a[i] < q.a[i]) return true;
      if (p.a[i] > q.a[i]) return false;
    }
    return false;
}
void make(int l, int r, int k, int w)
{
    if (k == 26) {
      for (int i = l; i <= r; ++i) 
        f[a[i].num] = w;
      return;
    }
    int ll, rr;
    ll = l;
    for (int i = l+1; i <= r; ++i) {
      if (a[i].a[k] > a[i-1].a[k]) {
        if (a[ll].a[k] == 0)
          make(ll,i-1,k+1,w+1);
        else
          make(ll,i-1,k+1,w);
        ll = i;
      }
    }
    make(ll,r,k+1,w);
}
int main()
{
    freopen("B0.in","r",stdin);
    freopen("B0.out","w",stdout);
    
    scanf("%d",&cases);
    for (int k = 1; k <= cases; ++k) {
      printf("Case #%d: ",k);
      scanf("%d%d",&n,&m);
      scanf("%c",&ch);
      for (int i = 1; i <= n; ++i) {
        scanf("%s",c[i]);
      }
      for (int i = 1; i <= m; ++i) {
        scanf("%s",b);
        memset(f,0,sizeof(f));
        for (int j = 1; j <= n; ++j) {
          a[j].len = strlen(c[j]);
          a[j].num = j;
        }
        for (int j = 0; j < 26; ++j)
          for (int k = 1; k <= n; ++k) {
            w = 0;
            for (int p = 0; p < a[k].len; ++p) {
              w *= 2;
              if (c[k][p] == b[j]) ++w;
            }
            a[k].a[j] = w;
          }
        
        sort(a+1, a+(1+n), cmp);
        
        int l(1), r;
        for (int i = 2; i <= n; ++i) 
          if (a[i].len > a[i-1].len) {
            make(l,i-1,0,0);
            l = i;
          }
        make(l,n,0,0);
        
        ans = 1;
        for (int i = 2; i <= n; ++i)
          if (f[i] > f[ans]) ans = i;
        printf("%s ", c[ans]);
      }
      printf("\n");
    }
    return 0;
}
