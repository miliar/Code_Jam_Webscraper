#include <stdio.h>
#include <string.h>
#include <stdlib.h>
using namespace std;
const int MaxN=200+5;
struct Timeable
{
    int time,bel;
};

int T,t,time,NA,NB,i,j,HH,MM,leave,arrive,AnsA,AnsB,CurA,CurB;
Timeable A[MaxN],B[MaxN],s;
FILE *In=fopen("B-large.in","r");
FILE *Out=fopen("B-large.out","w");
int main()
{
    fscanf(In,"%d",&T);
    for(t=1;t<=T;t++)
    {
        memset(A,0,sizeof(A));
        memset(B,0,sizeof(B));
        fscanf(In,"%d%d%d",&time,&NA,&NB);
        for(i=0;i<NA;i++)
        {
            fscanf(In,"%d:%d",&HH,&MM);
            leave=HH*60+MM;
            fscanf(In,"%d:%d",&HH,&MM);
            arrive=HH*60+MM;
            arrive+=time;
            A[i].time=leave;
            A[i].bel=0;
            B[i+NB].time=arrive;
            B[i+NB].bel=1;
        }
        for(i=0;i<NB;i++)
        {
            fscanf(In,"%d:%d",&HH,&MM);
            leave=HH*60+MM;
            fscanf(In,"%d:%d",&HH,&MM);
            arrive=HH*60+MM;
            arrive+=time;
            A[i+NA].time=arrive;
            A[i+NA].bel=1;
            B[i].time=leave;
            B[i].bel=0;
        }
        for(i=0;i<NA+NB;i++)
            for(j=i+1;j<NA+NB;j++)
                if (A[i].time>A[j].time || A[i].time==A[j].time && A[j].bel==1)
                {
                    s=A[i];A[i]=A[j];A[j]=s;
                }
        for(i=0;i<NA+NB;i++)
            for(j=i+1;j<NA+NB;j++)
                if (B[i].time>B[j].time || B[i].time==B[j].time && B[j].bel==1)
                {
                    s=B[i];B[i]=B[j];B[j]=s;
                }
        AnsA=0;
        CurA=0;
        for(i=0;i<NA+NB;i++)
        {
            if (A[i].bel==0)
            {
                if (CurA)
                    CurA--;
                else
                    AnsA++;
            }
            else
                CurA++;
        }
        AnsB=0;
        CurB=0;
        for(i=0;i<NA+NB;i++)
        {
            if (B[i].bel==0)
            {
                if (CurB)
                    CurB--;
                else
                    AnsB++;
            }
            else
                CurB++;
        }
        fprintf(Out,"Case #%d: %d %d\n",t,AnsA,AnsB);
    }
    return 0;
}
