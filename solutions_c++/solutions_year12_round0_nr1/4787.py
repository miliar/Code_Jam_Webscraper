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
    map <char,char> my;
     for(i=0;i<strlen(a);i++)
    {
        my[a[i]]=x[i];
 
    }
    for(i=0;i<strlen(b);i++)
    {
        my[b[i]]=y[i];
 
    }
    for(i=0;i<strlen(c);i++)
    {
        my[c[i]]=z[i];
 
    }
    my['q']='z';
    my['z']='q';
    int j,t;
    scanf("%d",&t);
     gets(l);
    for(j=1;j<=t;j++)
    {
 
     gets(l);
     printf("Case #%d: ",j);
 
    for(i=0;i<strlen(l);i++)
    {
  
        cout<<my[l[i]];
    }
    cout<<endl;
    }
return 0;
}
 