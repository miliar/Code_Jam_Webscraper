#include <stdio.h>
#include <iostream>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
#include <list>

using namespace std;

/*
bool isPrime[];

void prime(int n)
{
    int i,j,end;

    memset(isPrime,true,sizeof(isPrime));

    end = sqrt(n) +1;
    for (i=2; i<end; i++)
        if (isPrime[i]) {
            for(j=i*2; j<1001; j+=i)
                isPrime[j] = false;
        }
}
*/

#define for0(i,n)  for ((i)=0; (i)<(n); (i++))
#define for1(i,n)  for ((i)=1; (i)<=(n); (i++))
#define foriter(i,v)  for ((i)=(v).begin(); (i)!=(v).end(); (i)++)

map<char, char> dict;
char used[255];

void predo(char* l, char* a)
{
    int n = strlen(l);
    int i;
    for (i=0; i<n; i++) {
        dict[l[i]] = a[i];
        used[a[i]] = 1;
    }

}

void doit(char *a, char *l)
{
    int n = strlen(l);
    int i;
    for (i=0; i< n; i++)
        a[i] =  dict[l[i]];
    a[i] = '\0';
}

int main()
{
    int i,j,k,T,tt;
    char line[150], ans[150];

    dict['y'] = 'a';
    dict['e'] = 'o';
    dict[' '] = ' ';
    dict['q'] = 'z';
    dict['z'] = 'q';
    strcpy(line, "ejp mysljylc kd kxveddknmc re jsicpdrysi");
    strcpy(ans, "our language is impossible to understand");
    predo(line, ans);

    strcpy(line, "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
    strcpy(ans, "there are twenty six factorial possibilities");
    predo(line, ans);

    strcpy(line, "de kr kd eoya kw aej tysr re ujdr lkgc jv");
    strcpy(ans, "so it is okay if you want to just give up");
    predo(line, ans);
/*
    for (i='a'; i<='z'; i++)
        if (dict[i] == 0)
            printf("not find:%c\n", i);

    for (i='a'; i<='z'; i++)
        if (used[i] == 0)
            printf("not map:%c\n", i);

    for (i='a'; i<='z'; i++)
        printf("%c:%c ", i, dict[i]);
*/
    scanf("%d\n", &T);

    for0(tt,T) {
        gets(line);
        doit(ans,line);

        printf("Case #%d: ", tt+1);
        puts(ans);
    }
}
