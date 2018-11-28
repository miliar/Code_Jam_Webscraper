// 
// File:   train.cc
// Author: mahanth
//
// Created on 17 July, 2008, 11:57 AM
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
//
// 
//
class determine
{
public:
    int areq[22];
    int breq[22];
    
    int aav[22];
    int bav[22];
    int turn;
    int notA;
    int notB;
    void determine::input(int turnAround,int nA,int nB,int adep[],int aarr[],int bdep[],int barr[])
    {
        turn=turnAround;
        sort(adep,nA);
        sort(bdep,nB);
        notA=find(nA,nB,adep,barr,areq,aav);
        notB=find(nB,nA,bdep,aarr,breq,bav);
    }
    int determine::find(int n1,int n2,int dep[],int arri[],int req[],int av[])
    {
        int check,notr;
        notr=n1;
        for(int i=0;i<n2;i++)
        {
            check=arri[i]+turn;
            for(int j=0;j<n1;j++)
              if(req[j]!=1 && av[i]!=1 && check<=dep[j])
              {
                   req[j]=1;
                   printf("%d    ",av[i]);
                   av[i]=1;
                   printf("%d %d i=%d  j=%d\n",check,dep[j],i,j);
                   notr--;
              }
        }
        return(notr);
    }
    void determine::sort(int array[],int n)
    {
        int temp,i;
        for(i=n-1;i>0;i--)
          for(int j=0;j<i;j++)
           if(array[j]>array[j+1])
            {
                temp=array[j];
                array[j]=array[j+1];
                array[j+1]=temp;
            } 
        /*for(i=0;i<n;i++)
        {
            printf("%d\n",array[i]);
        }*/
    }
};
int main(int argc, char** argv) {
    
    FILE * inFile;
    FILE * outFile;
    inFile = fopen ("A-small.in","r");
    outFile=fopen("A-small.out","w+");
        
    int n,i;
    fscanf(inFile,"%d",&n);
    determine det[102];
    for(int k=0;k<n;k++)
    {
        int turn,na,nb;
        fscanf(inFile,"%d",&turn);
        fscanf(inFile,"%d %d",&na,&nb);
        int adep[22];
        int aarr[22];
        int bdep[22];
        int barr[22];
        
        for(i=0;i<na;i++)
        {
            int h,m;
            char s1[5];
            char s2[5];
            char s3[5];
            fscanf(inFile,"%[^:]",&s1);
            fscanf(inFile,"%[:]",&s2);
            fscanf(inFile,"%s",&s3);
            h=atoi(s1);
            m=atoi(s3);
            m=h*60+m;
            adep[i]=m;
            fscanf(inFile,"%[^:]",&s1);
            fscanf(inFile,"%[:]",&s2);
            fscanf(inFile,"%s",&s3);
            h=atoi(s1);
            m=atoi(s3);
            m=h*60+m;
            aarr[i]=m;
        }
        for(i=0;i<nb;i++)
        {
            int h,m;
            char s1[5];
            char s2[5];
            char s3[5];
            fscanf(inFile,"%[^:]",&s1);
            fscanf(inFile,"%[:]",&s2);
            fscanf(inFile,"%s",&s3);
            h=atoi(s1);
            m=atoi(s3);
            m=h*60+m;
            bdep[i]=m;
            fscanf(inFile,"%[^:]",&s1);
            fscanf(inFile,"%[:]",&s2);
            fscanf(inFile,"%s",&s3);
            h=atoi(s1);
            m=atoi(s3);
            m=h*60+m;
            barr[i]=m;
        }
        det[k].input(turn,na,nb,adep,aarr,bdep,barr);
        
    }
    for(int k=0;k<n;k++ )
    {
        fprintf(outFile,"Case #%d: %d %d\n",k+1,det[k].notA,det[k].notB);
    }  
    fclose (inFile);
    fclose (outFile);    
    return (EXIT_SUCCESS);
}

