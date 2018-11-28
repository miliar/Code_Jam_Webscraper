#include<iostream>
using namespace std;
#include<algorithm>
#include<stdlib.h>
const int MAXN = 130;
struct boat
{
   long start,end;
}a[MAXN],b[MAXN];       
long na,nb;
long t;

bool visiteda[MAXN],visitedb[MAXN];

int cmp1(const void *a,const void *b)
{
   boat *c = (boat *)a;
   boat *d = (boat *)b;
   return c->start-d->start;
}

int cmp2(const void *a,const void *b)
{
   boat *c = (boat *)a;
   boat *d = (boat *)b;
   return -(c->end-d->end);
}
          
int main()
{
    long val,x,y;
    long caseamount;
    long casenum = 1;
    long i,j,k;
    long ansa,ansb;
    freopen("Bac.txt","w",stdout);
    
    scanf("%ld",&caseamount);
    
    while(caseamount--)
    {
    scanf("%ld",&t);
    scanf("%ld%ld",&na,&nb);
    for(i=0;i<na;i++)
    {                    
    scanf("%ld%*c%ld",&x,&y);
    a[i].start = x*60+y;
    scanf("%ld%*c%ld",&x,&y);
    a[i].end = x*60+y; 

    }
    for(i=0;i<nb;i++)
     {
    scanf("%ld%*c%ld",&x,&y);
    b[i].start = x*60+y;
    scanf("%ld%*c%ld",&x,&y);
    b[i].end = x*60+y; 
    }

   /* for(i=0;i<na;i++)
    printf("%ld %ld\n",a[i].start,a[i].end);
    printf("\n");
    for(i=0;i<nb;i++)
    printf("%ld %ld\n",b[i].start,b[i].end);
    printf("\n");
    */
   // qsort(a,na,sizeof(a[0]),cmp1);
   // qsort(b,nb,sizeof(b[0]),cmp2);
    

    
    for(i=0;i<na;i++)
        visiteda[i] = false;              
     
    for(i=0;i<nb;i++)
        visitedb[i] = false;
          
    /*for(i=j=0,ansa = na;i<na&&j<nb;)
    {
        for(k=j;k<nb&&b[k].end+t<a[i].start;k++);
        
        if(k<nb&&b[k].end+t>=a[i].start)
           {
            ansa--;
            i++;
            }
            
        j = ++k;
                                                       
    }*/
    qsort(a,na,sizeof(a[0]),cmp1);
    qsort(b,nb,sizeof(b[0]),cmp2);
    
    /*
    for(i=0;i<na;i++)
    printf("%ld %ld\n",a[i].start,a[i].end);
    printf("\n");
    for(i=0;i<nb;i++)
    printf("%ld %ld\n",b[i].start,b[i].end);
    printf("\n");

    */
    
  /*  for(i=j=0,ansb = nb;i<nb&&j<na;)
    {
       for(k=j;k<na&&a[k].end+t<b[i].start;k++);
       
       if(k<na&&a[k].end+t>=b[i].start)
       {
         ansb--;
         i++;
         }
     
     j = ++k;
     }*/
     for(i=0,ansa = na;i<na;i++)
     {
        for(j=0;j<nb;j++)
         if(b[j].end+t<=a[i].start&&!visitedb[j])
         {
             visitedb[j] = true;
             ansa--;
             break;
             }
             }
       
       
     
  
    qsort(b,nb,sizeof(b[0]),cmp1);
    qsort(a,na,sizeof(a[0]),cmp2);
    
   /*     for(i=0;i<na;i++)
    printf("%ld %ld\n",a[i].start,a[i].end);
    printf("\n");
    for(i=0;i<nb;i++)
    printf("%ld %ld\n",b[i].start,b[i].end);
    printf("\n");*/
    
       for(i=0,ansb = nb;i<nb;i++)
       {
         for(j=0;j<na;j++)
          if(a[j].end+t<=b[i].start&&!visiteda[j])
          {
            visiteda[j] = true;
            ansb--;
            break;
            }
            }
        printf("Case #%ld: %ld %ld\n",casenum++,ansa,ansb);
                                                                                                                                     
     }                                                   
   //system("pause");
    return 0;
}
