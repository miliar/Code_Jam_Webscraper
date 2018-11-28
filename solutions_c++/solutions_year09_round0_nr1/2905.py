#include<iostream>
#include<string.h>
using namespace std;
int main()
{
char s[6000][50];
int l,d,n,count,test;
cin>>l>>d>>n;
count=0;
while(count<d)
 {cin>>s[count];
 count++;}
test=0;
char g;
g=getchar();
while(test<n)
{  
   int  pos[26][16]={0};
   for(int i=0;i<26;i++)
    for(int j=0;j<16;j++)      
         pos[i][j]=0;
   
   char c;
   
   int counter=0,f=0,posi=0;
   while((c=getchar())!='\n'&&c!=EOF)
   {
      if(c=='(')
      {
         while((c=getchar())!=')')
            pos[c-97][posi]=1;
         posi+=1;
      }
      else pos[c-97][posi++]=1;
    }
    for(int i=0;i<d;i++)
      {  f=0;
         for(int j=0;j<strlen(s[i]);j++)
         {    c=s[i][j]; 
              if(pos[(c-97)][j]==1)f++;
              else break;
          }
      if(f==strlen(s[i]))counter++;
     }
    test++;
    cout<<"Case #"<<test<<": "<<counter<<endl;
}
return 0;
}
      
          
