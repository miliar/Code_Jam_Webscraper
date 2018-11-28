#include <iostream>

using namespace std;
const int N = 1005;
int g[N];
int q[N],sq[N],sumq[N];
bool B[N];
int sm;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    int R,k,n,K=1;
    scanf("%d",&T);
    while(T--)
    {
        sm = 0;
        scanf("%d%d%d",&R,&k,&n);
        memset(sumq,0,sizeof(sumq));
        for(int i=0;i<n;i++)
        {
            B[i]=0;
            scanf("%d",g+i);
            sm+=g[i];
        }
        if(sm<=k)
        {
            printf("Case #%d: %d\n",K++,sm*R);
            continue;
        }
        int ptr = 0;
        int end = 0;
        while(B[ptr]==0)
        {
            int thisPtr = ptr;
            B[ptr]=1;
            int pos = ptr;
            int tsm = 0;
            while(tsm<=k)
            {
                tsm+=g[ptr];
                if(tsm>k)break;
                ptr++;
                ptr%=n;
                if(ptr==thisPtr)break;
            }
            q[end]=thisPtr;
            sq[end++]=tsm-g[ptr];
        }
        sumq[0]=sq[0];
        for(int i=1;i<end;++i)
        {
            sumq[i]+=sumq[i-1]+sq[i];
        }
        //printf("Ptr : %d\n",ptr);
        for(int i=0;i<end;++i)
        {
            if(q[i]==ptr)
            {
                ptr=i;
                break;
            }
        }
        if(R<end)
        {
            printf("Case #%d: %d\n",K++,sumq[R-1]);
           // printf("X\n");
        }
        else
        {
            int res = 0;
            if(ptr>0)res = sumq[ptr-1];
            R-=ptr;
            int nCount = end - ptr;
            int nTimes = R/nCount;
            int nRes = R%nCount;
            res += nTimes*(sumq[end-1]-sumq[ptr-1]);
            res += sumq[ptr-1+nRes]-sumq[ptr-1];
            printf("Case #%d: %d\n",K++,res);
           // printf("XX %d %d %d %d Res:%d\n",ptr,end,nCount,nTimes,nRes);
           // for(int i=0;i<end;++i)printf("%d,%d ",sumq[i],q[i]);printf("\n");
        }

    }
    return 0;
}
