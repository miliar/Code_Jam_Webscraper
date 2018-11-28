#include<stdio.h>
#include<string.h>
#include<iostream>

using namespace std;

int check(char *str,int n);
void fun(char *str, char poss[][30],int pos);
int L,D,N;
char word[5005][30];
int valid;

int main(int argc,char *argv[])
{
 char poss[30][30];
 char str[30];
 char dum;
 int i,j;
 
 
 cin >> L ;
 cin >> D >> N;
 for(i=0;i<D;i++)
 {
  cin >> word[i];
 }
 int casen=0;
 
 for(casen=0;casen < N;casen++)
 {
   for(i=0;i<L;i++)
   {
    cin>>dum;
    j=0;
    poss[i][j]='\0';
    if(dum=='(')
    {
       cin>>dum;
       while(dum!=')')
       {
          poss[i][j]=dum;
          j++;
          cin>>dum;
       }
   
    }
    else
    {
       poss[i][j]=dum;
       j++;
    }
    poss[i][j]='\0';
   }

   //for(i=0;i<L;i++)
     //cout<<poss[i]<<endl;
   valid=0;
   str[L]='\0';
   fun(str,poss,0);
   cout<<"Case #"<<casen+1<<": "<<valid<<endl;
 }
 
}

void fun(char *str, char poss[][30],int pos)
{
 int j;
 if(pos > L-1)
 {
   //cout<<str<<endl;
    if(check(str,L))
      valid++;
    return;
 }
 j=0;
 //for(i=pos;i<L;i++)
 {
    while(poss[pos][j]!='\0')
    {
       str[pos]=poss[pos][j];
       j++;
       if( check(str,pos+1) )
        fun(str,poss,pos+1);
    }
 }
 
}
int check(char *str,int n)
{
 for(int i=0;i<D;i++)
  if( strncmp(str,word[i],n) == 0)
   return 1;
 return 0;
}
