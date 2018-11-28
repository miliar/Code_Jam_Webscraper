#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<math.h>
using namespace std;

int t,n,l,h;
int a[1000];



int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("cs1.txt","w",stdout);
    int i,j;
    scanf("%d",&t);
    int cnt=1;
    while(t--)
    {
        scanf("%d %d %d",&n,&l,&h);
        for(i=0;i<n;i++)
            scanf("%d",&a[i]);
        printf("Case #%d: ",cnt++);
        int flag=0;
        for(i=l;i<=h;i++)
        {
            for(j=0;j<n;j++)
            {
                if(i%a[j]==0||a[j]%i==0)
                    continue;
                else
                    break;
            }
            if(j==n)
            {
                flag=1;
                break;
            }
        }
        if(flag==0)
            printf("NO\n");
        else
            printf("%d\n",i);
        
        
    }
    //system("pause");
    return 0;
}
