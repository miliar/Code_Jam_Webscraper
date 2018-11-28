#include<cstdio>
using namespace std;
int main()
{
    FILE *in,*out;
    in=fopen("in.txt","r");
    in=fopen("A-large(2).in","r");
    out=fopen("Alarge.out","w");
    //out=stdout;
    int T,N,K;
    fscanf(in,"%d",&T);
    int caseno=1;
    while(T--)
    {
        fscanf(in,"%d %d",&N,&K);
        //use bit representation of k
        //state reset when K=2^N
        int pow2N=1<<N;
        K%=pow2N;
        //check if all bits is on
        fprintf(out,(K==pow2N-1)?"Case #%d: ON\n":"Case #%d: OFF\n",caseno++);
    }
    return 0;
}
