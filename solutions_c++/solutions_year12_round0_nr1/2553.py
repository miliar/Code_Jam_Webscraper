#include<stdio.h>
#include<string.h>
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
int i,t,l,j;
char a[200];
char c;
FILE *fp = fopen("C:\\Users\\Sameer\\Desktop\\A-small-attempt5.in", "r");
FILE *fq = fopen("C:\\Users\\Sameer\\Desktop\\output.out", "w");
fscanf(fp,"%d",&t);
fgetc(fp);
for(j=1;j<=t;j++)
{
    fgets(a,110,fp);
    l=strlen(a);
    for(i=0;i<l;i++)
    {
        c=a[i];
        switch(c)
        {
            case 'a' : a[i]='y';break;
            case 'b' : a[i]='h';break;
            case 'c' : a[i]='e';break;
            case 'd' : a[i]='s';break;
            case 'e' : a[i]='o';break;
            case 'f' : a[i]='c';break;
            case 'g' : a[i]='v';break;
            case 'h' : a[i]='x';break;
            case 'i' : a[i]='d';break;
            case 'j' : a[i]='u';break;
            case 'k' : a[i]='i';break;
            case 'l' : a[i]='g';break;
            case 'm' : a[i]='l';break;
            case 'n' : a[i]='b';break;
            case 'o' : a[i]='k';break;
            case 'p' : a[i]='r';break;
            case 'q' : a[i]='z';break;
            case 'r' : a[i]='t';break;
            case 's' : a[i]='n';break;
            case 't' : a[i]='w';break;
            case 'u' : a[i]='j';break;
            case 'v' : a[i]='p';break;
            case 'w' : a[i]='f';break;
            case 'x' : a[i]='m';break;
            case 'y' : a[i]='a';break;
            case 'z' : a[i]='q';break;
        }
    }
    fprintf(fq,"Case #%d: ",j);
    fputs(a,fq);
}
fclose(fp);
fclose(fq);
return 0;
}
