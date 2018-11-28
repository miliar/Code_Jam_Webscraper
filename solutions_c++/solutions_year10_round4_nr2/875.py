#include <string>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
int least[2048];
int M[1024];
int m = 1000000;
int W;
bool remaining(int i)
{
  if( i >= W )
    return least[i]>= 1;
  return remaining(2*i) || remaining(2*i + 1);
}
void buy(int i)
{
  if( i >= W ){
    least[i]--;
    return;
  }
  buy(2*i);
  buy(2*i + 1);
}
int main()
{
  int c = 1;
  scanf("%d", &c);
  for(int C = 1; C <= c; C++)
    {
      int ans = 0;
      int P;
      scanf("%d", &P);
      
      W = 1<<P;
      for(int i = 0 ; i < (1<<P); i++){
	scanf("%d", M + i);
	least[i + W] = P - M[i];
      }
      for(int j = 1; j<= P; j++)
	for(int i = 0 ; i < (1<<(P-j)); i++)
	  {
	    scanf("%d", &ans);
	  }
      int ci = 1;
      int cost = 0;
      while(true)
	{
	  if(ci >= 2*W)
	    break;
	  if( remaining(ci) ){
	    buy(ci);
	    cost++;
	  }
	  ci++;
	  
	}
      printf("Case #%d: %d\n", C, cost);
    }
}

