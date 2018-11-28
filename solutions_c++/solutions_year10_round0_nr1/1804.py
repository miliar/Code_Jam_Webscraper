#include <cstdio>

int K, N, T;

bool test()
{
    int mask = (1<<N)-1;
    return (K&mask) == mask;
}

int main()
{
  scanf("%d", &T);
  for(int i=1;i<=T; ++i)
  {
	scanf("%d%d", &N, &K);
	printf("Case #%d: %s\n",i, test() ? "ON" : "OFF");
  }
  return 0;
}