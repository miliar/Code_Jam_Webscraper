#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main()
{
    int n,out=1;
    FILE *fp1,*fp2;
    fp1=fopen("d:\\1.in","r+");
    fp2=fopen("d:\\1.out","w+");
    char trans[128];
    char str1[105]="ejp mysljylc kd kxveddknmc re jsicpdrysi",
         str2[105]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
         str3[105]="de kr kd eoya kw aej tysr re ujdr lkgc jv";

    char str11[105]="our language is impossible to understand",
         str22[105]="there are twenty six factorial possibilities",
         str33[105]="so it is okay if you want to just give up";
    for(int i=0;i<strlen(str1);i++)
        {
        trans[str1[i]]=str11[i];
        }
    for(int i=0;i<strlen(str2);i++)
        {trans[str2[i]]=str22[i];
        }
    for(int i=0;i<strlen(str3);i++)
        {trans[str3[i]]=str33[i];
        }
    trans['q']='z';
    trans['z']='q';

    fscanf(fp1,"%d\n",&n);
    while(n--)
    {
        char ch;
        fprintf(fp2,"Case #%d: ",out++);
        while((ch=getc(fp1))!='\n')
            fprintf(fp2,"%c",trans[ch]);
        fprintf(fp2,"\n");
    }
    return 0;
}
