#include<stdio.h>

int main()
{
    int n,n1,i;
    char c;
    char key[]="yhesocvxduiglbkrztnwjpfmaq";
    char str[100];
    scanf("%d",&n);
    n1=n;
getchar();
//getchar();
      while(n--)
        {
	printf("Case #%d: ",n1-n);
	while((c=getchar())!='\n')
{if(c!=' ')
printf("%c",key[c-97]);
else 
printf(" ");}
printf("\n");
                  }
    return 0;
    
    }
    
    
    
