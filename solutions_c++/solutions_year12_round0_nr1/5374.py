#include<iostream>
#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<ctype.h>

using namespace std;

int main()
{FILE *R,*S,*Ch;
char x[101],y;
int i,j,d[27],t,l,z=0;
Ch=fopen("C.txt","r");
y=fgetc(Ch);
i=1;
while(y!=EOF)
{j=int(y);
d[j-96]=i+96;
i++;
y=fgetc(Ch);
}
R=fopen("R","r");
S=fopen("S.txt","a");

fscanf(R,"%d",&t);fgets(x,100,R);
printf("%d\n",t);
while(z<t)
{fprintf(S,"\nCase #%d: ",z+1);
fgets(x,110,R);
{l=strlen(x);
printf("%d\n",l);
for(i=0;i<l;i++)
{ if(isalpha(x[i]))
{fputc(d[int(x[i]-96)],S);}
 else
fputc(x[i],S);
}}
z++;
}



getch();
return 0;
}
