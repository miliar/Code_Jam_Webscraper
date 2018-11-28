#include<cstdio>
using namespace std;

int main()
{
    FILE *fin, *fout;
    fin = fopen("B-small.in","r");
    fout = fopen("B-small.out","w");
    int T,t;
    int L,P,C;
    fscanf(fin,"%d",&T);
    for (t=1; t<=T; t++)
    {
        fscanf(fin,"%d%d%d",&L,&P,&C);
        int x=0,y=L;
        while (y < P)
        {
            y *= C;
            x++;
        }
        x--;
        int ans=0;
        while (x)
        {
            x >>= 1;
            ans++;
        }
        fprintf(fout,"Case #%d: %d\n",t,ans);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
