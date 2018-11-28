#include<string>
#include<cstdio>
using namespace std;
int main()
{
    float n,x,br;
    int i,t,j;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        br=0;
        scanf("%f",&n);
        for(j=0;j<n;j++)
        {
            scanf("%f",&x);
            if(x==j+1)br++;
        }
        printf("Case #%d: ",i+1);
        printf("%.6f\n",n-br);
    }
}
