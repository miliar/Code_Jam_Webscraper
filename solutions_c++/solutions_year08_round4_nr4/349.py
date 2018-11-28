/*
TASK: D-perm
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>

using namespace std;

int n,k;
FILE *fin,*fout;
char buff[50100];
char biff[50100];
int uu[20]={0,1,2,3,4,5,6,7,8,9};
int facto[10]={1,1,2,6,24,120,720,5040};

int main()
{
    int sss,ss;
    int i,j,l;
    fin = fopen("D-small-attempt0.in","r");
    fout = fopen("D-small.out","w");
    fscanf(fin,"%d",&sss);
    for(ss=1;ss<=sss;ss++)
    {
        printf("--%d--\n",ss);
        fscanf(fin,"%d",&k);
        fscanf(fin,"%s",buff);
        n = strlen(buff);
        int cnt;
        int mincnt; mincnt = 123456768;
        for(i=0;i<facto[k];i++)
        {
            for(j=0;j<n/k;j++)
            {
                for(l=0;l<k;l++)
                {
                    biff[j*k+l] = buff[j*k+uu[l]];
                }
            }
            cnt = 0;
            for(j=1;j<n;j++) if(biff[j]!=biff[j-1]) cnt++;
            cnt++;
            if(mincnt>cnt) mincnt = cnt;
            next_permutation(uu,uu+k);
        }
        fprintf(fout,"Case #%d: %d\n",ss,mincnt);
    }
    system("PAUSE");
    return 0;
}
