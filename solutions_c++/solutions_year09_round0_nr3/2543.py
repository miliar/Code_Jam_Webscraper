#include<iostream>
#include<stdio.h>
#include<conio.h>

using namespace std;
int knt=0;
char test[]="welcome to code jam";
int make(char arr[],int i,int k);
int main()
{
    char arr[501];
    int casen=1;
    int i=0,k=0,n;
    FILE *fp,*fans;
    fp=fopen("prb3.txt","r");
    fans=fopen("ans3.txt","w");
    char ch;
    fscanf(fp,"%d",&n);
    fscanf(fp,"%c",&ch);
    for(int z=0;z<n;z++)
    {
            knt=0;i=0;k=0;
            fgets(arr,501,fp);
    while(arr[i]!='\0')
    {
                       if(arr[i]==test[k])
                       {
                                          make(arr,i+1,k+1);
                       }
                       i++;
    }
    fprintf(fans,"Case #%d: %04d\n",casen++,knt);
    }
    
    
    fclose(fp);
    fclose(fans);
    
}

int make(char arr[],int i,int k)
{
     if(k==19)
     {
              knt++;
              return 0;
     }
     while(arr[i]!='\0')
     {
                        if(arr[i]==test[k])
                        {
                                          make(arr,i+1,k+1);
                        }
                        i++;
                        
     }
     
}
