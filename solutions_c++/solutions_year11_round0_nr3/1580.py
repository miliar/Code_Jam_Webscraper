#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;
int N,a[1001],sum=0,T;
int main()
{
    freopen("test.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for(int r = 1;r<=T;r++)
    {
        scanf("%d",&N);
        sum = 0;
        for(int i=0;i<N;i++)
          scanf("%d",&a[i]);
        sort(a,a+N);
        int f = 0;
        for(int i=1;i<N;i++)
          sum+=a[i],f = f^a[i];
        printf("Case #%d: ",r);
        if(f==a[0])
          printf("%d",sum);
        else
          printf("NO");
        printf("\n");
    }
    //system("pause");
    return 0;
}
