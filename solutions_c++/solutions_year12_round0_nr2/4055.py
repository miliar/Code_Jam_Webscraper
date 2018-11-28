#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    freopen("D://B-large.in","r",stdin);
    freopen("D://out.txt","w",stdout);
    int t,s,p,n,i,temp,c,k,j,f,y;
    scanf("%d",&t);
    for(k=0;k<t;k++)
    {   c=0;f=0;y=0;
        scanf("%d %d %d",&n,&s,&p);
        int arr[n];
        for(i=0;i<n;i++)
        scanf("%d",&arr[i]);
        sort(arr,arr+n);
        for(j=0;j<n;j++)
        {   if(arr[j]>=p){
            temp=arr[j]-p;
            temp=temp/2;

            if(f==1&&arr[j]>=y&&temp>0)
            {++c;
            }
            else if(temp>=p-1 and temp>=0)
            {++c;

            f=1;
            y=arr[j];
            }
            else if(temp>=p-2&&s>=1&&temp>=0)
            {++c;

            s--;}

        }
        }
        printf("Case #%d: %d\n",k+1,c);
    }
    return 0;

}
