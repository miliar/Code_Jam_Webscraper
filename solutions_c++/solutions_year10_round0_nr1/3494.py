#include<iostream>
using namespace std;
int main(void)
{
    FILE *fin =fopen("A-large.in","r");
    FILE *fout = fopen("A-large.out","w");
    int t,n,k;
    fscanf(fin,"%d",&t);
    for(int cas=1;cas<=t;cas++){
        fscanf(fin,"%d%d",&n,&k);
        if((k+1)%(1<<n)==0)
            fprintf(fout,"Case #%d: ON\n",cas);
        else
            fprintf(fout,"Case #%d: OFF\n",cas);
    }
    fclose(fin);
    fclose(fout);
    //system("pause");
    return 0;
}
