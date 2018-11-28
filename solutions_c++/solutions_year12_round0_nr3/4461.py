#include <cstdlib>
#include<fstream>
#include<iostream>
#include<cmath>
#include<cstdlib>
#include<sstream>
using namespace std;
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<string.h>

int func1(int,double);
int main()
{
   ofstream out;
   out.open("Bsmallout.txt");
   
   ifstream in;
   in.open("Bsmall.txt");
   
   int cnum=1000,i,j=0,A,B,pos,counter=0,r,d,k=0;
   double n,len;
   string s[cnum],str;
   
   out.clear();
   in.seekg(0);
   
   if(out) cout<<"ha ha ha";
   getch();
   out.clear();
   in.clear();
 
   i=0;
   while(in)
   {  
      getline(in,s[i]);      
         
         pos=s[i].find(" ");
         str=s[i].substr(0,pos);
         
         stringstream convert(str); // stringstream used for the conversion initialized with the contents of Text
         if ( !(convert >> A) )//give the value to Result using the characters in the string
         A = 0;//if that fails set Result to 0
         
         str=s[i].substr(pos+1);
         
         stringstream convert2(str); // stringstream used for the conversion initialized with the contents of Text
         if ( !(convert2 >> B) )//give the value to Result using the characters in the string
         B = 0;//if that fails set Result to
                 
         counter=0;
         if(A!=0&&B!=0&&i!=0)
         {for(j=A;j<=B;j++)
          {
               len=ceil(log10(j));
               n=j;
               for(k=len-1;k>=0;k--)
               {n=func1(n,len);
                if(n<=B&&n>j)
                {counter++;} 
               }
               out<<endl;
          }
         out<<"Case #"<<i<<": "<<counter<<endl;}
         i++;
      }
           
   
   
in.close();
out.close();
getch();
return 0;
}

int func1(int j, double len)
{             
              int r,d;
              double n;
               r=j%10; //cout<<r<<" ";
               d=j/10; //cout<<d<<" ";
               n=r*pow(10,len-1)+d; //out<<n<<" ";
               return n;
}
