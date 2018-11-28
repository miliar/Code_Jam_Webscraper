#include <iostream>
using namespace std;
const int maxn = 1005;
#define  LL long long
int n,r,k;
LL p[maxn];
int next[maxn];
LL Sum[maxn];
LL Tr,Tm;
void calc(int first,int head)
{
    while(1)
    {
         Tr++;Tm+=Sum[head];
         head=next[head];
         if(head==first) break;
    }
}
LL solve()
{
        int i,j,x;
        LL sum,money;
        Tr=0,Tm=0;
        int first,head;
        for(i=0;i<n;i++)
        {
            scanf("%d",&x);
            p[i]=(LL)x;
        }

        for(i=0;i<n;i++)  next[i]=-1;
        i=0;

        while(1)
        {
            j=i;sum=0;
            while(1)
            {
                if(sum+p[j]>k) break;

                sum+=p[j];
                j=(j+1)%n;

                if(j==i) break;
            }
            next[i]=j;Sum[i]=sum;
            i=j;
            if(next[i]!=-1) break;
        }

        first=i,head=i;
        calc(first,head);

        money=0;head=0;
        for(i=1;i<=r;i++)
        {
             if(head==first) break;
             money+=Sum[head];
             head=next[head];
        }
        money+=((LL)r-i+1)/Tr*Tm;
        r=(r-i+1)%Tr;
        head=first;
        for(i=1;i<=r;i++)
        {
            money+=Sum[head];
            head=next[head];
        }
        return money;
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int t,T;
    scanf("%d",&T);
//    cout<<t<<endl;
    for(t=1;t<=T;t++)
    {
        scanf("%d%d%d",&r,&k,&n);
        LL money=solve();
        printf("Case #%d: ",t);
        cout<<money<<endl;
    }
    return 0;
}
