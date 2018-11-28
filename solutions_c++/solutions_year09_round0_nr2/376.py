#include<algorithm>
#include<stdio.h>
using namespace std;

FILE * in = fopen("in.in","r");
FILE * out = fopen("out.out","w");

int t[101][101] , ret[101][101] , cur , n , m;

int solve(int x,int y)
{
    if(ret[x][y] != -1) return ret[x][y];
    int mi = 1 << 30 , mix , miy;
    if(x > 0 && t[x-1][y] < mi) mi = t[x-1][y] , mix = x-1 , miy = y;
    if(y > 0 && t[x][y-1] < mi) mi = t[x][y-1] , mix = x , miy = y-1;
    if(y < m-1 && t[x][y+1] < mi) mi = t[x][y+1] , mix = x , miy = y+1;
    if(x < n-1 && t[x+1][y] < mi) mi = t[x+1][y] , mix = x+1 , miy = y;
    if(mi >= t[x][y]){cur++; return ret[x][y] = cur;}
    return ret[x][y] = solve(mix,miy);
}

int main()
{
    int i , a , k , c = 0;
    fscanf(in,"%d",&k);
    while(k)
    {
        k-- , c++;
        fscanf(in,"%d %d",&n,&m);
        for(i=0;i<n;i++)
            for(a=0;a<m;a++)
                fscanf(in,"%d",&t[i][a]);
        memset(ret,-1,sizeof ret);
        cur = -1;
        for(i=0;i<n;i++)
            for(a=0;a<m;a++)
                solve(i,a);
        fprintf(out,"Case #%d:\n",c);
        for(i=0;i<n;i++)
        {
            for(a=0;a<m-1;a++)
                fprintf(out,"%c ",ret[i][a] + 'a');
            fprintf(out,"%c\n",ret[i][m-1] + 'a');
        }
    }
    return 0;
}
