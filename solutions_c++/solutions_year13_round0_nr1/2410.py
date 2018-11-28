#include <iostream>
#include <stdio.h>
FILE *fin = fopen("A-large-practice.in","r");
FILE *fout = fopen("output.txt","w");
using namespace std;

int main()
{
    int n;
    fscanf(fin,"%d",&n);
    for(int i=0;i<n;i++)
    {
        int credit,item,il[2000];
        fscanf(fin,"%d",&credit);
        fscanf(fin,"%d",&item);
        int j,k;
        for(j=0;j<item;j++)
        {
            fscanf(fin,"%d",&il[j]);
        }
        int maxc=0,mp1,mp2;
        for(j=0;j<item;j++)
        {
            for(k=j+1;k<item;k++)
            {
                if(maxc<il[j]+il[k]&&il[j]+il[k]<=credit)
                {
                    maxc=il[j]+il[k];
                    mp1=j;
                    mp2=k;
                }
            }
        }
        fprintf(fout,"Case #%d: %d %d\n",i+1,mp1+1,mp2+1);
    }
    return 0;
}
