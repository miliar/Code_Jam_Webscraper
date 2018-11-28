#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){
    int n,size,place;
    char b[]="yhesocvxduiglbkrztnwjpfmaq";
    scanf("%d",&n);
   // n=n+1;
    int i=0,j=0;
    char a[105];
    for(i=0;i<n+1;i++){
     gets(a);
     if(i!=0)printf("Case #%d: ",i);
     for(j=0;j<strlen(a);j++){
      if(a[j]!=' ')printf("%c",b[a[j]-'a']);
      else printf(" ");
     }
     printf("\n");
    }
   // system("pause");
}
