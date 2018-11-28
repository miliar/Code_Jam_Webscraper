#include <iostream>
#include <stdio.h>
#include<string.h>
//#include<conio.h>
#include<map>
using namespace std;

int fincount=0;


void right(char a[])
{
    int l=strlen(a);
    int temp=a[0];
    int temp1;
    for(int i=1;i<l;i++)
    {
            temp1=a[i];
            a[i]=temp;
            temp=temp1;
    }
    a[0]=temp;
}

int count(int a,int b)
{
         char a1[8];
         char b1[8];
         //itoa(a,a1,10);
         //itoa(b,b1,10);
         int len;
         for(int i=a;i<=b;i++)
         {
                 map <int,int> big;
                 itoa(i,a1,10);
                 len=strlen(a1);
                 int temp1=atoi(a1);
                 for(int j=0;j<len;j++)
                 {
                         right(a1);
                         int temp=atoi(a1);
                         
                         if(big[temp]==0)
                         {
                         if(a<=temp && temp<=b && temp!=temp1)
                         {
                                       //cout<<temp1<<"."<<temp<<" ";
                                       fincount++;
                                       big[temp]=1;                                       
                         }
  
                         
  }
                         //else
                           //fincount++;
                 }            
         }
         
}
                 
int main()
{
    int a,b,t;
    char c[8];
    cin>>t;

    int len;
    for(int k=1;k<=t;k++)
    {
              fincount=0;
              cin>>a>>b;
              count(a,b);
              cout<<"Case #"<<k<<": "<<fincount/2<<endl;
    }
              //right(c);
    //for(int i=0;i<4;i++)

    //getch();
    
    return 0;
}
