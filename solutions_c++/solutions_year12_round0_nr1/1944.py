#include <cstdio>
#include <cstdlib>

int main ()
{
    char key[] = "yhesocvxduiglbkrztnwjpfmaq";
    char tmp[101];
    int t;

    scanf ("%d" ,&t);

    for (int i = 0 ; i < t ; i++)
    {
        scanf ("\n%[^\n]" , tmp);
        printf ("Case #%d: ",i+1);
        for (int j = 0 ; tmp[j] != '\0' ; j++)
        {
            if (tmp[j] == ' ')
            {
                printf (" ");
                continue;
            }
            printf ("%c" , key[tmp[j]-'a']);
        }
        printf ("\n");
    }

    return 0;
}
