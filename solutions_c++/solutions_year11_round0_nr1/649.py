#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
using namespace std;

int n;
int to, tb, po, pb, t;
char ch;
int x;
int times;

int abs(int w)
{
    if (w < 0) w = -w;
    return w;
}
int main()
{
    freopen("A1.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&times);
    for (int k = 1; k <= times; ++k) {
      printf("Case #%d: ",k);
      scanf("%d",&n);
      t = to = tb = 0;
      po = pb = 1;
      for (int i = 1; i <= n; ++i) {
        scanf("%c",&ch);
        scanf("%c%d",&ch,&x);
        if (ch == 'O') {
          to += abs(x-po)+1;
          po = x;
          if (to <= t) 
            to = t+1;
          t = to;
        }
        else {
          tb += abs(x-pb)+1;
          pb = x;
          if (tb <= t) 
            tb = t+1;
          t = tb;
        }
      }
      printf("%d",t);
      printf("\n");
    }
    return 0;
}
