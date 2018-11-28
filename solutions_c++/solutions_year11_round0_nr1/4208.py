#include<stdio.h>
#include<vector>
#include<conio.h>
using namespace std;

struct T
{
    char r;
    int t;
    T(char _r,int _t)
    {
       r=_r;
       t=_t;
    }
};   

int t=1,n,tests,mint,i,currb,curro,nextb,nexto;
char curr;
vector<T> a;
void next(int x);
void inc();

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("bot_trust.out","w",stdout);
    scanf("%d",&tests);
    while(t<=tests)
    {       
       scanf("%d",&n);
       a.clear();
       for(i=0;i<n;i++)
       {
           char temp;
           int c;
           scanf(" %c %d",&temp,&c);
           a.push_back(T(temp,c));
       }           
       currb=0;
       curro=0;       
       i=0;       
       mint=0;
       while(i<n)
       {
           curr=a[i].r;
           next(i);
           //printf("%d %d %d %d : %d\n",nexto,nextb,curro,currb,mint);
           inc();
           i++;
       }
       printf("Case #%d: %d\n",t,mint-1);  
       t++;          
    }
                   
    getch();
}

void inc()
{
     if(curr=='O')
     {
          if(curro==nexto)
          {
               mint++;
               //printf("O %d %d %d %d : %d\n",nexto,nextb,curro,currb,mint);
               if(currb<nextb)
               {currb++;}
               else if(currb>nextb)
               {currb--;}
          }
          else
          {
          while(curro<nexto || curro>nexto)
          {
              (curro<nexto?curro++:curro--);
              mint++;
              if(currb<nextb)
              {currb++;}
              else if(currb>nextb)
              {currb--;}
              //printf("O %d %d %d %d : %d\n",nexto,nextb,curro,currb,mint);
          }              
          mint++;
          if(currb<nextb)
          {currb++;}
          else if(currb>nextb)
          {currb--;}
          }             
     }
     else
     {
          if(currb==nextb)
          {
              mint++;
              //printf("B %d %d %d %d : %d\n",nexto,nextb,curro,currb,mint);
              if(curro<nexto)
              {curro++;}
              else if(curro>nexto)
              {curro--;}
          }
          else
          {
          while(currb<nextb || currb>nextb)
          {
              (currb<nextb?currb++:currb--);
              mint++;
              if(curro<nexto)
              {curro++;}
              else if(curro>nexto)
              {curro--;}
              //printf("B %d %d %d %d : %d\n",nexto,nextb,curro,currb,mint);
          }         
          mint++;
          if(curro<nexto)
          {curro++;}
          else if(curro>nexto)
          {curro--;}
          }
     }
}
     
     
void next(int x)
{
     nextb=0;
     nexto=0;
     for(int y=x;y<n;y++)
     {
        if(a[y].r=='O')
        {nexto=a[y].t;break;}
     }
     for(int y=x;y<n;y++)
     {
        if(a[y].r=='B')
        {nextb=a[y].t;break;}
     }
}
