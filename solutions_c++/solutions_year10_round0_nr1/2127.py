#include <cstdio>
using namespace std;

int main ()
{
    FILE *fin=fopen ("Snapper Chain.in","r");
    FILE *fout=fopen ("Snapper Chain.out","w");

    int T,t;
    int n,k;
    int x;
    
    fscanf (fin,"%d",&T);
    
    for(t=1;t<=T;t++)
    {
        fscanf (fin,"%d %d",&n,&k);
        
        x=k%(1<<n);
        
        if(x==(1<<n)-1)
            fprintf (fout,"Case #%d: ON\n",t);
        else
            fprintf (fout,"Case #%d: OFF\n",t);
    }
    return 0;
}
