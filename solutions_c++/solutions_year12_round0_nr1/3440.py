#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

FILE *in = fopen ("A.in","r");
FILE *out = fopen ("A.out","w");

int main()
{
    char tr[100];
    string e[3],g[3];
    e[0]="our language is impossible to understand";
    e[1]="there are twenty six factorial possibilities";
    e[2]="so it is okay if you want to just give up";
    g[0]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    g[1]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    g[2]="de kr kd eoya kw aej tysr re ujdr lkgc jv";

    int i,j,t,c=1;
    for (i='a';i<='z';i++)
        tr[i-'a']=i;
    tr['y'-'a']='a';
    tr['q'-'a']='z';
    tr['e'-'a']='o';
    tr['z'-'a']='q';
    for (i=0;i<3;i++)
        for (j=0;j<g[i].size();j++)
            if (g[i][j]!=' ')
               tr[g[i][j]-'a']=e[i][j];

    fscanf (in,"%d\n",&t);

    for (c=1;c<=t;c++)
    {
        char x[200];
        fgets(x,150,in);
        string str=x,ret="";
        //cout << str << endl;
        for (i=0;i<str.size();i++)
        {
            if (str[i]==' ')
               ret+=" ";
            else
               ret+=tr[str[i]-'a'];
        }
        //cout << ret << endl;
        //system ("pause");
        fprintf (out,"Case #%d: %s\n",c,ret.c_str());
    }

    return 0;
}
