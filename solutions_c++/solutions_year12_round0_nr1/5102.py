#include <cstdio>

char input[] =
"ejp mysljylc kd kxveddknmc re jsicpdrysi "
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd "
"de kr kd eoya kw aej tysr re ujdr lkgc jv ";

char output[] =
"our language is impossible to understand "
"there are twenty six factorial possibilities "
"so it is okay if you want to just give up ";

char table[26] = { 0 };

void decode() {
    for (int i = 0; input[i]; ++i)
        if (input[i] != ' ')
            table[input[i] - 'a'] = output[i];
    table['y'-'a'] = 'a';
    table['e'-'a'] = 'o';
    table['q'-'a'] = 'z';
    int sum = 0;
    int index = -1;
    for (int i = 0; i < 26; ++i)
        if (table[i] != 0)
            sum += table[i] - 'a';
        else
            index = i;
    if (index != -1)
        table[index] = 'a' + 25 * 26 / 2 - sum;
    int unmatched = 0;
    for (int i = 0; i < 26; ++i)
        if (table[i] == 0)
            printf("Unmatched character: %c\n", i + 'a');
}

int main() {
    decode();
    int t; scanf("%d\n", &t);
    char line[101];
    for (int caseid = 1; caseid <= t; ++caseid) {
        gets(line);
        for (int i = 0; line[i]; ++i)
            if (line[i] != ' ')
                line[i] = table[line[i] - 'a'];
        printf("Case #%d: %s\n", caseid, line);
    }
    return 0;
}
