#include <cstdio>
#include <string.h>

char replace (char c){
    switch (c){
        case 'a': return 'y';
        case 'b': return 'h';
        case 'c': return 'e';
        case 'd': return 's';
        case 'e': return 'o';
        case 'f': return 'c';
        case 'g': return 'v';
        case 'h': return 'x';
        case 'i': return 'd';
        case 'j': return 'u';
        case 'k': return 'i';
        case 'l': return 'g';
        case 'm': return 'l';
        case 'n': return 'b';
        case 'o': return 'k';
        case 'p': return 'r';
        case 'q': return 'z';
        case 'r': return 't';
        case 's': return 'n';
        case 't': return 'w';
        case 'u': return 'j';
        case 'v': return 'p';
        case 'w': return 'f';
        case 'x': return 'm';
        case 'y': return 'a';
        case 'z': return 'q';
        case ' ': return ' ';
        case '\n': return '\n';
    }

}

int main (){

    FILE *fin = fopen ("A-small-attempt0.in", "r");
    FILE *fout = fopen ("out.txt", "w");
    int n;
    fscanf (fin, "%d\n", &n);
    char line[200];
    for (int i = 0; i < n; i++){
        fgets(line, sizeof(line), fin);
        for (int j = 0; j < strlen(line); j++){
            line[j] = replace(line[j]);
        }
        printf ("Case #%d: %s", i+1, line);
        fprintf (fout, "Case #%d: %s", i+1, line);
    }
    fclose (fin);
    fclose (fout);

    return 0;
}
