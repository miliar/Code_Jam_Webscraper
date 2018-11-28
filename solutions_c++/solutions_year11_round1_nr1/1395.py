#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;

int PD,PG;
int T;
long long N;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    bool temp;
    for(int t=1;t<=T;t++)
    {
        temp=false;
        scanf("%lld%d%d",&N,&PD,&PG);
        if((PD!=0&&PG==0)||(PG==100&&PD!=100)) {printf("Case #%d: Broken\n",t); continue;}
        if(N<=100)
        {
            for(long long i=1;i<=N;i++)
            {
                if(i*PD%100==0) {temp=true;break;}
            }
        }
        if(temp) printf("Case #%d: Possible\n",t);
        else printf("Case #%d: Broken\n",t);
    }
    return 0;
}
