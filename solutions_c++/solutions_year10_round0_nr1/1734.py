#include <fstream>

using namespace std;

int main()
{
    FILE *inp,*out;
    inp=fopen("A-large.in","r");
    out=fopen("A-largeOut.out","w");
    int t,p,i,n;
    long long int k;
    fscanf(inp,"%d",&t);
    long long int T[31];
    T[1]=1;
    for(i=2;i<31;i++)
        T[i]=(T[i-1]<<1)+1;
    for(p=0;p<t;p++)
    {
        fscanf(inp,"%d%lld",&n,&k);
        fprintf(out,"Case #%d: ",p+1);
        if(k%(T[n]+1)==T[n])
            fprintf(out,"ON\n");
        else
            fprintf(out,"OFF\n");
    }
    return 0;
}
