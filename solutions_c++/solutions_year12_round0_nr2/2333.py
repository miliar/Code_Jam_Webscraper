#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
    int i,j,k,T;
    FILE* fin = fopen("b.in","r");
    FILE* fout = fopen("b.out","w");
    
    fscanf(fin, "%d", &T);
    for (i=1;i<=T;++i)
    {
        int n,s,p,count=0;
        int point[200]={0};
        fscanf(fin,"%d %d %d",&n,&s,&p);
        for (j=0;j<=n-1;++j)
        {
            fscanf(fin,"%d",&point[j]);
            if (point[j] >= 3*p-2) count++;
            else if (point[j] >= 3*p-4 && s>0 && point[j]>0)
            {
                 s--;
                 count++;
            }
        }
        fprintf(fout, "Case #%d: %d\n",i,count);
    }
}
