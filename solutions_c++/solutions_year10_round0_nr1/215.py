#include <string>
#include <cstring>
#include <cstdio>
#include <iostream>
using namespace std;
char * str[] = {"OFF", "ON"};
int main()
{
  int T;
  scanf("%d", &T);
  int N, K;
  int c= 1;
  while(T--)
    {
      scanf("%d %d", &N, &K);
      bool ok = true;
      for(int i = 0 ; i < N; i++)
	if(!(( K >> i)&1))
	  ok = false;
      printf("Case #%d: %s\n",c++, str[ok]);
    }
}
