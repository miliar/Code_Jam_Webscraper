#include <iostream>
#include <string>
using namespace std;

void main()
{
    int i,n;
    FILE *fp1,*fp2;

    char str[110];

    fp1 = fopen("in.txt", "r");
    fp2 = fopen("out.txt", "w+");
    fscanf(fp1, "%d", &n);
    fgets(str, 110, fp1);

    for(i=1; i <= n; i++)
    {
        fgets(str, 110, fp1);

        /*
        a y
        b h
        c e
        d s
        e o
        f c
        g v
        h x
        i d
        j u
        k i
        l g
        m l
        n b
        o k
        p r
        q z
        r t
        s n
        t w
        u j
        v p
        w f
        x m
        y a
        z q
        */
        for (int j=0; j<strlen(str); j++)
        {
            switch (str[j])
            {
            case 'a':
                str[j] = 'y';
                break;
            case 'b':
                str[j] = 'h';
                break;
            case 'c':
                str[j] = 'e';
                break;
            case 'd':
                str[j] = 's';
                break;
            case 'e':
                str[j] = 'o';
                break;
            case 'f':
                str[j] = 'c';
                break;
            case 'g':
                str[j] = 'v';
                break;
            case 'h':
                str[j] = 'x';
                break;
            case 'i':
                str[j] = 'd';
                break;
            case 'j':
                str[j] = 'u';
                break;
            case 'k':
                str[j] = 'i';
                break;
            case 'l':
                str[j] = 'g';
                break;
            case 'm':
                str[j] = 'l';
                break;
            case 'n':
                str[j] = 'b';
                break;
            case 'o':
                str[j] = 'k';
                break;
            case 'p':
                str[j] = 'r';
                break;
            case 'q':
                str[j] = 'z';
                break;
            case 'r':
                str[j] = 't';
                break;
            case 's':
                str[j] = 'n';
                break;
            case 't':
                str[j] = 'w';
                break;
            case 'u':
                str[j] = 'j';
                break;
            case 'v':
                str[j] = 'p';
                break;
            case 'w':
                str[j] = 'f';
                break;
            case 'x':
                str[j] = 'm';
                break;
            case 'y':
                str[j] = 'a';
                break;
            case 'z':
                str[j] = 'q';
                break;
            }
        }
        
        fprintf(fp2, "Case #%d: %s",i, str);
    }
}