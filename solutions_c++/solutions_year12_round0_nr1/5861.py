# include <stdio.h>
# include <stdlib.h>
# include <string.h>

# define MAXLENGTH 2000

char swap(char c)
{
    if (c=='y') return 'a';
    if (c=='n') return 'b';
    if (c=='f') return 'c';
    if (c=='i') return 'd';
    if (c=='c') return 'e';
    if (c=='w') return 'f';
    if (c=='l') return 'g';
    if (c=='b') return 'h';
    if (c=='k') return 'i';
    if (c=='u') return 'j';
    if (c=='o') return 'k';
    if (c=='m') return 'l';
    if (c=='x') return 'm';
    if (c=='s') return 'n';
    if (c=='e') return 'o';
    if (c=='v') return 'p';
    if (c=='z') return 'q';
    if (c=='p') return 'r';
    if (c=='d') return 's';
    if (c=='r') return 't';
    if (c=='j') return 'u';
    if (c=='g') return 'v';
    if (c=='t') return 'w';
    if (c=='h') return 'x';
    if (c=='a') return 'y';
    if (c=='q') return 'z';

    else return c;

}


int main ()
{
    int T,i,j=1;
    FILE *in, *out;

    in = fopen("A-small-attempt7.in", "r");
    out = fopen ("output.txt", "w");

    fscanf (in, "%d", &T);

  
    char str [MAXLENGTH];
    fgets(str, MAXLENGTH, in);

    while ( j <= T)
    {
        fgets(str, MAXLENGTH, in);
        for (i=0; i<strlen(str); i++)
        {
            str[i] = swap(str[i]);
        }

        printf ("Case #%d: ", j);
        fprintf (out, "Case #%d: ", j);
        printf("%s", str);
        fprintf(out, "%s", str);

        j++;
    }

    fclose(in);
    fclose(out);

    system("pause");
}
