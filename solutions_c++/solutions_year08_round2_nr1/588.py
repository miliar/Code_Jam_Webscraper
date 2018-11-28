#include <iostream>
#include <cstdlib>
using namespace std;

struct ss{long long x,y;}q[100004];

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    long long N,n,A,B,C,D,X,Y,M;
    long long cas,sen,t,tt,ttt;
    long long p;
    scanf("%I64d",&N);
    for(sen=1;sen<=N;++sen)
    {
        p=0;
        scanf("%I64d%I64d%I64d%I64d%I64d%I64d%I64d%I64d",&n,&A,&B,&C,&D,&X,&Y,&M); 
        q[0].x=X;
        q[0].y=Y;    
        for(t=1;t<=n-1;t++)
        {
            q[t].x=(A * q[t-1].x + B)% M;    
            q[t].y=(C * q[t-1].y + D) % M;
        }
        
        for(t=0;t<=n-3;++t)
        for(tt=t+1;tt<=n-2;++tt)
        for(ttt=tt+1;ttt<=n-1;++ttt)
            if((q[t].x+q[tt].x+q[ttt].x)%3==0 && (q[t].y+q[tt].y+q[ttt].y)%3==0)
                p++;
        printf("Case #%I64d: %I64d\n",sen,p);
    }
    
    
    //system("pause");
    return 0;
}
