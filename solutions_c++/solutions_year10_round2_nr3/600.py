#include<stdio.h>
#include<algorithm>
using namespace std;
#define MOD 100003

FILE * in = fopen("in.in","r");
FILE * out = fopen("out.out","w");

int n , arrc , ret[30] , vis[30];

int check(int mask)
{
    int i , a = -1;
    arrc = 1;
    memset(vis,-1,sizeof vis);
    for(i=0;i<=24;i++)
        if(mask & (1 << i)) a = i+2 , vis[i+2] = arrc++;
    return a;
}

int main()
{
    int i , a , k , caseID = 0 , ind;
    for(i=1;i<=(1<<24);i++)
    {
        a = check(i);
        if(a < 2) continue;
        ind = a ;
        while(1)
        {
            if(vis[ind] == -1) break;
            ind = vis[ind];
        }
        if(ind == 1) ret[a]++ , ret[a] %= MOD;
    }
    fscanf(in,"%d",&k);
    while(k--)
    {
        fprintf(out,"Case #%d: ",++caseID);
        fscanf(in,"%d",&n);
        fprintf(out,"%d\n",ret[n]);
    }
    return 0;
}
