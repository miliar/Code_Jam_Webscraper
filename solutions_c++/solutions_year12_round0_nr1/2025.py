#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int c[30];

void init()
{
    c[0]=24;
    c[1]=7;
    c[2]=4;
    c[3]=18;
    c[4]=14;
    c[5]=2;
    c[6]=21;
    c[7]=23;
    c[8]=3;
    c[9]=20;
    c[10]=8;
    c[11]=6;
    c[12]=11;
    c[13]=1;
    c[14]=10;
    c[15]=17;
    c[16]=25;
    c[17]=19;
    c[18]=13;
    c[19]=22;
    c[20]=9;
    c[21]=15;
    c[22]=5;
    c[23]=12;
    c[24]=0;
    c[25]=16;
}

char s[1000];
int cc=0;

int main()
{
    init();
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    gets(s);
    while (t--)
    {
        gets(s);
        printf("Case #%d: ",++cc);
        int l=strlen(s);
        for (int i=0;i<l;i++)
            if (s[i]==' ') printf(" ");
            else printf("%c",c[s[i]-'a']+'a');
        puts("");
    }
    return 0;
}
