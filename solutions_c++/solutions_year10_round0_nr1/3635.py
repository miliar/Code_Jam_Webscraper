#include<cstdio>
#include<vector>
typedef long int lint;
using namespace std;
lint calc_2pow_n(int n)
{
    lint x,i;
    x=1;
    i=2;
    while(n)
    {
        if(n%2)
            x*=i;
        i=i*i;
        n=n/2;
    }
    return x;
}
int main()
{
    int i,j,n,k,t;
    lint pow;
    FILE *ifp,*ofp;
    ifp =fopen("A-large.in","r");
    ofp = fopen("A-large.out", "w");
    fscanf(ifp,"%d",&t);
    for(i=1;i<=t;i++)
    {
        fscanf(ifp,"%d %d",&n,&k);
        pow=calc_2pow_n(n);
        fprintf(ofp,"Case #%d: ",i);
        if((k+1)%(pow))
            fprintf(ofp,"OFF\n");
        else
            fprintf(ofp,"ON\n");
    }
    fclose(ifp);
    fclose(ofp);
}
