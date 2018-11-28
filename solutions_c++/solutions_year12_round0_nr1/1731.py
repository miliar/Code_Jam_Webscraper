#include <cstdio>
#include <cstring>

char table[26];

void
init_table()
{
    char str1[] = "our language is impossible to understand";
    char str2[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    char str3[] = "there are twenty six factorial possibilities";
    char str4[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    char str5[] = "so it is okay if you want to just give up";
    char str6[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

    for (int i = 0; i < 26; i++)
        table[i] = '*';
    for (int i = 0; i < strlen(str1); i++)
        if (str2[i] != ' ')
            table[ str2[i]-'a' ] = str1[i];
    for (int i = 0; i < strlen(str1); i++)
        if (str4[i] != ' ')
            table[ str4[i]-'a' ] = str3[i];
    for (int i = 0; i < strlen(str1); i++)
        if (str6[i] != ' ')
            table[ str6[i]-'a' ] = str5[i];

    // come from hint
    table['q'-'a'] = 'z';
    table['z'-'a'] = 'q';
}

void
print_table()
{
    for (int i = 0; i < 26; i++)
        printf("%c ", i+'a');
    printf("\n");
    for (int i = 0; i < 26; i++)
        printf("%c ", table[i]);
    printf("\n");
}

void
parse(char * src)
{
    while (*src)
    {
        if (*src == ' ')
            printf(" ");
        else
            printf("%c", table[*src - 'a']);
        src++;
    }
    printf("\n");
}

int
main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    init_table();
//    print_table();
    int T;
    scanf("%d", &T);
    getchar();
    char str[101];
    for (int case_i = 1; case_i <= T; case_i++)
    {
        gets(str);
        printf("Case #%d: ", case_i);
        parse(str);
    }

    return 0;
}
