#include<cstdio>
#include<algorithm>
#include<vector>
#include<string.h>
using namespace std;
#define MAX 1001
#define MAXH 10001
int BIT[MAXH];
int N;
struct node
{
    int a,b;
    bool operator <(const node &s)const
    {
        return a>s.a;
    }
};
node Adj[MAX];
int read(int idx)
{
    int sum=0;
    while(idx)
    {
        sum+=BIT[idx];
        idx-=(idx&-idx);
    }
    return sum;
}
void update(int idx)
{
    //adds only 1
    while(idx<=MAXH)
    {
        BIT[idx]++;
        idx+=(idx&-idx);
    }
}

long long int solve()
{
    //this will use the BIT
    memset(BIT,0,sizeof(BIT));
    long long int ans=0;
    for(int i=0;i<N;i++)
    {
        ans=ans+read(Adj[i].b);
        update(Adj[i].b);
    }
    return ans;
}
int main()
{
    FILE *in,*out;
    in=fopen("in.txt","r");
    out=fopen("out.txt","w");
    int T;
    fscanf(in,"%d",&T);

    for(int cases=1;cases<=T;cases++)
    {
        fscanf(in,"%d",&N);
        for(int i=0;i<N;i++)
        {
            int ai,bi;
            fscanf(in,"%d %d",&ai,&bi);
            Adj[i]=(node){ai,bi};
        }
        sort(Adj,Adj+N);
        fprintf(out,"Case #%d: %lld\n",cases,solve());
    }
    return 0;
}
