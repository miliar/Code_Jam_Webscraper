#include <cstdio>
using namespace std;

int main()
{
int t;
scanf("%d",&t);

for(int i=0;i<t;i++)
{
long long int n,k;
scanf("%d %d",&n,&k);


long long  p=1<<n;
k=k%p;
if(k==p-1)
printf("Case #%d: ON\n",i+1);
else
printf("Case #%d: OFF\n",i+1);


}

return 0;
}
