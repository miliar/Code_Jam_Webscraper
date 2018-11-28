#include<stdio.h>
#include<string.h>
int main()

{
int k,t,i,len,count=1;
char ch,str[200];

scanf("%d",&t);
t=t+1;

for(k=0;k<t;k++)
{
gets(str);
len=strlen(str);

for(i=0;i<len;i++)
{

ch=str[i];

switch (ch)
{

case 'a' : str[i]='y';
			  break;

case 'b' : str[i]='h';
			  break;

case 'c' : str[i]='e';
			  break;

case 'd' : str[i]='s';
			  break;

case 'e' : str[i]='o';
			  break;

case 'f' : str[i]='c';
			  break;

case 'g' : str[i]='v';
			  break;

case 'h' : str[i]='x';
			  break;

case 'i' : str[i]='d';
			  break;

case 'j' : str[i]='u';
			  break;

case 'k' : str[i]='i';
			break;

case 'l' : str[i]='g';
			  break;

case 'm' : str[i]='l';
			  break;

case 'n' : str[i]='b';
			  break;

case 'o' : str[i]='k';
			  break;

case 'p' : str[i]='r';
			  break;

case 'q' : str[i]='z';
			  break;

case 'r' : str[i]='t';
			  break;

case 's' : str[i]='n';
			  break;

case 't' : str[i]='w';
			  break;

case 'u' : str[i]='j';
			  break;

case 'v' : str[i]='p';
			  break;

case 'w' : str[i]='f';
			  break;

case 'x' : str[i]='m';
			  break;

case 'y' : str[i]='a';
			  break;

case 'z' : str[i]='q';
			  break;


}

}

if(k!=0)
printf("Case #%d: %s\n",k,str);

}



return 0;

}
