#include<stdio.h>
#include<algorithm>
using namespace std;

FILE * in = fopen("in.in","r");
FILE * out = fopen("out.out","w");

int r , n , k , t[1001] , next[1001] , vis[1001];
long long c[1001] , visc[1001];

int main()
{
    int i , a , R , caseID = 0;
    long long ret = 0 , sum;
    fscanf(in,"%d",&R);
    while(R--)
    {
        fprintf(out,"Case #%d: ",++caseID);
        fscanf(in,"%d %d %d",&r,&k,&n);
        for(i=0;i<n;i++) fscanf(in,"%d",&t[i]);
        for(i=0;i<n;i++)
        {
            sum = 0;
            a = i;
            while((long long)sum+(long long)t[a] <= k)
            {
                sum += (long long) t[a];
                a++;
                a %= n;
                if(a == i) break;
            }
            next[i] = a;
            c[i] = sum;
        }
        memset(vis,-1,sizeof vis);
        i = 0 , a = 0 , ret = 0;
        vis[0] = 0;
        visc[0] = 0;
        while(i < r)
        {
            ret += c[a];
            i++;
            a = next[a];
            if(vis[a] != -1)
            {
                long long time = i - vis[a] , cost = ret - visc[a];
                ret += (long long) ((r-i)/(time)) * (long long) cost;
                i   += (((r-i)/(time)) * time);
            }
            vis[a] = i;
            visc[a] = ret;
        }
        fprintf(out,"%lld\n",ret);
    }
    //while(1);
    return 0;
}
