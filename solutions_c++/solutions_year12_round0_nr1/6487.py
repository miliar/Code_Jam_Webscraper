#include<stdio.h>
#include<string.h>
char str[101];
int main()
{
freopen("A-small-attempt1.in", "r", stdin);
freopen("OUTPUT1.txt", "w", stdout);
char dict[27]=
{' ',
'y',
'h',
'e',
's',
'o',
'c',
'v',
'x',
'd',
'u',
'i',
'g',
'l',
'b',
'k',
'r',
'z',
't',
'n',
'w',
'j',
'p',
'f',
'm',
'a',
'q'
};
int i,j,k;
gets(str);
i=str[0]-'0';
if(str[1]!='\0')
{j=str[1]-'0';
i=i*10+j;
}
for( j=1;j<=i;j++)
{
   gets(str);
     for(k=0;str[k]!='\0';k++){
     if(str[k]==' ')str[k]==' ';
     else str[k]=dict[str[k]-'a'+1];
     }
     printf("Case #%d: %s\n",j,str);
     
}
fclose(stdin);
fclose(stdout);
}
