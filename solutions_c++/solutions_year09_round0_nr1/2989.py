// cpp.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
/*
ID: reza_711
PROG: test
LANG: C++
*/
#include<iostream>
#include<fstream>
using namespace std; 
 int main()
{
     ofstream fout("A-small.txt");
     ifstream fin("Asmall.out");
     char str[5050][100],str1[10000],str2[1000][1000];
     int L,D,R,i,j,k,l,m,o,c,d;
	 
	 fin>>L>>D>>R;
	 
     for(i=0;i<D;i++)
     {
       fin>>str[i];
     } 
     for(i=1;i<=R;i++)
     {
       fin>>str1;
       k=0;
       for(j=0;j<strlen(str1);j++)
       { 
         l=0;
         if(str1[j]=='(')
         {
            
			j++;
            while(str1[j]!=')')
            {
               str2[k][l++]=str1[j++];                  
            }
         
         }
         else if(str1[j]==' ');
         else
		 {
			 str2[k][l]=str1[j];
	
			// j++;
		

			 l++;
		 }
         str2[k][l++]='\0';
		 k++;
       }
       c=0;
       for(o=0;o<D;o++)
       {
           d=0;
           for(j=0;j<L;j++)
           {
       
               for(m=0;m<strlen(str2[j]);m++)
               {
            
                   if(str[o][j]==str2[j][m])
                   {break;}
         
                       
               }
               if(m!=strlen(str2[j]))d++;
                       
           }
           if(d==L)c++;
       }
       
     fout<<"Case #"<< i<<": "<<c<<endl;
     } 
//	 fout<<a+b<<endl;}     
     return 0;
}
