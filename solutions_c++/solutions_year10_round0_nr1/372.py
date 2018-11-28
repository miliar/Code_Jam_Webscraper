
#include <cstring>
#include <iostream>
#include <cstdio>
using namespace std;


bool snapper[30];
int power;

int main()
{
  int n, t, k;

  cin >> t;
  for (int i = 1; i <= t; i++)
  {
    cin >> n >> k;
    printf("Case #%d: %s\n", i, (k + 1) % (1 << n) == 0 ? "ON" : "OFF");
  }

  return 0;
}
