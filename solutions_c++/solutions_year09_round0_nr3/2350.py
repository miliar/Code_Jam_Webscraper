#include <iostream>
#include <cstring>
#define m 19

using namespace std;

int n,i,j,k,l;
int mic[25][1005];
char txt[100];
char in[1005];

int main()
{
    FILE *fin=fopen("C-small-attempt0.in","r");
    FILE *fin2=fopen("welcome.txt","r");
    FILE *fout=fopen("C-small.out","w");
    fgets(txt,105,fin2);
    printf("%c\n\n",txt[m-1]);
    fscanf(fin,"%d\n",&n);
    for(i=1;i<=n;i++)
    {
        fgets(in,1005,fin);
        l=strlen(in);
        for(j=0;j<=l;j++)
        {
            for(k=0;k<=m;k++)
            {
                mic[k][j]=0;
            }
        }
        for(j=0;j<=l;j++)
        {
            mic[m][j]=1;
        }
        for(j=m-1;j>=0;j--)
        {
            for(k=0;k<l;k++)
            {
                if(in[k]==txt[j])
                {
                    mic[j][k]=mic[j+1][k+1];
                }
            }
            for(k=l-1;k>=0;k--)
            {
                mic[j][k]+=mic[j][k+1];
                if(mic[j][k]>=1000)
                mic[j][k]-=1000;
            }
        }
        fprintf(fout,"Case #%d: ",i);
        if(mic[0][0]<10)
        {
            fprintf(fout,"000");
        }
        else if(mic[0][0]<100)
        {
            fprintf(fout,"00");
        }
        else if(mic[0][0]<1000)
        {
            fprintf(fout,"0");
        }
        fprintf(fout,"%d\n",mic[0][0]);
    }
    return 0;
}
