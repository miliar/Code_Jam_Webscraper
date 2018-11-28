#include <iostream>
#include <cstdio>
#include <string>

using std::cout ;

int times ;
char str[50];

int cases=0;
int input (){
 scanf("%s",str);
 cases++;
 printf("Case #%d: ",cases);
 int i,j,len = strlen(str);
 for(i=len-1;i>=0;i--){
     int pos = -1;
     for(j=i+1;j<len;j++)
       if(str[j]>str[i]&&(pos==-1||(str[j]<str[pos])))
       pos=j;
   if(pos!=-1){
   char t = str[i];
   str[i]=str[pos];
   str[pos]=t;
   std::sort(str+i+1,str+len);
   printf("%s\n",str);
   return 0;    
   }             
 }   
 if(i==-1){
   std::sort(str,str+len);
   for(i=0;str[i]=='0';i++);
   printf("%c",str[i]);
   for(j=0;j<i+1;j++)
   printf("0");
   for(i++;str[i];i++)
   printf("%c",str[i]);
   printf("\n");         
 }
}
int main (){
  scanf("%d",&times);
  while(times--){
    input ();               
  }  
}
