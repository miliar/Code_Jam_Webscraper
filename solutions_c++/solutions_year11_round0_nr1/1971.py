#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int MAXN=110;

int max(int a,int b)
{
    if (a>b) return a;
    return b;
}

int min(int a,int b)
{
    if (a<b) return a;
    return b;
}

char s[MAXN];
int  b[MAXN];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j;
    int n;
    int t,cas,p1,p2,t1,t2,last;
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%c",&s[i]);
            while(s[i]!='O'&&s[i]!='B') scanf("%c",&s[i]);
            scanf("%d",&b[i]);
        }
        p1=1;
        p2=1;
        t1=0;
        t2=0;
        if (s[0]=='O')
        {
            t1=max(b[0],p1)-min(b[0],p1)+1;
            p1=b[0];
            last=0;
        }
        else
        {
            t2=max(b[0],p2)-min(b[0],p2)+1;
            p2=b[0];
            last=1;
        }
        for(i=1;i<n;i++)
        {
            if (last==0 && s[i]=='O')
            {
                t1+=(max(b[i],p1)-min(b[i],p1)+1);
                p1=b[i];
                last=0;
            }
            else if (last==0 && s[i]=='B')
            {
                t2=max(t1+1,t2+max(b[i],p2)-min(b[i],p2)+1);
                p2=b[i];
                last=1;
            }
            else if (last==1 && s[i]=='O')
            {
                t1=max(t2+1,t1+=(max(b[i],p1)-min(b[i],p1)+1));
                p1=b[i];
                last=0;
            }
            else
            {
                t2+=(max(b[i],p2)-min(b[i],p2)+1);
                p2=b[i];
                last=1;
            }

          //  cout<<p1<<" "<<t1<<" "<<p2<<" "<<t2<<endl;

        }
        printf("Case #%d: ",cas);
        printf("%d\n",max(t1,t2));
    }
    return 0;
}
