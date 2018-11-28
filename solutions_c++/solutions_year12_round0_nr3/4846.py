#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
int main()
{
    int i,t,n,m,j,x=0,cnt=0,m2,a,b,k,lam,s1=0,s2=1;
    int udig,hdig,tdig;
    scanf("%d",&t);
    int* z=NULL;
    z=(int*) malloc((2*t)*sizeof(int));
    lam=t;
    while(t--)
    {
              scanf("%d%d",&z[s1],&z[s2]);
              s1+=2;
              s2+=2;              
              }
              s1=0;
              s2=1;
              while(lam--)
              {
                        x++;
              if(z[s1]>=1 && z[s2]<=9)
              {
              printf("Case #%d: 0\n",x);
              }
              if(z[s1]>=10 && z[s2]<=99)
              {
                           for(n=z[s1];n<=z[s2];n++)
                           {
                           k=n;
                           udig=k%10;
                           k=k/10;
                           tdig=k%10;
                           m=(udig*10 + tdig);
                           if(m<=z[s2] && m>n)
                           cnt++;
                           }
                           printf("Case #%d: %d\n",x,cnt);
                           } 
                               
                           if(z[s1]>=100 && z[s2]<=999)
                           {
                           for(n=z[s1];n<=z[s2];n++)
                           {
                           k=n;
                           udig=k%10;
                           k=k/10;
                           tdig=k%10;
                           k=k/10;
                           hdig=k;
                           m=(tdig*100 + udig*10 + hdig);
                           if( m>n && m<=z[s2])
                           cnt++;
                           m2=(udig*100 + hdig*10 + tdig);
                           if(m2>n && m2<=z[s2])
                           cnt++;
                           }
                           printf("Case #%d: %d\n",x,cnt);
                           
                           }
                           cnt=0;
                           s1+=2;
                           s2+=2;
                           }
                           getch();
                           return 0;
                           }
                                             
    

