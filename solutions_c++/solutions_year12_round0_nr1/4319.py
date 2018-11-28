#include <iostream>
#include <string.h>
#include <windows.h>
#include <stdio.h>

using namespace std;
char enc1[]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
char dec1[]="our language is impossible to understand";
char enc2[]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char dec2[]="there are twenty six factorial possibilities";

char enc3[]="de kr kd eoya kw aej tysr re ujdr lkgc jvqz";
char dec3[]="so it is okay if you want to just give upzq";

char input[100];

int find(char* str,char chr);

int main()
{
    	FILE *fin  = fopen ("in", "r");

	FILE *fout = fopen ("out", "w");

int T;
	fscanf( fin, " %d", &T);

	for (int i=1;fscanf( fin, " %[^\n]", input)!=EOF;i++)
        {
            fprintf (fout, "Case #%d: ",i);
            for (int i=0;input[i]!=0;i++)
                {
                    if (find(enc1,input[i])!=-1)
                       {
                           fprintf( fout,"%c" ,dec1[find(enc1,input[i])]);
                       }
                    else if (find(enc2,input[i])!=-1)
                       {
                           fprintf( fout,"%c" ,dec2[find(enc2,input[i])]);
                       }
                    else  if (find(enc3,input[i])!=-1)
                       {
                           fprintf( fout,"%c" ,dec3[find(enc3,input[i])]);
                       }
                    else
                       {
                           fprintf(fout,"%c",input[i]);
                       }
                }
            fprintf(fout,"\n");

        }
    return 0;
}
int find(char* str,char chr)
{
    int len=lstrlen(str);
    for(int i=0;i<len;i++)
       {
           if (str[i]==chr)
              {
                  return i;
              }
       }
    return -1;
}
