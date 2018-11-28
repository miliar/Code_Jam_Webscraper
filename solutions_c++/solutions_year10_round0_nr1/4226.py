#include<stdio.h>


int main()
{
    int n,k;
    int i=1;
    int t;
    int power2[]={2,4,8,16,32,64,128,256,512,1024,};
    freopen("A-small-attempt1.in","rt",stdin);
    freopen("output.txt","wt",stdout);
    scanf("%d",&t);
    while(t--)
    {
      scanf("%d%d",&n,&k);
      printf("Case #%d",i);
      if((k+1)%power2[n-1]==0)
      printf(": ON\n");
      else
      printf(": OFF\n");
      i++;
    }
}
