#include<stdio.h>
#include<iostream>
#include<string.h>
//#include<conio.h>
#include<map>
using namespace std;

int i,j,k,n,p,q,cas,t,co,ii,jj,r,sum;
char a[100],b[100],st[100],ch;

int main()
{
 freopen("C-small-attempt0.in","r",stdin);
 freopen("in.txt","w",stdout);

 scanf("%d",&cas);


 for(t=1;t<=cas;t++)
 {
    scanf("%d %d",&p,&q);
    sprintf(st,"%d",q);
    co=0;
    for(i=p;i<=q;i++)
    {
       sprintf(a,"%d",i);
       n=strlen(a);
       strcpy(b,a);


       for(j=0;j<n-1;j++)
       {
         //printf("*");
         ch=b[0];
         for(ii=1;ii<n;ii++)
          b[ii-1]=b[ii];
         b[n-1]=ch;

         //cout<<b<<endl; getch();
         if(strcmp(a,b)==0){
         //printf("*");
         continue; }

         r=1;
         sum=0;
         for(jj=n-1;jj>=0;jj--)
         {
           sum+=(b[jj]-48)*r;
           r=r*10;
         }
         //cout<<sum<<"$"<<endl;

         if(sum>=p&&sum<=q)
         {

           co++;
         }
       }

      // printf("&\n");


    }

    printf("Case #%d: %d\n",t,co/2);
 }

return 0;
}
