#include <math.h>
#include <conio.h>
#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>


using namespace std;
FILE *fin,*fout;
int N;
string n_2_s(long long n);
int main()
{
   fin=fopen("C:/Documents and Settings/Abhijit/Desktop/codejam/round1b/B-large.in","r"); 
   fout=fopen("C:/Documents and Settings/Abhijit/Desktop/codejam/round1b/B-large.out","w");
   fscanf(fin,"%d\n",&N); 
   //cout<<N;   
   for(int i=1;i<=N;i++)
   {char *c;string s;
    char a;
    int swap=0,j;
    
    c=(char*) malloc (sizeof(char)*20);
      fscanf(fin,"%s\n",c); 
      s=c;
      //fgets(s,fin);
      cout<<s<<"::"; 
     for(j=s.size();j>0;j--)
     {
         if(s[j]>s[j-1]) {swap=1;break;}
             
     } 
     
     
     if(swap == 0) 
      {sort(s.begin(),s.end());s.insert(1,1,'0');
       if(s[0]=='0') 
        {for(int k=1;k<s.size();k++)
          if(s[k] != '0') {a=s[k];s[k]=s[0];s[0]=a;break;}
                     
                     }            
      }
     else 
     {sort(s.begin()+j,s.end()) ; 
      for(int k=j;k<s.size();k++)
       if(s[j-1]<s[k]){a=s[k];s[k]=s[j-1];s[j-1]=a;break;}  
       
     } 
     
     fprintf(fout,"Case #%d: ",i);
     for(int k=0;k<s.size();k++)
      fprintf(fout,"%c",s[k]);  
     fprintf(fout,"\n"); 
     cout<<s<<endl;    
   }
   
   cout<<"***end***"; 
   fclose(fin);
   fclose(fout);
   getch(); 
 return 0;   
}

string n_2_s(long long n)
{string s;char c;
do
{c=48+n%10;s.insert(0,1,c);n=n/10;
        
}while(n !=0);
       
 return s;      
       
}       
