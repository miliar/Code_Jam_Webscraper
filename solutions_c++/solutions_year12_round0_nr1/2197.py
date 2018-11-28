#include<iostream>
#include<stdio.h>
#include<stdlib.h>
int a[26]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};
int main()
{
 char str[110]="\0";
 int j,x,i=0,T;
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 gets(str);
 T=atoi(str);
 for(i=1; i<=T; i++)
 {
  gets(str);
  j=0;
  printf("\nCase #%d: ",i);
  while(str[j]!='\0')
  {
   if(str[j]!=' ')
   {
    x=str[j]-'a';
    printf("%c",'a'+a[x]);
   }
   else
    printf(" ");
   j++;
  }
 }
 return 0;
}