#include<iostream>

using namespace std;
#define min(a,b) (a < b ? (a) : (b) )
FILE *fp;
FILE *fp2;

int T,N;

int main()
{
    fp = fopen("testin.txt","r");
    fp2 = fopen("out.txt","w");
    fscanf(fp,"%d",&T);
    for(int i = 1;i <= T;++i)
    {
        fscanf(fp,"%d",&N);
        int xorsum = 0,sum = 0,minnum = 999999999;
        for(int i = 1;i <= N;++i)
        {
            int t;
            fscanf(fp,"%d",&t);
            xorsum ^= t;
            sum += t;
            minnum = min(minnum,t);
        }   
        if(xorsum == 0)
            fprintf(fp2,"Case #%d: %d\n",i,sum - minnum);
        else
            fprintf(fp2,"Case #%d: NO\n",i);
    }
    fclose(fp);
    fclose(fp2);
    return 0;    
}
