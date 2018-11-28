
#include <cstdio>
#include <cstring>

int gao[256];
int main()
{
    char b1[256], b2[256];
    gets(b1);
    gets(b2);
    for (int i = 0; i < strlen(b1); ++i)
        gao[b1[i]] = b2[i];
    gets(b1);
    gets(b2);
    for (int i = 0; i < strlen(b1); ++i)
        gao[b1[i]] = b2[i];
    gets(b1);
    gets(b2);
    //gao['o'] = 'e';
    //gao['z'] = 'q';
    //gao['a'] = 'y';
    for (int i = 0; i < strlen(b1); ++i)
        gao[b1[i]] = b2[i];
    for (int i = 'a'; i <= 'z'; ++i)
        printf("'%c',", gao[i]);
}
/*
ejp mysljylc kd kxveddknmc re jsicpdrysi
our language is impossible to understand
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
there are twenty six factorial possibilities
de kr kd eoya kw aej tysr re ujdr lkgc jv
so it is okay if you want to just give up
*/