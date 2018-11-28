#include <cstdio>
#include <memory.h>

void fillMap(char gToNMap[], char gWords[], char nWords[]);

int main() 
{
    char case1G[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    char case2G[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    char case3G[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    char case4G[] = "qz";
    char case1N[] = "our language is impossible to understand";
    char case2N[] = "there are twenty six factorial possibilities";
    char case3N[] = "so it is okay if you want to just give up";
    char case4N[] = "zq";
    char gToNMap[26];
    memset(gToNMap, 0, sizeof(gToNMap));
    fillMap(gToNMap, case1G, case1N);
    fillMap(gToNMap, case2G, case2N);
    fillMap(gToNMap, case3G, case3N);
    fillMap(gToNMap, case4G, case4N);
    /*
    for (int idx = 0; idx < 26; ++idx)
    {
        printf("%c: %c\n", idx + 'a', gToNMap[idx]);
    }
    */
    int t;
    scanf("%d", &t);
    char input[101];
    char output[101];
    gets(input);
    for (int caseNum = 1; caseNum <= t; ++caseNum)
    {
        memset(output, 0, sizeof(output));
        gets(input);
        int idx = 0;
        while (input[idx] != '\0')
        {
            output[idx] = gToNMap[input[idx] - 'a'];
            ++idx;
        }
        output[idx] = '\0';
        printf("Case #%d: %s\n", caseNum, output);
    }
    return 0;
}

void fillMap(char gToNMap[], char gWords[], char nWords[]) 
{
    int ptr = 0;
    while (gWords[ptr] != '\0')
    {
        gToNMap[gWords[ptr] - 'a'] = nWords[ptr];
        ++ptr;
    }
}
