
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main()
{
    int c,d,i,j,k,p,n,t,pos,tag;
    char tra;
    char con1[200],con2[200],con3[200],opp1[200],opp2[200],list[200];
    FILE * fp1,* fp2;
    fp1=fopen("B-small-attempt0.in","r");
    fp2=fopen("2.txt","w");
    fscanf(fp1,"%d",&t);
    for (i=1;i<=t;i++)
    {
        fscanf(fp1,"%d%c",&c,&tra);
        for (j=1;j<=c;j++) fscanf(fp1,"%c%c%c",&con1[j],&con2[j],&con3[j]);
        fscanf(fp1,"%d%c",&d,&tra);
        for (j=1;j<=d;j++) fscanf(fp1,"%c%c",&opp1[j],&opp2[j]);
        fscanf(fp1,"%d%c",&n,&tra);
        pos=0;
        for (j=1;j<=n;j++)
        {
            pos++;
            fscanf(fp1,"%c",&list[pos]);
            tag=1;
            for (k=1;k<=c;k++)
                if (((con1[k]==list[pos])&&(con2[k]==list[pos-1]))||(con1[k]==list[pos-1])&&(con2[k]==list[pos]))
                {
                      pos--;
                      list[pos]=con3[k];
                      tag=0;
                      break;
                      }
            if (tag)
                for (k=1;k<pos;k++)
                    for (p=1;p<=d;p++)
                        if (((opp1[p]==list[pos])&&(opp2[p]==list[k]))||((opp1[p]==list[k])&&(opp2[p]==list[pos])))
                            pos=0;  
            }
        fprintf(fp2,"Case #%d: [",i);
        if (pos)
        {
                fprintf(fp2,"%c",list[1]);
                for (j=2;j<=pos;j++) fprintf(fp2,", %c",list[j]);
                }
        fprintf(fp2,"]\n");
        }
    fclose(fp1);
    fclose(fp2);
    return 0;
    }
