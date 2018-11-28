#include<stdio.h>
#include<string.h>
#include<map>
#include<iostream>
using namespace std;
int main()
{
    int i;
    char a[100]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    char b[100]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    char c[100]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    char x[100]="our language is impossible to understand";
    char y[100]="there are twenty six factorial possibilities";
    char z[100]="so it is okay if you want to just give up";
    char l[500];
    map <char,char> mymap;
    map <char,char>::iterator it;
/*
    fflush(stdin);
    gets(a);
    fflush(stdin);
    gets(b);
    fflush(stdin);
    gets(c);
    fflush(stdin);
    gets(x);
    fflush(stdin);
    gets(y);
    fflush(stdin);
    gets(z);
  */  for(i=0;i<strlen(a);i++)
    {
        mymap[a[i]]=x[i];

    }
    for(i=0;i<strlen(b);i++)
    {
        mymap[b[i]]=y[i];

    }
    for(i=0;i<strlen(c);i++)
    {
        mymap[c[i]]=z[i];

    }
    mymap['q']='z';
    mymap['z']='q';
    /*for ( it=mymap.begin() ; it != mymap.end(); it++ )
    cout << (*it).first << " => " << (*it).second<<endl ;
*/
    int j,t;
    scanf("%d",&t);
gets(l);
    for(j=1;j<=t;j++)
    {

//fflush(stdin);
gets(l);
printf("Case #%d: ",j);

        for(i=0;i<strlen(l);i++)
    {
        //if(mymap[l[i]]!=' ')
        cout<<mymap[l[i]];
    }
    cout<<endl;
    }
return 0;
}
