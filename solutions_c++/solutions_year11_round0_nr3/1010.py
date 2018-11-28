#include <cstdio>
#include <algorithm>
using namespace std;
typedef unsigned long long ULL;
typedef long long LL;
long mas[1024];
int main()
{
    int a,b;
    int t,n;
    LL sum;
    ULL ssum=0;
    freopen("inc.txt","r",stdin);
    freopen("outc.txt","w",stdout);
    scanf("%d",&t);
    for(int c=0;c<t;c++)
    {
        sum=0;
        ssum=0;
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%ld",&mas[i]);
            sum^=mas[i];
            ssum+=mas[i];
        }
        ssum-=*min_element(mas,mas+n);
        if(sum) printf("Case #%d: NO\n",c+1);
        else{
            printf("Case #%d: ",c+1);
            printf("%llu\n",ssum);
        }
    }
    return 0;
}
