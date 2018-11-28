#include<stdio.h>
#include<iostream>
#include<string.h>
#include<ctype.h>
#include<map>
using namespace std;

int main()
{
    int n;

    FILE *in = fopen("A-small-attempt0.in","r");
    FILE *out = fopen("A_out.txt","w");

    map<char,char> m;

    m['a']='y';
    m['b']='h';
    m['c']='e';
    m['d']='s';
    m['e']='o';
    m['f']='c';
    m['g']='v';
    m['h']='x';
    m['i']='d';
    m['j']='u';
    m['k']='i';
    m['l']='g';
    m['m']='l';
    m['n']='b';
    m['o']='k';
    m['p']='r';
    m['q']='z';
    m['r']='t';
    m['s']='n';
    m['t']='w';
    m['u']='j';
    m['v']='p';
    m['w']='f';
    m['x']='m';
    m['y']='a';
    m['z']='q';

    char str[110];

    fscanf(in,"%d\n",&n);

    for(int Case=1; Case<=n; Case++){
        fgets(str,110,in);

        fprintf(out,"Case #%d: ",Case);

        int len = strlen(str);

        for(int i=0;i<len-1;i++)
        {
            if(str[i]==' ')
                fprintf(out," ");
            else if(isupper(str[i]))
            {
                char ans = m[ str[i]-'A'+'a' ];
                fprintf(out,"%c",ans-'a'+'A');
            }
            else
            {
                char ans = m[ str[i] ];
                fprintf(out,"%c",ans);
            }
        }
        fprintf(out,"\n");
    }
    fclose(in);
    fclose(out);
    return 0;
}
