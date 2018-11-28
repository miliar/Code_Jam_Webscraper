#include <cstdio>
#include <cmath>

using namespace std;

int main()
{
int n,k,t;
int temp,temp2;
scanf("%d",&t);
temp2=t;
while(t--)
          {
          scanf("%d",&n); scanf("%d",&k);
          temp=pow(2,(double)n);
          if((k+1)%temp==0) printf("Case #%d: ON\n",temp2-t);
          else printf("Case #%d: OFF\n",temp2-t);
          }
return 0;
}
