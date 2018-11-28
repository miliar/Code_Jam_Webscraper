#include <stdio.h>
#include <string.h>

int L, D, N;

char words[6000][30];
char tokens[100][100];

void Tokenize(char curWord[])
{
    int curTokenIx = 0;
    int curTokenLen = 0;
    int i;
    int lenWord;
    int tokenizing = 0;

    lenWord = strlen(curWord);

    for (i=0; i<lenWord; i++)
    {
        // Mirar la letra actual
        // ver si es normal, inicio de token, o fin de token
        if (curWord[i] == '(')
        {
            tokenizing = 1;
        }
        else if (curWord[i] == ')')
        {
            tokenizing = 0;
        }
        else
        {
            tokens[curTokenIx][curTokenLen++] = curWord[i];
        }

        if (!tokenizing)
        {
            tokens[curTokenIx][curTokenLen] = '\x0';
            curTokenIx++;
            curTokenLen = 0;
        }
    }
}

int Match(char patternWord[])
{
    int matching = 1;

    for (int i=0; i<L; i++)
    {
        char compareStr[2] = " ";

        compareStr[0] = patternWord[i];
        if ( strstr(tokens[i], compareStr) == NULL )
        {
            matching = 0;
            break;
        }
    }

    return matching;
}

int MatchCount()
{
    int matchWords = 0;

    for (int i=0; i<D; i++)
    {
        if ( Match(words[i]) )
            matchWords++;
    }

    return matchWords;
}

int main()
{
    int testCase;
    FILE *inFile, *outFile;
    char curWord[1000];

    inFile = fopen("input.txt", "rt");
    outFile = fopen("output.txt", "wt");

    fscanf(inFile, "%d %d %d", &L, &D, &N);

    for (int curWordIx=0; curWordIx<D; curWordIx++)
    {
        // Cargar las palabras
        fscanf(inFile, "%s", words[curWordIx]);
    }
    

    for (testCase=1; testCase<=N; testCase++)
    {
        fscanf(inFile, "%s", curWord);

        Tokenize(curWord);
        
        int matchWords = MatchCount();

        fprintf(outFile, "Case #%d: %d\n", testCase, matchWords);
    }
    
    fclose(outFile);
    fclose(inFile);
    return 0;
}
