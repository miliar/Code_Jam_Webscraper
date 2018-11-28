#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int t=0,T;
    scanf("%d",&T);
    while(t++<T)
    {
        int n,s,p,x,i,br=0,brs=0;
        scanf("%d%d%d",&n,&s,&p);
        for(i=0;i<n;i++)
        {
            scanf("%d",&x);
            int a,b,c;
            a=b=c=x/3;
            if(x%3==1)c++;
            if(x%3==2){b++;c++;}
            if(c>=p)
            {
                br++;
                continue;
            }
            if(c+1>=p&&brs<s&&x)
            {
                c++;
                b--;
                if(c-b<3)
                br++;brs++;
                continue;
            }
        }
        printf("Case #%d: %d\n",t,br);
        }
        return 0;
}
