#include <cstdio>
using namespace std;
int main()
{
 int T;
 int t[1001];
 scanf("%d",&T);
 for(int i=1;i<=T;i++)
 {
  int N;
  scanf("%d",&N);
  for(int j=0;j<N;j++)
	  scanf("%d",&t[j]);
  int min=9999999;
  int x=0;
  int s=0;
  for(int j=0;j<N;j++)
   {if(t[j]<min)min=t[j];x^=t[j];s+=t[j];}
  if(x)
	  printf("Case #%d: NO\n",i);
  else
	  printf("Case #%d: %d\n",i,s-min);
 }
}
