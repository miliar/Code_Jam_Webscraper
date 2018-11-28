//
#include<stdio.h>
#include<fstream.h>
#include<conio.h>
int main()
{
     int i,j,T,N,S,p,a,cnt,sur,arr[100],s[100],ns[100];
     freopen("B-large.in","r",stdin);
     freopen("Output.out","w",stdout);
     scanf("%d",&T);
     for(i=0;i<T;i++)
     {
                     scanf("%d%d%d",&N,&S,&p);
                     cnt=sur=0;
                     for(j=0;j<N;j++)
                     {
                                     scanf("%d",&arr[j]);
                                     a=arr[j]/3;
                                     switch(arr[j]%3)
                                     {
                                                     case 1:
                                                          s[j]=a+1;
                                                          ns[j]=a+1;
                                                          if(a==0)
                                                          {
                                                                  s[j]=-1;
                                                          }
                                                          break;
                                                     case 2:
                                                          s[j]=a+2;
                                                          ns[j]=a+1;
                                                          if(a==9)
                                                          {
                                                                  s[j]=-1;
                                                          }
                                                          break;
                                                     case 0:
                                                          s[j]=a+1;
                                                          ns[j]=a;
                                                          if(a==0)
                                                          {
                                                                  s[j]=-1;
                                                          }
                                                          if(a==10)
                                                          {
                                                                   s[j]=-1;
                                                          }
                                     }
                                     if(ns[j]>=p)
                                     {
                                               cnt++;
                                               //printf("cnt incremented");
                                     }
                                     else if(s[j]>=p)
                                     {
                                          if(sur<S)
                                          {
                                                   sur++;
                                                   //printf("sur = %d\n",sur);
                                                   cnt++;
                                                   //printf("cnt incremented\n");
                                          }
                                     }
                     }
                     printf("Case #%d: %d\n",i+1,cnt);
     }
     getch();
}
