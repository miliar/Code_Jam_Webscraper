#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
int t,n;
struct node
{
    int a,b;
}p[1005];



int main()
{
    
    freopen("A-large.in","r",stdin);
    freopen("AAAlarge.out","w",stdout);
    int i,j,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%d %d",&p[i].a,&p[i].b);
        int num=0;
        for(i=0;i<n-1;i++)
            for(j=i+1;j<n;j++)
                if((p[i].a>p[j].a&&p[i].b<p[j].b)||(p[j].a>p[i].a&&p[j].b<p[i].b))
                    num++;
        printf("Case #%d: %d\n",k,num);
    }
    //system("pause");
    return 0;
}
