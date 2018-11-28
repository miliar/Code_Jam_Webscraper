#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

//char googlereseMap[] = 
//{
//    'y', 'n',
//    'f', 'i',
//    'c', 'w',
//    'l', 'b',
//    'k', 'u',
//    'o', 'm',
//    'x', 's',
//    'e', 'v',
//    'z', 'p',
//    'd', 'r',
//    'j', 'g',
//    't', 'h',
//    'a', 'q'
//};

char googlereseMap[] = 
{
    'y', 'h',
    'e', 's',
    'o', 'c',
    'v', 'x',
    'd', 'u',
    'i', 'g',
    'l', 'b',
    'k', 'r',
    'z', 't',
    'n', 'w',
    'j', 'p',
    'f', 'm',
    'a', 'q'
};

int main(int argc, char * argv[])
{
    int amt; //Number of lines
    int i, j; //iterators
    char str[256]; //Buffer for string
    char filename[256];
    FILE *f_in, *f_out;

    printf("File to load: ");
    scanf("%s", filename);
    f_in = fopen(filename, "r");
    f_out = fopen("C:\out.txt", "w");

    fscanf(f_in, "%d", &amt); //Get the amount of lines
    fgetc(f_in); //Remove newline

    for(i = 0; i < amt; ++i)
    {
        fgets(str, 256, f_in);

        //Convert letters
        for(j = 0; str[j]; ++j)
            if(isalpha(str[j]))
                str[j] = googlereseMap[str[j]-'a'];

        fprintf(f_out, "Case #%d: %s", i+1, str);
    }
    
    system("pause");
    return 0;
}
