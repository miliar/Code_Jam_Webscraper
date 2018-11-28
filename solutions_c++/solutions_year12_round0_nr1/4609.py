#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    char op[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    FILE *fp=fopen("A-small-attempt0.in", "r"), *ofp=fopen("A-small.txt", "w");
     int T,i;
     char g[102];

       fscanf(fp, "%d", &T);


        char c;
        c=fgetc(fp);
       for(int tc=1;tc<=T;tc++)
       {
               fgets(g,102,fp);

               for(i=0;g[i]!='\n';i++)
               {
                   if(g[i]!=' ')
                   g[i]=op[g[i]-97];
               }
               // print cases

               fprintf(ofp, "Case #%d: %s", tc, g);

       }
       return 0;
}
