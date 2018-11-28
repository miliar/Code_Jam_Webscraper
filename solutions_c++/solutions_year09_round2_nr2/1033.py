#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;

int main()
{
 int t,i,l,max,k,p,j,flag=0,nt;
 char s[25],temp,news[25];
 cin>>t;
 nt=t;
 while(t>0)
 {
  cin>>s;
  l=strlen(s);
  max=s[l-1];
  flag=0;
         for(i=l-2;i>=0;i--)
         {
                     if(s[i]>=max)
                     max=s[i];   
                     else
                     {
                         for(j=l-1;j>i;j--)
                         {
                             if(s[j]>s[i])
                             {
                                   temp=s[j];
                                   s[j]=s[i];
                                   s[i]=temp;
                                   
                                   k=0;
                                   for(p=0;p<=i;p++)
                                   news[k++]=s[p];
                                   
                                   for(p=l-1;p>i;p--)
                                   news[k++]=s[p];

                                   break;
                             }
                         }
                         news[k]='\0';
                         flag=1;
                         break;
                     }
         }
         
         if(flag==0)
         {
          /*s[l]=s[l-1];
          s[l+1]='\0';
          s[l-1]='0';
          strrev(s);
          */
          for(i=l-1;i>=0;i--)
          {
                       if(s[i]!='0')
                       break;
          }
          s[l]='0';
          s[l+1]='\0';
          l++;
          
          k=0;
          for(j=i;j<l;j++)
             news[k++]=s[j];
          for(j=i-1;j>=0;j--)
             news[k++]=s[j];
          news[k]='\0';
         }
         cout<<"Case #"<<nt-t+1<<": "<<news<<endl;
  t--;
 }
 
 getch();
 return 0;
}
