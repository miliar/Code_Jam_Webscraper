#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int a,b;
int nod(int n)
{
    int i=0;
    while(n)
    {n/=10;i++;}
    return i;
}
int recycle(int n)
{
    int p,i,l,j,res=0,m=n,nd,a[10],size=0,fl;
    nd=nod(n);
    for(i=1,p=1;i<nd;i++)
    p*=10;    
    for(i=1;i<nd;i++)
    {
              l=m%10;
              m/=10;
              //printf("nd:%d n:%d m:%d l:%d pow:%d\n",nd,n,m,l,pow(10,nd-1));
              m+=(l*p);
              //m+=(l*((int)pow(10,nd-1)));   
              //printf("nd:%d n:%d m:%d l:%d\n",nd,n,m,l);
              //system("pause");
                if((m>n)&&(m<=b))            
                {
                                             for(fl=j=0;j<size;j++)
                                             if(m==a[i]){fl=1;break;}
                                             if(!fl)
                                             {
                                             a[size++]=m;
                                              //printf("n:%d m:%d l:%d\n",n,m,l);
                                              res++;
                                             }
                }
    }
    return res;       
}
int main()
{
 int test,ctr=1,i,ans;
 freopen("C-small-attempt0.in","r",stdin);
 freopen("output.txt","w",stdout); 
 scanf("%d",&test);
 for(;ctr<=test;ctr++)
 {
                      scanf("%d%d",&a,&b);
                      for(ans=0,i=a;i<=b;i++)
                                       ans+=recycle(i);     
                      printf("Case #%d: %d\n",ctr,ans);
 }
 return 0;
}
