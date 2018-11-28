#include<stdio.h>
#include<string>
#include<iostream>
using namespace std;


char s[28]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '};
char p[28]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q',' '};


char a[200];


int main()
{
  int t;
  scanf("%d",&t);
  for(int i=0;i<t;i++){
   getchar();
   scanf("%[^\n]", a );

   int len=strlen(a);
   
   printf("Case #%d: ",i+1);
	for(int j=0;j<len;j++){
	  for(int k=0;k<=27;k++){   
	    if(a[j]==s[k]){
         printf("%c",p[k]);                                   
       }
	  } 
  
}
    printf("\n");
  }
}
