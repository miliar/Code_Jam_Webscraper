#include<iostream>
#include<queue>
#include<stdlib.h>
#include<string.h>
#include <stdio.h>
#include <math.h>
#define N 6010
#define MAX 20000000
#define MAXX(a,b) (a<b?b:a)
#include <iostream>


char trans[26];
void init()
{
    char s[3][100] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
                    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                    "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
    char a[3][100] = {"our language is impossible to understand",
                    "there are twenty six factorial possibilities",
                    "so it is okay if you want to just give up"};
    int i, j;
    for(i = 0; i < 26; i++)trans[i] = -1;
    trans['q'-'a']='z';
    trans['z'-'a']='q';
    for(i = 0; i < 3; i++) {
        for(j = 0; j < strlen(a[i]); j++) {
            if(a[i][j] >= 'a' && a[i][j] <= 'z') {
            //printf("j = %d\n", j);
                trans[s[i][j]-'a'] = a[i][j];
            //printf("j = %d\n", j);

            }
        }
    }
   // for(i = 0; i < 26; i++)printf("%c %c\n", i+'a', trans[i]);
}

int main()
{
    int n;
    int i, j;
    char str[1024];
    char ans[1024];
     init();
  //  freopen("in","r",stdin);freopen("out","w",stdout);
    scanf("%d", &n);
    gets(str);
    for(i = 1; i <= n; i++)
    {
        gets(str);
        printf("Case #%d: ", i);
        j = strlen(str);
        if(str[j-1]=='\n')str[j-1]='\0';
        for(j = 0 ; j< strlen(str); j++) {
            //if(str[j] == ' ')printf(" ");
            if(str[j] >= 'a' && str[j] <= 'z')printf("%c", trans[str[j]-'a']);
            else printf("%c", str[j]);
        }
        printf("\n");
    }
    return 0;
}
