#include <iostream>

using namespace std;

int main()
{
    int t;
    FILE* fp=fopen("ain.txt","r");
    FILE* fpp=fopen("aout.txt","w");
    fscanf(fp,"%d",&t);
    for(int i=1;i<=t;i++)
    {
        int n,k;bool f=1;
        fscanf(fp,"%d%d",&n,&k);
        int m=(1<<n);
        k%=m;
        for(int j=0;j<n;j++)
          if(((1<<j)&k)==0){f=0;break;}
        fprintf(fpp,"Case #%d: ",i);
        if(f)fprintf(fpp,"ON\n");
        else fprintf(fpp,"OFF\n");
    }
    fclose(fp);
    fclose(fpp);
}
