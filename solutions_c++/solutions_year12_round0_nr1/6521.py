#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;
int main()
{int a[26],n,i;
char str[120],ch;
a[0]=121;
a[1]=104;
a[2]=101;
a[3]=115;
a[4]=111;
a[5]=99;
a[6]=118;
a[7]=120;
a[8]=100;

a[9]=117;
a[10]=105;
a[11]=103;
a[12]=108;
a[13]=98;
a[14]=107;
a[15]=114;
a[16]=122;
a[17]=116;
a[18]=110;
a[19]=119;
a[20]=106;
a[21]=112;
a[22]=102;
a[23]=109;
a[24]=97;
a[25]=113;

scanf("%d",&n);
while(n-->0)
{ch=getchar();
    gets(str);
for(i=0;str[i]!='\0';i++)
if(str[i]!=' ')
str[i]=a[(int)str[i]-97];
printf("%s\n",str);
}
return (0);
}

