#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"

int cs,c,n,k;

int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    scanf("%d%d",&n,&k);
	printf("Case #%d: ",c);
	if((k+1)%(1<<n))
	  printf("OFF\n");
	else
	  printf("ON\n");
  }  
  return 0;
}
