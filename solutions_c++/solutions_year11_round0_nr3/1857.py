#include <cstdio>
unsigned int t,n,c[1000];
int main()
{
    FILE *fin,*fout;
    fin=fopen("in.txt","r");
    fout=fopen("out.txt","w");
    fscanf(fin,"%d",&t);
    for (int xht=1;xht<=t;xht++)
    {
        int min=100000000,sum=0;
        unsigned int toxor=0;
        fscanf(fin,"%d",&n);
        for (int xhn=0;xhn<n;xhn++)
            fscanf(fin,"%d",&c[xhn]);
        for (int xhn=0;xhn<n;xhn++)
            toxor^=c[xhn];
        if (toxor!=0)
        {
           fprintf(fout,"Case #%d: NO\n",xht);
        }
        else
        {
            for (int xhn=0;xhn<n;xhn++)
            {
                sum+=c[xhn];
                min=(min<c[xhn]?min:c[xhn]);
            }
            min=sum-min;
            fprintf(fout,"Case #%d: %d\n",xht,min);
        }
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
