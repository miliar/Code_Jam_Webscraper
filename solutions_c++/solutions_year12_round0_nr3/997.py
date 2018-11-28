#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int main()
{
    freopen("C-large.in.","r",stdin);
    freopen("out.txt","w",stdout);
    
    int amm;
    scanf("%d",&amm);
    for (int i=1;i<=amm;i++)
    {
        int low,high;
        scanf("%d%d",&low,&high);
        printf("Case #%d: ",i);
        if (high/10==0){printf("0\n");continue;}
        if (high/100==0)
        {
           int ans=0;
           for (int j=low;j<=high;j++)
           {
               int p=j/10+(j%10)*10;
               if (p!=j&&p>=low&&p<=high)ans++;              
           }               
           printf("%d\n",ans/2);                       
           continue;
        }
        if (high/1000==0)
        {
           int ans=0;
           for (int j=low;j<=high;j++)
           {
               int a=j/100;
               int b=(j%100)/10;
               int c=j%10;
               if (a==b&&a==c)continue;
               int p1=b*100+c*10+a;
               if (p1!=j&&p1>=low&&p1<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p1);
               }
               int p2=c*100+a*10+b;
               if (p2!=p1&&p2!=j&&p2>=low&&p2<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p2);
               }
           }               
           printf("%d\n",ans/2);                       
           continue;                
        }
        
        if (high/10000==0)
        {
           int ans=0;
           for (int j=low;j<=high;j++)
           {
               int a=j/1000;
               int b=(j%1000)/100;
               int c=(j%100)/10;
               int d=j%10;
               if (a==b&&a==c&&a==d)continue;
               int p1=b*1000+c*100+d*10+a;
               if (p1!=j&&p1>=low&&p1<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p1);
               }
               int p2=c*1000+d*100+a*10+b;
               if (p2!=p1&&p2!=j&&p2>=low&&p2<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p2);
               }
               int p3=d*1000+a*100+b*10+c;
               if (p3!=p2&&p3!=p1&&p3!=j&&p3>=low&&p3<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p2);
               }
           }               
           printf("%d\n",ans/2);                       
           continue;                
        }
        
        if (high/100000==0)
        {
           int ans=0;
           for (int j=low;j<=high;j++)
           {
               int a=j/10000;
               int b=(j%10000)/1000;
               int c=(j%1000)/100;
               int d=(j%100)/10;
               int e=j%10;
               if (a==b&&a==c&&a==d&&a==e)continue;
               int p1=b*10000+c*1000+d*100+e*10+a;
               if (p1!=j&&p1>=low&&p1<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p1);
               }
               int p2=c*10000+d*1000+e*100+a*10+b;
               if (p2!=p1&&p2!=j&&p2>=low&&p2<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p2);
               }
               int p3=d*10000+e*1000+a*100+b*10+c;
               if (p3!=p2&&p3!=p1&&p3!=j&&p3>=low&&p3<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p2);
               }
               int p4=e*10000+a*1000+b*100+c*10+d;
               if (p4!=p3&&p4!=p2&&p4!=p1&&p4!=j&&p4>=low&&p4<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p2);
               }
           }               
           printf("%d\n",ans/2);                       
           continue;                
        }
        
        if (high/1000000==0)
        {
           int ans=0;
           for (int j=low;j<=high;j++)
           {
               int a=j/100000;
               int b=(j%100000)/10000;
               int c=(j%10000)/1000;
               int d=(j%1000)/100;
               int e=(j%100)/10;
               int f=j%10;
               if (a==b&&a==c&&a==d&&a==e&&a==f)continue;
               int p1=b*100000+c*10000+d*1000+e*100+f*10+a;
               if (p1!=j&&p1>=low&&p1<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p1);
               }
               int p2=c*100000+d*10000+e*1000+f*100+a*10+b;
               if (p2!=p1&&p2!=j&&p2>=low&&p2<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p2);
               }
               int p3=d*100000+e*10000+f*1000+a*100+b*10+c;
               if (p3!=p2&&p3!=p1&&p3!=j&&p3>=low&&p3<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p2);
               }
               int p4=e*100000+f*10000+a*1000+b*100+c*10+d;
               if (p4!=p3&&p4!=p2&&p4!=p1&&p4!=j&&p4>=low&&p4<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p2);
               }
               int p5=f*100000+a*10000+b*1000+c*100+d*10+e;
               if (p5!=p4&&p5!=p3&&p5!=p2&&p5!=p1&&p5!=j&&p5>=low&&p5<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p2);
               }
           }               
           printf("%d\n",ans/2);                       
           continue;                
        }
        
        if (high/10000000==0)
        {
           int ans=0;
           for (int j=low;j<=high;j++)
           {
               int a=j/1000000;
               int b=(j%1000000)/100000;
               int c=(j%100000)/10000;
               int d=(j%10000)/1000;
               int e=(j%1000)/100;
               int f=(j%100)/10;
               int g=j%10;
               if (a==b&&a==c&&a==d&&a==e&&a==f&&a==g)continue;
               int p1=b*1000000+c*100000+d*10000+e*1000+f*100+g*10+a;
               if (p1!=j&&p1>=low&&p1<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p1);
               }
               int p2=c*1000000+d*100000+e*10000+f*1000+g*100+a*10+b;
               if (p2!=p1&&p2!=j&&p2>=low&&p2<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p2);
               }
               int p3=d*1000000+e*100000+f*10000+g*1000+a*100+b*10+c;
               if (p3!=p2&&p3!=p1&&p3!=j&&p3>=low&&p3<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p2);
               }
               int p4=e*1000000+f*100000+g*10000+a*1000+b*100+c*10+d;
               if (p4!=p3&&p4!=p2&&p4!=p1&&p4!=j&&p4>=low&&p4<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p2);
               }
               int p5=f*1000000+g*100000+a*10000+b*1000+c*100+d*10+e;
               if (p5!=p4&&p5!=p3&&p5!=p2&&p5!=p1&&p5!=j&&p5>=low&&p5<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p2);
               }
               int p6=g*1000000+a*100000+b*10000+c*1000+d*100+e*10+f;
               if (p6!=p5&&p6!=p4&&p6!=p3&&p6!=p2&&p6!=p1&&p6!=j&&p6>=low&&p6<=high)
               {
                  ans++;
                  //printf("%d %d\n",j,p2);
               }
           }               
           printf("%d\n",ans/2);                       
           continue;                
        }
    }
    return 0;   
}
