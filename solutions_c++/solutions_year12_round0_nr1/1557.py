#include <stdio.h>

/*

Input
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv


Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up

*/

#define DEF_MAPPING(o, r) mapping_table[o] = r;

int main()
{
    char mapping_table['a' + 26];
    for (char c = 'a' ; c <= 'z' ; ++c) mapping_table[c] = c;

    DEF_MAPPING('a', 'y')
    DEF_MAPPING('b', 'h')
    DEF_MAPPING('c', 'e')
    DEF_MAPPING('d', 's')
    DEF_MAPPING('e', 'o')
    DEF_MAPPING('f', 'c')
    DEF_MAPPING('g', 'v')
    DEF_MAPPING('h', 'x')
    DEF_MAPPING('i', 'd')
    DEF_MAPPING('j', 'u')
    DEF_MAPPING('k', 'i')
    DEF_MAPPING('l', 'g')
    DEF_MAPPING('m', 'l')
    DEF_MAPPING('n', 'b')
    DEF_MAPPING('o', 'k')
    DEF_MAPPING('p', 'r')
    DEF_MAPPING('q', 'z')
    DEF_MAPPING('r', 't')
    DEF_MAPPING('s', 'n')
    DEF_MAPPING('t', 'w')
    DEF_MAPPING('u', 'j')
    DEF_MAPPING('v', 'p')
    DEF_MAPPING('w', 'f')
    DEF_MAPPING('x', 'm')
    DEF_MAPPING('y', 'a')
    DEF_MAPPING('z', 'q')


    FILE *ifile = freopen("A-small-attempt0.in", "r", stdin);
    FILE *ofile = freopen("output_data.txt", "w", stdout);

    int num_inputs;
    scanf("%d\n", &num_inputs);

    char buf[1024];
    for (int i = 0 ; i < num_inputs ; ++i)
    {
        gets(buf);
        for (char* p = buf ; *p ; ++p)
        {
            if (*p != ' ') 
            {
                *p = mapping_table[*p];
            }
        }

        printf("Case #%d: %s\n", (i+1), buf);
    }

    fclose(ifile);
    fclose(ofile);

    return 0;
}