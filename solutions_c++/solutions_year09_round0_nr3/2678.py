#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;


int fun(char *str,int i,int pos);
char welcome[100] = "welcome to code jam";
int maxstr,maxwel;
int main(int argc,char * argv[])
{
 char str[600];
 strcpy(welcome,"welcome to code jam");
 maxwel= strlen(welcome);
 int val=0,N;
 cin>>N;
 //gets(str);

 for(int i=0;i<N;i++)
 {
  getchar();
  scanf("%[^\n]",str);
  //gets(str);
  //cout<<str<<endl;
  maxstr= strlen(str);
  val = fun(str,0,0);
  val=val%1000;
  printf("Case #%d: %04d\n",i+1,val);
  
 }
 
 //for(i=0;i<max;i++)
 //{
   
 //}
 
}
int fun(char *str,int strpos,int welpos)
{
 int ret=0,k;
 if(strpos > maxstr-1)
   return 0;
 for(k=strpos;k<maxstr;k++)
 {
   if(str[k]==welcome[welpos])
   {
      if(welpos==maxwel-1)
        ret+=1;      
      else
      {
        ret += fun(str,k+1,welpos+1);
        ret = ret%1000;
      }
   }
 }
 return ret;
}
