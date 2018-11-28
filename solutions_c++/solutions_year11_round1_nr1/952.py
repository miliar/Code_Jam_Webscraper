#include<stdio.h>
#include<vector>
#include<bitset>
#include<iostream>
#include<conio.h>
using namespace std;

#define max(a,b) (a>=b?a:b)
int t=1,tests,D,G,Pd,Pg,i,flag=0,j,num;
long long N;
char pos[]="Possible",br[]="Broken";
vector<int> factors;
int check(int x);

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&tests);
    while(t<=tests)
    {
         scanf("%I64d %d %d",&N,&Pd,&Pg);
         flag=0;
         if(Pd==0 && Pg==0)
         {
              flag=1;
         }
         else if(Pd>0 && Pg==0)
         {
              flag=0;
         }
         else if(Pd==0 && Pg>0 && Pg!=100)
         {
              flag=1;
         }
         else if(Pd==100 && Pg==100)
         {
              flag=1;
         }
         else if(Pd<100 && Pg==100)
         {
              flag=0;
         }
         else if(Pd==100 && Pg<100)
         {
              flag=1;
         }
         else
         {
              factors.clear();
              num=0;
              for(i=1;i<=Pd;i++)
              {
                  if(Pd%i==0)
                  {factors.push_back(i);num++;}
              }
              for(i=0;i<num && flag==0;i++)
              {
                  if(factors[i]<N &&  check(factors[i])==1)
                  {flag=1;}
              }
         }
         if(flag==1)
         {
              j--;i--;
              //printf("Case #%d: %s %d %d %d %d %d\n",t,pos,(j*100)/i,Pd,Pg,j,i);
              printf("Case #%d: %s\n",t,pos);
         }
         else
         {
              printf("Case #%d: %s\n",t,br);
         }
         t++;
    }
    getch();
}
         
int check(int x)
{
     float other=(float)(x*100)/Pd;
     if(other<=N && other-(int)other==0)
     {return 1;}
     else
     {return 0;}
}        
         
         
         
         
         
         
         
         
         
          
                     
