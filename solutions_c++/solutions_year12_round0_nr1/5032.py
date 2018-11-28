#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;
//char st0[]= "a zoo";
//char st0a[]="y qee";
char st0[]="z";
char st0a[]="q";

char st1[]= "ejp mysljylc kd kxveddknmc re jsicpdrysi";
char st1a[]="our language is impossible to understand";

char st2[]= "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char st2a[]="there are twenty six factorial possibilities";

char st3[]= "de kr kd eoya kw aej tysr re ujdr lkgc jv";
char st3a[]="so it is okay if you want to just give up";

char st4[]= "q";
char st4a[]="z";

char findChar(char c)
{
    unsigned int i;


    for (i=0; i<strlen(st0); i++)
    {
        if (st0[i]==c)
        {
            c=st0a[i];
            return c;
        }

    }


    for (i=0; i<strlen(st1); i++)
    {
        if (st1[i]==c)
        {
            c=st1a[i];
            return c;
        }

    }


    for (i=0; i<strlen(st2); i++)
    {
        if (st2[i]==c)
        {
            c=st2a[i];
            return c;
        }

    }

    for (i=0; i<strlen(st3); i++)
    {
        if (st3[i]==c)
        {
            c=st3a[i];
            return c;
        }

    }

        for (i=0; i<strlen(st4); i++)
    {
        if (st4[i]==c)
        {
            c=st4a[i];
            return c;
        }

    }

cout <<"\n*c=c* '"<<c<<"'\n";
    return c;

}
char strIn [255];
unsigned int n;
int main()
{
    unsigned int i,j;
    cin>>n;
    for (i=0; i<n; i++)
    {
        cin.getline(strIn,255);
        if (strlen(strIn)==0)
            cin.getline(strIn,255);
        for (j=0; j<strlen(strIn); j++)
            strIn[j]=findChar(strIn[j]);
        cout <<"Case #"<<i+1<<": "<< strIn<<endl;
    }
    return 0;
}
