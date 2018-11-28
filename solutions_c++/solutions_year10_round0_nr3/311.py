#include<cstdio>
#include<memory>
using namespace std;

int main()
{
    FILE *fin, *fout;
    fin = fopen("C-large.in","r");
    fout = fopen("C-large.out","w");
    int T,t,r,k,n;
    int g[1002],a[1002],next[1002];
    fscanf(fin,"%d",&T);
    for (t=1; t<=T; t++)
    {
        fscanf(fin,"%d%d%d",&r,&k,&n);
        memset(g,0,sizeof(g));
        memset(a,0,sizeof(a));
        memset(next,0,sizeof(next));
        int i,j;
        for (i=0; i<n; i++)
            fscanf(fin,"%d",g+i);
        i = j = 0;
        for (i=0; i<n; i++)
        {
            a[i] = g[i];
            j = (i + 1) % n;
            while (j != i && a[i] + g[j] <= k)
            {
                a[i] += g[j];
                j =(j + 1) % n;
            }
            next[i] = j;
        }
        long long ans;
        i = 0, ans = 0;
        for (j=0; j<r; j++)
        {
            ans += a[i];
            i = next[i];
        }
        fprintf(fout,"Case #%d: %lld\n",t,ans);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
