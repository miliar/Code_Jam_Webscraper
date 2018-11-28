#include<cstdio>
#include<cmath>
#include<algorithm>
#include<numeric>
using namespace std;
int t,n,a[1010];
main(){
  scanf("%d",&t);
  for(int tt=1;tt<=t;tt++){
    scanf("%d",&n);
    int s=0;
    for(int i=0;i<n;i++)scanf("%d",&a[i]),s^=a[i];
    printf("Case #%d: ",tt);
    if(s){puts("NO");continue;}
    printf("%d\n",accumulate(a,a+n,0)-*min_element(a,a+n));
  }
}

