#include <stdio.h>
#include <algorithm>
using namespace std;

double p[100000];
double pp[100000];

void solve(){

    int a,b;
    scanf("%d %d",&a,&b);
    double partial_p = 1;
    pp[0]=1;
    for (int i=1;i<=a;i++)  {
        scanf("%lf",&p[i]);  
   //     printf("%lf\n",p[i]);
        partial_p *= p[i];
        pp[i] = partial_p;
    } 


    double exp = pp[a]*(b-a+1) + (1-pp[a])*(b+1 + b-a+1);
    exp = min(exp,(double) 1 + b+1);
    for (int i=0;i<=a;i++){
        exp = min(pp[i]*(2*(a-i) + b-a+1) +  (1-pp[i])*(2*(a-i)+b-a+1 +b +1),exp);
    }
    printf("%lf\n",exp);
}

int main(){
    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
