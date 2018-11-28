#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>



using namespace std;

char d[256];

int main()
{
const char *a=
"ejp mysljylc kd kxveddknmc re jsicpdrysi"
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
"de kr kd eoya kw aej tysr re ujdr lkgc jv",
*b=
"our language is impossible to understand"
"there are twenty six factorial possibilities"
"so it is okay if you want to just give up";

        d['q'+128]='z';
        d['z'+128]='q';
        int n = strlen(a);
        for (int i = 0; i < n; ++i)
                d[a[i] + 128] = b[i];
        for (int i = 'a'; i <= 'z'; ++i)
                cerr << d[i + 128] << endl;
        scanf("%d", &n);
        char s[1111];
        gets(s);
        for (int i = 1; i <= n; ++i)
        {
                gets(s);
                for (int j = 0; j < strlen(s); ++j)
                        s[j] = d[s[j] + 128];
                printf("Case #%d: ", i);
                puts(s);
        }
        return 0;
}
