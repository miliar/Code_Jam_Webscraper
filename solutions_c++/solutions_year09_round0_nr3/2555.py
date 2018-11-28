#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<string.h>
using namespace std;

int main()
{
 int a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,i,n,nt,l,noc; 
 char str[501];
 
 cin>>n;
 nt=n;
 cin.get(); 
 while(n>0)
 {
     cin.getline(str,501);
      
     l=strlen(str);
     noc=0;
     for(a0=0;a0<l;a0++)
     {
      for(a1=a0+1;a1<l;a1++)
      {
       for(a2=a1+1;a2<l;a2++)
       { 
        for(a3=a2+1;a3<l;a3++)
        {
         for(a4=a3+1;a4<l;a4++)
         {
          for(a5=a4+1;a5<l;a5++)
          {
           for(a6=a5+1;a6<l;a6++)
           { 
            for(a7=a6+1;a7<l;a7++)
            {
             for(a8=a7+1;a8<l;a8++)
             {
              for(a9=a8+1;a9<l;a9++)
              {
               for(a10=a9+1;a10<l;a10++)
               { 
                for(a11=a10+1;a11<l;a11++)
                {
                 for(a12=a11+1;a12<l;a12++)
                 {
                  for(a13=a12+1;a13<l;a13++)
                  {
                   for(a14=a13+1;a14<l;a14++)
                   { 
                    for(a15=a14+1;a15<l;a15++)
                    {
                     for(a16=a15+1;a16<l;a16++)
                     {
                      for(a17=a16+1;a17<l;a17++)
                      {
                       for(a18=a17+1;a18<l;a18++)
                       { 
                        if(str[a0]=='w'&&str[a1]=='e'&&str[a2]=='l'&&str[a3]=='c'&&str[a4]=='o'&&str[a5]=='m'&&str[a6]=='e'&&str[a7]==' '&&str[a8]=='t'&&str[a9]=='o'&&str[a10]==' '&&str[a11]=='c'&&str[a12]=='o'&&str[a13]=='d'&&str[a14]=='e'&&str[a15]==' '&&str[a16]=='j'&&str[a17]=='a'&&str[a18]=='m')
                        {
                         noc++;
                         if(noc==10000)
                         noc=0;
                        }
                       }
                      }
                     }                         
                    } 
                   }
                  }
                 }                         
                } 
               }
              }
             }         
            } 
           }
          }
         }
        } 
       }
      }
     }
     if(noc<10)
     cout<<"Case #"<<nt-n+1<<": 000"<<noc<<endl;
     else if(noc<100)
     cout<<"Case #"<<nt-n+1<<": 00"<<noc<<endl;
     else if(noc<1000)
     cout<<"Case #"<<nt-n+1<<": 0"<<noc<<endl;
     else if(noc<10000)
     cout<<"Case #"<<nt-n+1<<": "<<noc<<endl;
     n--;
 }
// getch();
 return 0;
}
