#include <cstdio>
#include <cstring>
using namespace std;

char line[512];
char welc[] = "welcome to code jam";

int t[512][22];

int solve(int p1, int p2)
{
  if(t[p1][p2] != -1)
    return t[p1][p2];

  if(welc[p2] == '\0')
    return t[p1][p2] = 1;
  if(line[p1] == '\0')
    return t[p1][p2] = 0;
  if(line[p1] == welc[p2])
    return t[p1][p2] = (solve(p1+1, p2+1) + solve(p1+1, p2) ) % 10000;
  else
    return t[p1][p2] = solve(p1+1, p2) % 10000;
}

int main()
{
  int n;
  scanf("%d\n", &n);

  for(int i=1;i<=n;++i)
  {
    for(int a=0;a<512;++a)
      for(int b=0;b<22;++b)
        t[a][b] = -1;

    gets(line);
    printf("Case #%d: %04d\n", i, solve(0, 0));
  }

  return 0;
}

