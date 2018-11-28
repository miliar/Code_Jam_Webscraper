#include<cstdio>
#include<memory>
using namespace std;

int main()
{
    FILE *fin, *fout;
    fin = fopen("A-large.in","r");
    fout = fopen("A-large.out","w");
    int T,t;
    int n,a[1001],b[1001];
    fscanf(fin,"%d",&T);
    for (t=1; t<=T; t++)
    {
        fscanf(fin,"%d",&n);
        int i,j;
        for (i=0; i<n; i++)
            fscanf(fin,"%d%d",a+i,b+i);
        int ans=0;
        for (i=0; i<n-1; i++)
            for (j=i+1; j<n; j++)
            {
                if ( (a[i]-a[j])*(b[i]-b[j]) < 0 )
                    ans++;
            }
        fprintf(fout,"Case #%d: %d\n",t,ans);
    }
    return 0;
}
