#include <fstream>
#define N 2000
using namespace std;

int main()
{
    FILE *inp,*out;
    inp=fopen("C-large.in","r");
    out=fopen("C-largeOut.out","w");
    int t,p,i,j,n,start,curr;
    int k,r;
    int cntb4,cntP;
    long long int total,sumb4,sumP;
    fscanf(inp,"%d",&t);
    int G[N],S[N],next[N];
    bool visited[N];
    for(p=0;p<t;p++)
    {
        fscanf(inp,"%d%d%d",&r,&k,&n);
        for(i=0;i<n;i++)
        {
            fscanf(inp,"%d",&G[i]);
            S[i]=G[i];
            next[i]=0;
        }
        for(i=0;i<n;i++)
        {
            j=i+1;
            while(j%n!=i)
            {
                if(S[i]+G[j%n]>k)
                    break;
                S[i]+=G[j%n];
                j++;
            }
            next[i]=j%n;
        }
        start=0;
        curr=0;
        for(i=0;i<n;i++)
            visited[i]=false;
        for(i=0;i<n;i++)
        {
            visited[curr]=true;
            curr=next[curr];
            if(visited[curr])
            {
                break;
            }
        }
        start=curr;
        sumb4=0;
        cntb4=0;
        curr=0;
        do
        {
            sumb4+=S[curr];
            cntb4++;
            curr=next[curr];
        }while(curr!=start);
        curr=start;
        sumP=0;
        cntP=0;
        do
        {
            sumP+=S[curr];
            cntP++;
            curr=next[curr];
        }while(curr!=start);
        total=0;
        if(r<=cntb4)
        {
            curr=0;
            while(r>0)
            {
                total+=S[curr];
                curr=next[curr];
                r--;
            }
        }
        else
        {
            r-=cntb4;
            total+=sumb4;
            total+=((long long int)r/cntP)*sumP;
            r%=cntP;
            curr=start;
            while(r>0)
            {
                total+=S[curr];
                curr=next[curr];
                r--;
            }
        }
        ////////////////
/*
        for(i=0;i<n;i++)
            printf("%d ",S[i]);
        printf("\n");
        for(i=0;i<n;i++)
            printf("%d ",next[i]);
        printf("\n");
        printf("%d %lld %d %lld",cntb4,sumb4,cntP,sumP);
        printf("\n");
        *//////////////////
        fprintf(out,"Case #%d: %lld\n",p+1,total);
    }

    return 0;
}
