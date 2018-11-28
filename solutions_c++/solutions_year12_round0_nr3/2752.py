#include <stdio.h>
#include <iostream>
#include <fstream>

using namespace std;
int main()
{
int t;
fstream ip ("C-large.in");
fstream op ("output1.txt");
ip>>t;
int size=t;
while(t--)
{
 int count=0;
 int min;
 int max;
 ip>>min;
 ip>>max;
 string smin="";
 string smax="";
 int rmax=max;
 while(max>0)
 {
   int i=(max%10);
   max=max/10;
   char c=i+48;
   smax=c+smax;
 }

 int rmin=min;
 while(smin.length()!=smax.length())
 {
   int i=(min%10);
   min=(min-min%10)/10;
   char c=i+48;
   smin=c+smin;
  
 }


 for(int i=rmin;i<=rmax;i++)
 {
   string n="";
   int x=i;
   
   while(n.length()!=smax.length())
   {
     int a=(x%10);
      x=(x-x%10)/10;
     char c=a+48;
     n=c+n;
   }
  
 
   int size=n.length();
   string* check=new string[size];
   
   int j=1;
   while(j<size)
   { 
      check[j]="";
      int k=0;
     int flag1=0;
     int flag2=0;
     int flag3=0;
      int  flag4=0;
     
     while(k<size)           
     {
       if(n[k]==n[(k+j)%size]){k++;continue;}
       if((n[k]<n[(k+j)%size]))
       {
         flag1=1;break;
       }
       else
       {
        break;
       }
       k++;
     } 
     k=0;
     
     while(k<size)           
     {
       if(smax[k]==n[(k+j)%size]){k++;if(k==size)flag2=1;continue;}
       if((smax[k]>n[(k+j)%size]))
       {
         flag2=1;break;
       }
       else
       {
        break;
       }
       k++;
     } 
     k=0;
     
     while(k<size)           
     {
       if(smin[k]==n[(k+j)%size])
       {
          k++;
          if(k==size){flag3=1;break;}
          continue;
       }
       if((smin[k]<n[(k+j)%size]))
       {
         flag3=1;break;
       }
       else
       {
        break;
       }
       k++;
     } 
     if(flag1&&flag2&&flag3)
     {
      
      k=0;
      while(k<size)
      {
       check[j]=check[j]+n[(k+j)%size];
       k++;
      }
      
      
      if((size&1)==0)
     {
         
         k=0;
         while(k<j)
        {
         if(check[k]==check[j]){flag4=1;break;}
         k++;
        }
         if(flag4!=1){count++;}
         
      }
      else
      {
        
        count++;
      } 
   }
     
     j++;
   }
     delete[] check;
  }
  op<<"Case #"<<size-t<<": "<<count<<"\n";
  cout<<size-t<<endl;
  
  

}



}
