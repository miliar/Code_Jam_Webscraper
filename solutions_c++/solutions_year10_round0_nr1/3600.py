/*
  PROG:GCJ_1
  ID:Klion
  LANG:C++
 */
#include <iostream>
using namespace std;
int main(void)
{
	  freopen("A-large.in","r",stdin);
	  freopen("A-large.txt","w",stdout);
	  int T;
	  long N,K;
	  scanf("%d",&T);
	  for(int i = 1;i < T+1;i++)
	    {
	    	scanf("%d %d",&N,&K);//input
	    	printf("Case #%d: ",i);//outpu case
	    	long ans = (1 << N)-1;//tans to binary
	    	if((ans & K) == ans)//if there is one snapper isn't on so the light can't onn
	    		printf("ON\n");
	    	else
	    		printf("OFF\n");
	    }
    return 0;
}
