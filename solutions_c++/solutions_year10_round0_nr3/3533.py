#include<iostream>
#include<queue>
using namespace std;
int i,t,r,k,n,top,back,sum,s,ccase,tt;
struct node
{
    int num;
    int next;
    int pre;
}a[1003];
int main()
{
    freopen("hh1.txt","r",stdin);
    freopen("hh2.txt","w",stdout);
    scanf("%d",&t);
    ccase=0;
    while(t--)
    {
        scanf("%d%d%d",&r,&k,&n);
		tt=0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i].num);
			tt+=a[i].num;
            if(i!=0)a[i].pre=i-1;
            if(i!=n)a[i-1].next=i;   
        }
        a[0].pre=n-1;
        a[n-1].next=0;
        top=0;back=n-1;sum=0;
        for(i=1;i<=r;i++)
        {
            s=k;
			if(tt<=k){sum+=tt;continue;}
            while(a[top].num<=s)
            {
                s-=a[top].num;
                sum+=a[top].num;
                top=(top+1)%n;
                back=(back+1)%n;
            }
        }
        printf("Case #%d: %d\n",++ccase,sum);
    }
    return 0;
}
