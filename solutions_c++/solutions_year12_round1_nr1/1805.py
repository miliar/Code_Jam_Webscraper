#include<iostream>
//#include<conio.h>
#include<math.h>
#include<stdio.h>
using namespace std;
int main()
{
    int qq,tt=0;
    cin>>qq;
    while(tt<qq)
    {
                tt++;
    int a,b;
    cin>>a>>b;
    float f[a],d[a],e;
   int u=0,l;
    u=pow(2,a);
    int q[a+2][u],count=0;
   float t[u];
    for(int i=a-1;i>=0;i--)
    {
            cin>>e;
            f[i]=e;
            d[i]=1-e;
            }
  
    l=a;
   while(l>0)
    {
              l/=2;
              count++;
              }
    int k[count],temp=0,len=0,mem=0;
    float res;
    len=count;
    for(int i=0;i<count;i++)
    {
            k[i]=0;
            }
    for(int i=0;i<u;i++)
    {
   for(int i=0;i<a;i++)
    {
            k[i]=0;
            }
            l=i;
    count=0;
    while(l>0)
    {
              temp=l%2;
              k[count]=temp;
              l/=2;
              count++;
              }
    res=1.0f;     
     for(int j=a-1;j>=0;j--)
     {
             if(k[j]==1)
            {
                        res=res*d[j];
                        }
            else
            {
             res*=f[j];
                }
             }
     t[i]=res;
            }
     //cout<<"t[i]"<<endl;
     int p;
     for(int i=0;i<a+2;i++)
     {
             for(int j=0;j<u;j++)
             {
                     if(i!=(a+1))
                     {
                       p=j;
                     for(int h=0;h<i;h++)
                     {
                             p=p>>1;
                             }
            //         cout<<"p "<<i<<" "<<j<<" "<<p<<endl;
                     if(p!=0)
                     {
                          //   cout<<"i "<<i<<" "<<j<<" "<<p<<endl;
                             q[i][j]=0;
                             q[i][j]=i+b+b-(a-i)+2;
                             }
                     else
                     {
                         q[i][j]=0;
                         q[i][j]=i+b-(a-i)+1;
                         }        
                               }
                         else
                         {
                             q[i][j]=b+2;
                             }
                     }
             }
    float sum[u],max=700000.0;
     for(int i=0;i<a+2;i++)
     {
             sum[i]=0.0;
             for(int j=0;j<u;j++)
             {
             sum[i]+=t[j]*q[i][j];
             }
             if(sum[i]<max)
             {
                           max=sum[i];
                           }
             
             }
     printf("Case #%d: %f\n",tt,max);
     }
     //cout<<max<<endl;
  //  getch();
    return(0);
    }
