#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string.h>

using namespace std;

int Abs(int a)
{
    if(a<0) return -a;
    else return a;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,n,a,O,R;
    int ans;
    char c;
    int maxO,maxR,minO,minR;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        scanf("%d",&n);
        O=1; R=1;
        maxO=1; maxR=1; minO=1; minR=1;
        ans=0;
        for(int i=0;i<n;i++)
        {
            getchar();
            scanf("%c%d",&c,&a);
            if(c=='O')
            {
                if(minO<=a&&a<=maxO)
                {
                    ans++;
                    maxR++;
                    minR--;
                    if(minR<1) minR=1;
                }
                else
                {
                    if(a>maxO)
                    {
                        ans+=a-maxO+1;
                        maxR+=a-maxO+1;
                        minR-=a-maxO+1;
                    }
                    else
                    {
                        ans+=-a+minO+1;
                        maxR+=-a+minO+1;
                        minR-=-a+minO+1;
                    }
                    if(minR<1) minR=1;
                }
                minO=a; maxO=a;
            }
            else
            {
                if(minR<=a&&a<=maxR)
                {
                    ans++;
                    maxO++;
                    minO--;
                    if(minO<1) minO=1;
                }
                else
                {
                    if(a>maxR)
                    {
                        ans+=a-maxR+1;
                        maxO+=a-maxR+1;
                        minO-=a-maxR+1;
                    }
                    else
                    {
                        ans+=-a+minR+1;
                        maxO+=-a+minR+1;
                        minO-=-a+minR+1;
                    }
                    if(minO<1) minO=1;
                }
                minR=a;
                maxR=a;
            }
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
