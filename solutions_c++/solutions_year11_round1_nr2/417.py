#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>

using namespace std;

struct Palabra
{
    char letras[15];
    int longitud;
};

int diccionarioSize = 0;
struct Palabra diccionario[10001];
int diccionario2Size = 0;
struct Palabra diccionario2[10001];

void solveCase(int caseN, FILE *fp);

bool existsWordWith(char letra);
bool wordHasLetter(struct Palabra pal, char letter);
bool matchesInLetters(struct Palabra palSrc, struct Palabra palCmp, char letra);

int main()
{
    FILE *fp = fopen("output.txt", "w");

    int numberOfCases;
    fscanf(stdin, "%d", &numberOfCases);
    //printf("Lei %d casos\n", numberOfCases);
    for(int caseN = 0; caseN < numberOfCases; caseN++)
    {
        solveCase(caseN, fp);
    }

    fclose(fp);
    return 0;
}

void solveCase(int caseN, FILE *fp)
{

    int N, M;
    fscanf(stdin, "%d %d", &N, &M);

    for(int i=0; i < N; i++)
    {
        fscanf(stdin, "%s", diccionario[i].letras);
        diccionario[i].longitud = strlen(diccionario[i].letras);
    }
    diccionarioSize = N;


    fprintf(fp, "Case #%d:", (caseN + 1));

    char guess[30];
    for(int i=0; i < M; i++)
    {
        fscanf(stdin, "%s", guess);
        //printf("Adivina: %s\n", guess);
        int guessLength = strlen(guess);

        int bestPoint = 0;
        int bestPal = 0;

        for(int pal = 0; pal < diccionarioSize; pal++)
        {
            //printf("Probando puntaje con palara: %s\n", diccionario[pal].letras);
            // copiar diccionario
            for(int j=0; j < diccionarioSize; j++)
            {
                diccionario2[j] = diccionario[j];
            }
            diccionario2Size = diccionarioSize;



            // eliminar palabras que son de distinta longitud
            for(int j=0; j < diccionario2Size; j++)
            {
                if(diccionario2[j].longitud != diccionario[pal].longitud)
                {
                    diccionario2[j] = diccionario2[diccionario2Size - 1];
                    diccionario2Size--;
                    j--;
                }
            }

            int points = 0;

            for(int j=0; j < guessLength; j++)
            {
                if(existsWordWith(guess[j]))
                {
                    if(!wordHasLetter(diccionario[pal], guess[j]))
                    {
                        points++;

                        for(int k=0; k < diccionario2Size; k++)
                        {
                            if(wordHasLetter(diccionario2[k], guess[j]))
                            {
                                diccionario2[k] = diccionario2[diccionario2Size - 1];
                                diccionario2Size--;
                                k--;
                            }
                        }
                    }
                    else
                    {
                        for(int k=0; k < diccionario2Size; k++)
                        {
                            if(!matchesInLetters(diccionario[pal], diccionario2[k], guess[j]))
                            {
                                diccionario2[k] = diccionario2[diccionario2Size - 1];
                                diccionario2Size--;
                                k--;
                            }
                        }

                        if(diccionario2Size == 1)
                        {
                            break;
                        }
                    }
                }
            }

            //printf("Gasto %d puntos\n", points);

            if(points > bestPoint)
            {
                bestPoint = points;
                bestPal = pal;
            }
        }

        //printf(">>> Conviene adivinar la palabra: %s\n", diccionario[bestPal].letras);
        fprintf(fp, " %s", diccionario[bestPal].letras);
    }



    fprintf(fp, "\n");
    return;
}

bool existsWordWith(char letra)
{
    for(int i=0; i < diccionario2Size; i++)
    {
        if(wordHasLetter(diccionario2[i], letra))
        {
            return true;
        }
    }
    return false;
}

bool wordHasLetter(struct Palabra pal, char letter)
{
    int i = 0;
    while(pal.letras[i] != '\0')
    {
        if(pal.letras[i] == letter) return true;
        i++;
    }
    return false;
}


bool matchesInLetters(struct Palabra palSrc, struct Palabra palCmp, char letra)
{
    for(int i=0; i < palSrc.longitud; i++)
    {
        if(palSrc.letras[i] == letra)
        {
            if(palCmp.letras[i] == letra) continue;
            return false;
        }
        else if(palCmp.letras[i] == letra)
            return false;
    }
    return true;
}

