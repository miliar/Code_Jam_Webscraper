#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int f[110];
int n,T,s,p,a[110];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    for (int ttt=1;ttt<=T;ttt++)
    {
        cin>>n>>s>>p;
        for (int k=1;k<=n;k++)
            cin>>a[k];
        int cnt=0;
        for (int k=1;k<=n;k++)
        {
            int num1,num2,num3;
            num1=a[k]/3;
            num3=a[k]/3+1;
            num2=a[k]-num1-num3;
            if (a[k]%3==0)
            {
                num1=a[k]/3;
                num3=a[k]/3;
                num2=a[k]/3;
            }
            if (num3>=p)
            {
                cnt++;
                continue;
            }
            if (s>0)
            if (a[k]%3!=1&&num2>0)
            {
                if (num3+1>=p)
                {
                    s--;
                    cnt++;
                }
            }
        }
        printf("Case #%d: %d\n",ttt,cnt);

    }
    return 0;
}
