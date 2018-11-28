#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<iostream>
#include<string.h>
using namespace std;
int done[2000000][7];
int main()
{


    FILE* f1;
    f1=fopen("opt.txt","w");
    int i,j,tc,tc1,ll,llc,ul,k,n1,ct[50]={0},flag=0,temp,l;
    int nod=0;
    char num[4],num2[4];
    scanf("%d",&tc);
    tc1=tc;


    while(tc--)
    {
        for(i=0;i<2000000;i++)
        {
            for(j=0;j<7;j++)
            {
                done[i][j]=0;
            }
        }
        nod=0;
        scanf("%d",&ll);
        scanf("%d",&ul);
        llc=ll;
        while(ll>0)
        {
           ll=ll/10;
           nod++;
        }
        if(nod==1)
        {
            ct[tc1-tc-1]=0;
            //printf("here A");
        }
        else
        {
            //printf("here B\n");
            for(i=llc;i<ul+1;i++)
            {
                //printf("\n");
                temp=i;
                //printf("%d:",temp);
                for(l=1;l<nod;l++)
                 {
                    k=temp/pow(10,(float)(nod-1));
                    //printf("%d:",(int)pow(10,(float)(nod-1)));
                    int p = (int)ceilf(pow(10,(nod-1)));
                    temp=temp%p * 10 + k;
                    //printf("%d %d \t",p,temp);

                    n1=temp;

                    /*sprintf(num,"%d",i);

                    strcpy(strcat(substr(num,l,strlen),substr(num,0,l)),num2);
                    n1=atoi(num2);*/
                    if(i<n1 && n1>=ll && n1<=ul)
                    {
                        flag=1;
                        for(j=0;j<=7;j++)
                        {

                            if(done[i][j]==n1)
                            {

                                flag=0;
                                break;

                            }
                            else if(done[i][j]==0)
                            {
                                flag=1;
                                break;
                            }
                        }
                        //printf("\n flag %d \n",flag);
                        if(flag!=0)
                        {

                            done[i][j]=n1;
                            ct[tc1-tc-1]++;

                        }

                    }
                 }
            }
        }
    }

    for(i=1;i<=tc1;i++)
    {

        fprintf(f1,"Case #%d: %d\n",i,ct[i-1]);
    }
    cin.sync();
    cin.get();
}
