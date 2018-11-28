#include <iostream>
#include <cstdio>
#include <cstring>
#define N 2000005
using namespace std;
int ok[N],ans;
int s,t;
int a[30];
int T,cnt=0;
int p[30],n,m;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("outc.txt","w",stdout);
    cin>>T;
    for (int ttt=1;ttt<=T;ttt++)
    {
        cin>>s>>t;
        int bit=0;
        int temp=s;
        while (temp!=0)
        {
            bit++;
            temp=temp/10;
        }
        cnt=0;
        memset(ok,0,sizeof(ok));
        for (int num=s;num<=t;num++)
        if (!ok[num])
        {
            if (num==1212)
               num=1212;
            temp=num;
            for (int i=0;i<bit;i++)
            {
                a[bit-i]=temp%10;
                temp=temp/10;
            }
            for (int i=bit+1;i<=bit*2;i++)
                 a[i]=a[i-bit];
            temp=0;
            m=0;
            for (int start=1;start<=bit;start++)
            {
                temp=0;
                for (int i=start;i<start+bit;i++)
                     temp=temp*10+a[i];
                if (temp>=s&&temp<=t)
                {
                    ok[temp]=true;
                    p[++m]=temp;
                }
            }
            p[0]=0;
            int tot=0;
            for (int i=1;i<m;i++)
              for (int j=i+1;j<=m;j++)
                if (p[i]>p[j])swap(p[i],p[j]);
            for (int i=1;i<=m;i++) if(p[i]!=p[i-1])tot++;
            cnt+=((tot-1)*tot)/2;
        }
        printf("Case #%d: %d\n",ttt,cnt);
    }
    return 0;
}
