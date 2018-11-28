#include<stdio.h>
#include<string.h>
#include<fstream>
using namespace std;
int main()
{
int t,n,s,p,i,j,min1,min2,cnt;
int a[200];
freopen("C:\\Users\\Sameer\\Desktop\\B-small-attempt1.in","r",stdin);
freopen("C:\\Users\\Sameer\\Desktop\\output.out","w",stdout);
scanf("%d",&t);
for(j=1;j<=t;j++)
{
    cnt=0;
    scanf("%d%d%d",&n,&s,&p);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    if(p==0)
    {
        printf("Case #%d: %d\n",j,n);
        continue;
    }
    min1=3*p-2;
    min2=min1-2;
    for(i=0;i<n;i++)
    {
        if(a[i]>=min1)
            cnt++;
        else if(a[i]>=min2&&s>0&&a[i]>p)
        {
            s--;
            cnt++;
        }
    }
    printf("Case #%d: %d\n",j,cnt);
}
return 0;
}
