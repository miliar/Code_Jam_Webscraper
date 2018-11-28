#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<cmath>
using namespace std;

#define maxn 63

char t[maxn];
int a[maxn];
int b[maxn];
int n;
int cases;
bool f;
long long w;
double ww;
long long z;

bool check()
{
    w = 0;
    for (int i = 0; i < n; ++i)
      w = w*2+a[i];
    z = sqrt(w);
    if (z*z == w) return true;
    return false;
}
void search(int k)
{
    if (k > b[0]) {
      f = check();
      return;
    }
    a[b[k]] = 0;
    search(k+1);
    if (f) return;
    a[b[k]] = 1;
    search(k+1);
}
int main()
{
    freopen("D0.in","r",stdin);
    freopen("D.out","w",stdout);

    scanf("%d",&cases);
    for (int k = 1; k <= cases; ++k) {
      printf("Case #%d: ", k);
      scanf("%s",&t);
      n = strlen(t);
      b[0] = 0;
      for (int i = 0; i < n; ++i) {
        if (t[i] == '?') 
          b[++b[0]] = i;
        else
          a[i] = t[i]-'0';
      }
      f = false;
      search(1);
      for (int i = 0; i < n; ++i) printf("%d",a[i]);
      printf("\n");
    }
}
