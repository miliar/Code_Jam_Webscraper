#include <iostream>


using namespace std;


int snapper[31];

int main()
{
  freopen("in.txt","r", stdin);
  freopen("out.txt", "w", stdout);
  int T;

  scanf("%d", &T);

  int N, K;

  for(int i = 1; i <= T; i++)
  {

      scanf("%d %d", &N, &K);
      if(K!=0 && ((K+1) % (1<<N)  == 0))  printf("Case #%d: ON\n", i);
      else printf("Case #%d: OFF\n", i);
  }
  return 0;
}
