#include <iostream>
using namespace std;
char original[5005][20];
char a[400];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("xxout.out","w",stdout);
    int i,j;
    int l,d,n,t;
    bool flag;
    while(scanf("%d%d%d",&l,&d,&n)!=-1)
    {
        for(i=0;i<d;i++)
        {
            scanf("%s",original[i]);
        }
        for(t=1;t<=n;t++)
        {
            scanf("%s",a);
            int pos=0;
            int end=0;
            int zi;
            int cnt=0;
            for(i=0;i<d;i++)
            {
                flag=1;
                pos=0;
                end=0;
                for(zi=0;zi<l;zi++)
                {
                    if(a[pos]=='(')
                    {
                        end=pos+2;
                        while(a[end]!=')')
                        {
                            end++;
                        }
                        for(j=pos+1;j<end;j++)
                        {
                            if(a[j]==original[i][zi])
                                break;
                        }
                        if(j==end)
                        {
                            flag=0;
                            break;
                        }
                        pos=end+1;
                    }
                    else
                    {
                        if(a[pos]!=original[i][zi])
                        {
                            flag=0;
                            break;
                        }
                        pos++;
                    }
                }
                if(flag)
                {
                   cnt++;
                }
            }
            printf("Case #%d: %d\n",t,cnt);
        }

    }
    return 0;
}
