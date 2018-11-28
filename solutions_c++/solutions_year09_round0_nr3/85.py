#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std ;

#define mod 10000

char str[505];
int best[505][20];
char sent[50]="welcome to code jam";
int n;
FILE *in=fopen("wel.in","r");

void scan()
{
    char ch;
    n=0;
    while (1)
    {
        fscanf(in,"%c",&ch);
        if (ch=='\n')break;
        str[n]=ch;
        n++;
    }
    str[n]='\0';
    return;
}
int solve(int ind,int let)
{
    if (best[ind][let]!=-1)return best[ind][let];
    if (let==18)return 1;
    int c,c2;
    int ret=0;
    for (c=ind+1;c<n;c++)
    if (str[c]==sent[let+1])
    {
        ret+=solve(c,let+1);
        ret%=mod;
    }
    return best[ind][let]=ret;
}

int main()
{
    freopen("wel.out","w",stdout);
    int c,c2;
    int tests;
    fscanf(in,"%d\n",&tests);
    int testn=1;
    while(tests)
    {
        printf("Case #%d: ",testn);
        testn++;
        tests--;
        scan();
        memset(best,-1,sizeof(best));
        int ret=0;
        for (c=0;c<n;c++)
        if (str[c]=='w')
        {
            ret+=solve(c,0);
            ret%=mod;
        }
        int num=ret;
        int nn=0;
        while(num){num/=10;nn++;}
        for (c=0;c<4-nn;c++)printf("0");
        if (ret>0)
        printf("%d",ret);
        printf("\n");
    }
//    system("pause");
    return 0;
}
