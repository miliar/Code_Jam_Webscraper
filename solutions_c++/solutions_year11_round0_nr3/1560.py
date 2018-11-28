#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

int t,n;
int c[1100];

int main()
{
    int i,j;
    freopen("C-large.in","r",stdin);
    freopen("cl1.txt","w",stdout);
    scanf("%d",&t);
    int cas=1;
    while(t--)
    {
        scanf("%d",&n);
        int sum=0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&c[i]);
            sum+=c[i];
        }
        sort(c,c+n);
        int a=0;
        for(i=0;i<n;i++)
            a=a^c[i];
        printf("Case #%d: ",cas++);
        if(a!=0)
            printf("NO\n");
        else
            printf("%d\n",sum-c[0]);
    }
    //system("pause");
    return 0;
}
