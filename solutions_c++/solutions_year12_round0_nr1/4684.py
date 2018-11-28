#include<iostream>
#include<stdio.h>
#include<ctype.h>
using namespace std;
char str[26],str2[26];
char convert(char );
void initialise();
int main()
{
    FILE *fp,*fi;
    char c;
    initialise();
    fp=fopen("op.txt","w");
    fi=fopen("A-small-attempt1.in","r");
    int i=1,n;
    fscanf(fi,"%d",&n);
    c=fgetc(fi);
    c=fgetc(fi);
    fprintf(fp,"Case #%d: ",i);
    while(1)
    {
        fprintf(fp,"%c",convert(c));
        if(c=='\n')
        {
            i++;
            if(i>n)
                break;
            fprintf(fp,"Case #%d: ",i);
        }
        c=fgetc(fi);
    }
    fclose(fi);
    return 0;
}
char convert(char a)
{
    char b;
    if(islower(a))
        b=str2[(a-97)];
    else
        b=a;
    return b;
}
void initialise()
{
    FILE *fo=fopen("cipher.txt","r");
    char b;
    int i;
    for(i=0;i<26;i++)
    {
        str[i]=fgetc(fo);
        b=i+97;
    }
    for(i=0;i<26;i++)
    {
        b=str[i];
        str2[(b-97)]=97+i;
    }
    fclose(fo);
}
