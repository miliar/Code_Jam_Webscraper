#include <cstdio>
using namespace std;

int main()
{
FILE *in = fopen("A-small.in","r");
FILE *out = fopen("A-small.out","w");

    char a[]="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upX";
    char g[]="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvX";
    
    char t[26];
    for (int i=0;i<26;i++)
        t[i]='#';
    
    t['q'-'a']='z';
    t['z'-'a']='q';
    
    int j=0;
    while (a[j]!='X')
    {
          t[g[j]-'a']=a[j]; 
          j++;
    }
    
    /*
    for (int i=0;i<26;i++)
        printf("%c -> %c\n",i+'a',t[i]);
    */
    
    int test;
    fscanf(in,"%d",&test);
    char c;
    fscanf(in,"%c",&c);
    for (int i=0;i<test;i++)
    {
        c='x';
        fprintf(out,"Case #%d: ",i+1);
        while (c!='\n')
        {
             fscanf(in,"%c",&c);
             if (c==' ') fprintf(out," "); 
             else if (c=='\n') fprintf(out,"\n");
             else fprintf(out,"%c",t[c-'a']);
        }
    }
    
    return(0);
}
