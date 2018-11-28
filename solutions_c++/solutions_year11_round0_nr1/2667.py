#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
char c[210];
int n,b[210],o[210];
int cnt1,cnt2;
int bnew,onew;
int f(int x)
{
    return x>0?x:(-x);
}
int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int cases=0;
    while(t--)
    {
        bnew=onew=1;
        cnt1=cnt2=0;
        cases++;
        scanf("%d",&n);
        int t1=0,t2=0;
        memset(b,0,sizeof(b));
        memset(o,0,sizeof(o));
        for(int i=1;i<=n;i++)
        {
            cin>>c[i];
            if(c[i]=='B')
            {
                cin>>b[++t1];
            }
            else cin>>o[++t2];
        }
        t1=t2=1;
        for(int i=1;i<=n;i++)
        {
            if(bnew!=b[t1]&&b[t1])
            {
                cnt1+=f(bnew-b[t1]);
                bnew=b[t1];
            }
            if(onew!=o[t2]&&o[t2])
            {
                cnt2+=f(onew-o[t2]);
                onew=o[t2];
            }
            if(c[i]=='B')
            {
                cnt1++;
                if(cnt2<cnt1) cnt2=cnt1;
                t1++;
            }
            else if(c[i]=='O')
            {
                cnt2++;
                if(cnt1<cnt2) cnt1=cnt2;
                t2++;
            }
        }
        printf("Case #%d: %d\n",cases,(cnt1>cnt2?cnt1:cnt2));
    }
    return 0;
}
