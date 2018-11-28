#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

#define minn(x,y) ((x)<(y)?(x):(y))
#define maxx(x,y) ((x)>(y)?(x):(y))

int T,N,a[105];

char str[105][5];

int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>N;
        for(int i=1;i<=N;i++)
        {
            scanf("%s%d",str[i],a+i);
        }

        int ans=0,blue=1,org=1,tb=0,to=0;
        for(int i=1;i<=N;i++)
        {
            if(str[i][0]=='B')
            {
                if(tb<abs(a[i]-blue)+1)
                {
                    ans+=(abs(a[i]-blue)+1-tb);
                    to+=(abs(a[i]-blue)+1-tb);
                }
                else
                {
                    ans++;
                    to++;
                }
                tb=0;
                blue=a[i];
            }
            else
            {
                if(to<abs(a[i]-org)+1)
                {
                    ans+=(abs(a[i]-org)+1-to);
                    tb+=(abs(a[i]-org)+1-to);
                }
                else
                {
                    ans++;
                    tb++;
                }
                to=0;
                org=a[i];
            }
        }

        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}

































