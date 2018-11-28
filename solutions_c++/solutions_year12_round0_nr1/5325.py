#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
int main()
{
    int t,n,m,i,j,k;
    cin>>t;
    char my[100];
    my[0]='y';my[1]='h';my[2]='e';my[3]='s';my[4]='o';my[5]='c';my[6]='v';my[7]='x';my[8]='d';my[9]='u';my[10]='i';my[11]='g';my[12]='l';
    my[13]='b';my[14]='k';my[15]='r';my[16]='z';my[17]='t';my[18]='n';my[19]='w';my[20]='j';my[21]='p';my[22]='f';my[23]='m';my[24]='a';my[25]='q';
    char a[1000],b[1000];
    for(k=1;k<=(t+1);k++)
    {
                   
                   
        gets(a);
       for(i=0;i<strlen(a);i++)
       {
          if(a[i]!=' ')
          {   
              //cout<<a[i]-97;                  
         b[i]=my[(int)a[i]-97];
         }
         else
         {
             b[i]=a[i];
             }
         }
         b[i]='\0';
         if(k>1)
         {
        printf("Case #");
        cout<<k-1;
        printf(": ");
        puts(b);
        
        } 
        }                     
                   return 0;
                   }                                             
                        
                                                  
              
