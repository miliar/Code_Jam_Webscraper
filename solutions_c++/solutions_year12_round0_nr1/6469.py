#include<stdio.h>
int main()
{
char s[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'},str[105];
int t,k=0;
scanf("%d\n",&t);
while(t--)
{
k++;
gets(str);
printf("Case #%d: ",k);
for(int i=0;str[i]!='\0';i++)
{
if(str[i]!=' ')
printf("%c",s[int(str[i]-'a')]);
else
printf("%c",str[i]);
}
printf("\n");
}
return 0;
}
