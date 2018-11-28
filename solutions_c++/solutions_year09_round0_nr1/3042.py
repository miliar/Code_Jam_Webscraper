#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
 const int L=100,D=5000,N=500;
 int l,d,n,j=0,pos=0,k=0,m,counttoken,mainflag=1,i,p;
 char input[D][L];
 string check[N];
 char token[D][L];
 int result[N],index[D];
 cin>>l>>d>>n;
for(j=0;j<n;j++)
result[j]=0;
 cin.ignore();
 for(i=0;i<d;i++)
 {
  cin>>input[i];        
 }
 
 cin.ignore();
 for(i=0;i<n;i++)
 {
   getline(cin,check[i],'\n');           
 }
 int flag=0;
 for(i=0;i<n;i++)
 {
         
         pos=0;
         flag=0;
        
         
         j=0;
         k=0;
         m=0;
         while(check[i][j]!='\0')
         {     m=0;
              if(check[i][j]=='(')
              {
                    j++;
                    while(check[i][j]!=')')
                    {
                         token[k][m]=check[i][j];
                         m++;
                         j++;
                    }
                    token[k][m]='\0';                        
              } 
              else
              {
                  token[k][m]=check[i][j];
                  token[k][m+1]='\0';
              }
              k++;
              j++;                  
         }
         counttoken=k;
         j=0;
         k=0;
         m=0;
         
         for(p=0;p<d;p++)
         {   mainflag=1;
             for(j=0;j<l;j++)
             {m=0;
               flag=0;
               while(token[j][m]!='\0')
               {
                              if(input[p][j]==token[j][m])
                              {flag=1;
                                break;
                              }
                              m++;
               }        
               if(flag==0)
               {       mainflag=0;
                       break;       
               } 
               else
                continue;       
             }
            if( mainflag==1)
            result[i]++;                 
         }
 }
 for(i=0;i<n;i++)
 cout<<"Case #"<<i+1<<": "<<result[i]<<endl;

    return 0;
}
