#include<iostream>
#include<fstream>
using namespace std;
char engine[103][257];
char query[1002][257];
int flag[102];
int now,ans,temp;
int n,size,i,qsize,j,k,t;
   ifstream fin;
ofstream fout;   
void ini()
 {
       fin>>size;
       fin.getline(engine[102],257);
        for (i=1;i<=size;i++)   
       {
         fin.getline(engine[i],257);
       
         }
         fin>>qsize;
          fin.getline(engine[102],257);
         for(j=1;j<=qsize;j++)
           fin.getline(query[j],257);
           temp=0;
           ans=0;
           now=0;
           for (i=1;i<=size;i++)
           flag[i]=0;
 return;
 }
int find(char s[257])
 {
   int temp,i;
    temp=0;
    for (i=1;i<=size;i++)
     {
      if (strcmp(engine[i],s)==0)
       {
         temp=i;
         break;
       }  
     };
      return temp;
 } 
int main() 
   {
fin.open("A.in");
fout.open("A.out");
   fin>>n;
   temp=0;
   for (t=1;t<=n;t++)
    {
      ini();
     for (i=1; i<=qsize; i++)
       {  
          
          k=find(query[i]);
          if (k==0) continue;
          if (flag[k]==0)
           {
            temp++;
                     flag[k]=1;
           };
          if (temp==size)
          { 
                 ans++;
                 temp=1;
                for (j=1;j<=size;j++)
                 flag[j]=0;
                  flag[k]=1;          
                  } 
       }         
      fout<<"Case #"<<t<<": "<<ans<<endl;       
    };
    fin.close();
    fout.close();
     return 0;       
    }
