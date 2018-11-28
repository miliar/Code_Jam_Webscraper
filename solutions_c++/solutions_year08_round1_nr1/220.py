#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int x[1000];
int y[1000];
int n;
int t;

void init()
{
  scanf(" %d", &n);
  for (int i = 0; i < n; ++i) {
    scanf(" %d", x+i);
  }
  for (int i = 0; i < n; ++i) {
    scanf(" %d", y+i);
  }
  sort(x, x+n);
  sort(y, y+n);
}

void proc()
{
  int s = 0;
  for (int i = 0; i < n; ++i) {
    s += x[i]*y[n-i-1];
  }
  printf("%d\n", s);
}


int main()
{
  scanf(" %d", &t);
  for (int i = 0; i < t; ++i) {
    init();
    printf("Case #%d: ", i+1);
    proc();
  }
}
