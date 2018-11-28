#include<iostream>
#include<stdio.h>
#include<conio.h>
#include<malloc.h>

using namespace std;



struct node 
{
       bool alpha[26];
       struct node *next[26];
};

typedef struct node NODE;

int chk(NODE *first,int k,int knt); 
int tknt=0,n,d,l;
char arr[100];
int main()
{
    NODE *a,*current,*first;
    int i,j,k;
    a=(NODE *)malloc(sizeof(NODE));
    first=current=a;
    for(i=0;i<26;i++)
    {
                     a->alpha[i]=false;
                     a->next[i]=0;
    }
    
    FILE *fp,*fans;
    fp=fopen("prb1.txt","r");
    fans=fopen("ans1.txt","w");
    
    fscanf(fp,"%d %d %d",&l,&d,&n);
    
    for(i=0;i<d;i++)
    {
                    fscanf(fp,"%s",arr);
                    for(j=0;j<l;j++)
                    {
                                   current->alpha[arr[j]-'a']=true;
                                   if(current->next[arr[j]-'a']==0)
                                   {
                                                                     a=(NODE*)malloc(sizeof(NODE));
                                                                                                                         
                                                                     for(k=0;k<25;k++)
                                                                     {
                                                                                     a->alpha[k]=false;
                                                                                   a->next[k]=0;
                                                                     }
                                                                     current->next[arr[j]-'a']=a;                               
                                                                     current=a;
                                   }
                                   else
                                   {
                                       current=current->next[arr[j]-'a'];
                                   }         
                    }              
                    current=first;
    }
    
    for(i=0;i<n;i++)
    {
                    fscanf(fp,"%s",arr);
                    chk(first,0,1);
                    fprintf(fans,"Case #%d: %d",i+1,tknt);
                    fprintf(fans,"\n");
                    tknt=0;
    }
    fclose(fp);
    fclose(fans);
}

int chk(NODE *first,int k,int knt)
{
     int i=k,j;
     if(arr[i]=='\0')
     return 0;
                if(arr[i]=='(')
                {
                               i++;
                               j=i;
                               while(arr[j]!=')')
                               j++;
                while(arr[i]!=')')
                {
                                  if(first->alpha[arr[i]-'a']==true)
                                  {
                                                                    if(knt==l)
                                                                    tknt++;
                                                                    chk(first->next[arr[i]-'a'],j+1,knt+1);
                                  }
                                  i++;
                }
                }
                else
                {
                                  if(first->alpha[arr[i]-'a']==true)
                                  {
                                                                    if(knt==l)
                                                                    tknt++;
                                                                    chk(first->next[arr[i]-'a'],i+1,knt+1);
                                  }
                                  i++;
                }                                 
}
