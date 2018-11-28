#include<iostream>

using namespace std;

FILE*fp;
FILE*fp2;

int T,n,a[10000];
int ans;

int solve()
{
    int ret = 0;
    for(int i = 1;i <= n;++i)
    {
        if(a[i] != i)
            ++ret;     
    }
    return ret;
}

int main()
{
    fp = fopen("testin.txt","r");
    fp2 = fopen("out.txt","w");
    fscanf(fp,"%d",&T);
    for(int i = 1;i <= T;++i)
    {
        fscanf(fp,"%d",&n);
        for(int i = 1;i <= n;++i)
            fscanf(fp,"%d",&a[i]);
        ans = solve();
        fprintf(fp2,"Case #%d: %d.000000\n",i,ans);
    }
    fclose(fp);
    fclose(fp2);
    return 0;    
}
