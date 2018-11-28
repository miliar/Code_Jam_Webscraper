#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<string.h>

using namespace std;

int main()
{
char m[]="yhesocvxduiglbkrztnwjpfmaq";
int t;
scanf("%d",&t);
for(int i=0;i<=t;i++)
{
char s[101];
cin.getline(s,101);
if(i==0) continue;
else
{
cout<<"Case #"<<i<<": ";
for(int i=0;i<strlen(s);i++)
{

if(s[i]!=' ')
printf("%c",m[s[i]-97]);
else 
printf(" ");
}
printf("\n");
}
}
fflush(stdin);


}
