#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<math.h>
#define M 1001
using namespace std;
int gcd(int a,int b)
{
	return b?gcd(b,a%b):a;
}
int father[M];
int find(int t)
{
    if(father[t]==0)return t;
    else 
    {
         father[t]=find(father[t]);
         return father[t];
    }
}
int un(int x,int y)
{
    int x1=find(x);
    int y1=find(y);
    if(x1!=y1)
    father[x1]=y1;
}
int main()
{
    freopen("B-small-attempt0.in","r",stdin);freopen("out.txt","w",stdout);
    int N;
    scanf("%d",&N);
    int a,b,p;
    for(int i=0;i<N;i++)
    {
       scanf("%d%d%d",&a,&b,&p);
       memset(father,0,sizeof(father));
       int set=0;
       //cout<<" "<<a<<b<<endl;
       for(int j=a;j<=b;j++)
       {
           for(int k=j+1;k<=b;k++)
           {
               int s=gcd(j,k);
               if(s<p)continue;
               int flag=1;
               for(int l=2;l<=sqrt(s)&&l<=p;l++)
               {
                   if(s%l==0){flag=0;break;}
               }
               if(flag==1)un(j,k);
           }
       }
        for(int j=a;j<=b;j++)
       {
           if(father[j]==0)set++;
       }
       printf("Case #%d: %d\n",i+1,set);
    }
}
