#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#define MAX(X,Y) ((X)>(Y)?(X):(Y))
#define MIN(X,Y) ((X)<(Y)?(X):(Y))
#define ABS(X)  ((X)>0?(X):(-(X)))
#define SWAP(TYPE,X,Y) {TYPE T=X; X=Y; Y=T;}
int nCase;
using namespace std;
#define SMALL
//#define LARGE
char bef[] = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
char aft[] = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
char chg[256], str[1005];
int main()
{
    #ifdef SMALL
    	freopen("A-small-attempt0.in","rt",stdin);
        freopen("A-small.out","wt",stdout);
    #endif
    #ifdef LARGE
    	freopen("A-large.in","rt",stdin);
        freopen("A-large.out","wt",stdout);
    #endif

    for(int i=0; bef[i]; i++)
        if(!chg[bef[i]])
            chg[bef[i]] = aft[i];
    chg['q'] = 'z';
    chg['z'] = 'q';
    
    scanf("%d\n",&nCase);
    for(int iCase=1; iCase<=nCase; iCase++)
    {
        gets(str);
        printf("Case #%d: ",iCase);
        for(int i=0; str[i]; i++)
            printf("%c",str[i]==' '?' ':chg[str[i]]);
        printf("\n");
    }
    scanf(" ");
    return 0;
}
