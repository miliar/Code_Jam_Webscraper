#include<stdio.h>
#include<string>
#include<string.h>
#include<iostream>

using namespace std;

int main()
{
    int T,j=0,i;
    char s[100];
    string dic("yhesocvxduiglbkrztnwjpfmaq");
    
    scanf("%d",&T);//fflush(stdin);
    gets(s);
    while(T!=0)
    {
       gets(s);
       //cout<<s<<endl;
       printf("Case #%d: ",j+1);
       //printf("\taaa\n");
       for(i=0;i<strlen(s);i++)
       {
               if(s[i]==32)
               printf(" ");
               else
               printf("%c",dic[((int)s[i])-97] );
               
//               printf("%c",dic[((int)s[i])-97] );
       }
       printf("\n");
       T--;
       j++;
    }
    return 0;
}
