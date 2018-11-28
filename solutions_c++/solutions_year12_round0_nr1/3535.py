#include <cstdlib>
#include <iostream>
#define SIZE 256

using namespace std;

void getInput( char* p, int maxSize, FILE* fp )
{
    int l;
    p = fgets( p, maxSize, fp );
    l = strlen(p);
    if ( p[l-1] == '\n' )
    	p[l-1] = '\0';
}

int main(int argc, char *argv[])
{
    int tcases, tctr, i, j;
    char input[SIZE];
    char mapping[26] = { 'y', 'h', 'e', 's', 'o', 'c', 'v' ,'x' ,'d' ,'u' ,'i' ,'g' ,'l' ,'b' ,'k' ,'r' ,'z' ,'t', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };
    
    FILE* fp = fopen("A-small-attempt0.in", "r");
    FILE* fp2 = fopen("output.txt", "w");
    
    fscanf(fp, "%d\n", &tcases);
    for (tctr=0; tctr<tcases; tctr++)
    {
        memset(input, 0, SIZE);
        getInput(input, SIZE, fp);
        for (i=0; i<strlen(input); i++)
        {
            if (input[i] == ' ') continue;
            input[i] = mapping[ ((int(tolower(input[i]))) - 97) ];
        }
        fprintf(fp2, "Case #%d: %s\n", tctr+1, input);
    }
    
    fclose(fp);
    fclose(fp2);
}
