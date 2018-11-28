#include<cstdio>
#include<algorithm>
#include<vector>
#include<string.h>
using namespace std;
#define MAX 1001
#define MAXH 10001
int table[MAXH];
int N;
struct elem
{
    int a,b;
    bool operator <(const elem &s)const
    {
        return a>s.a;
    }
};
elem Mat[MAX];
int read(int idx)
{
    int sum=0;
    while(idx)
    {
        sum+=table[idx];
        idx-=(idx&-idx);
    }
    return sum;
}
void update(int idx)
{
    while(idx<=MAXH)
    {
        table[idx]++;
        idx+=(idx&-idx);
    }
}

long long int solve()
{
    memset(table,0,sizeof(table));
    long long int ans=0;
    for(int i=0;i<N;i++)
    {
        ans=ans+read(Mat[i].b);
        update(Mat[i].b);
    }
    return ans;
}
int main()
{
    FILE *in,*out;
    in=fopen("A-in.txt","r");
    out=fopen("A-out.txt","w");
    int T;
    fscanf(in,"%d",&T);

    for(int cases=1;cases<=T;cases++)
    {
        fscanf(in,"%d",&N);
        for(int i=0;i<N;i++)
        {
            int ai,bi;
            fscanf(in,"%d %d",&ai,&bi);
            Mat[i]=(elem){ai,bi};
        }
        sort(Mat,Mat+N);
        fprintf(out,"Case #%d: %lld\n",cases,solve());
    }
    return 0;
}
