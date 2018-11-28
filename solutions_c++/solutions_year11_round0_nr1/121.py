#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<iostream>
using namespace std;
char c[1005];
int p[1005];
int o1[1005];
int o2[1005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        int h1=0,e1=0,h2=0,e2=0;
        for(int i=0;i<n;i++)
        {
            cin>>c[i]>>p[i];
            if(c[i]=='O')
                o1[e1++]=p[i];
            else
                o2[e2++]=p[i];
        }
        int cnt=0;
        int p1=1,p2=1;
        for(int i=0;i<n;i++)
        {
            if(c[i]=='O')
            {
                if(abs(p1-o1[h1])<abs(p2-o2[h2]))
                {
                    cnt+=abs(p1-o1[h1])+1;
                    if(p2<o2[h2])
                        p2+=abs(p1-o1[h1])+1;
                    else
                        p2-=abs(p1-o1[h1])+1;
                    p1=o1[h1];

                }
                else
                {
                    cnt+=abs(p1-o1[h1])+1;
                    p1=o1[h1];
                    p2=o2[h2];
                }
                h1++;
            }
            else
            {
                if(abs(p2-o2[h2])<abs(p1-o1[h1]))
                {
                    cnt+=abs(p2-o2[h2])+1;
                    if(p1<o1[h1])
                        p1+=abs(p2-o2[h2])+1;
                    else
                        p1-=abs(p2-o2[h2])+1;
                    p2=o2[h2];

                }
                else
                {
                    cnt+=abs(p2-o2[h2])+1;
                    p2=o2[h2];
                    p1=o1[h1];
                }
                h2++;
            }
        }
        printf("Case #%d: %d\n",++cas,cnt);
    }
    return 0;
}
