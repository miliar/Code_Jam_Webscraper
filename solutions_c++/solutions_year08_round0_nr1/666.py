#include <stdio.h>
#include <string.h>


// Constante INFINITO
#define INFINITO 32000

// Los nombres de los motores de búsqueda
char searchEngines[101][110];
// palabras a buscar
char wordList[1001][110];
// mínimo número de cambios para llegar a una palabra
int minChanges[1001];
// Los valores del caso a resolver
int Q, S;

// Función para resolver cada caso
int SolveCase()
{
    int i, j, k;
    int lastChange;
    
    if (Q == 0) return 0;
    
    // Inicializar el centinela en la posición 0 de la lista de palabras
    strcpy(wordList[0], "*");
    minChanges[0] = -1;

    // Inicializar el mínimo número de cambios a Infinito para todo el arreglo
    for (i=1; i<=Q; i++)
        minChanges[i] = INFINITO;

    // Arrancar en cada posición de Query para ver hasta donde podemos avanzar
    for (i=0; i<=Q; i++)
    {
        // Con cuantos cambios de motor de búsqueda hemos llegado hasta i
        lastChange = minChanges[i];
        
        // Probar ahora con cada motor de búsqueda hasta donde podemos avanzar
        for (j=0; j<S; j++)
        {
            k = i+1;
            while ((k<=Q) && (strcmp(wordList[k], searchEngines[j]) != 0) )
            {
                  // Revisamos si se mejora el mínimo de llegada hasta esta
                  // palabra
                  if (lastChange+1 < minChanges[k])
                     minChanges[k] = lastChange + 1;
                     
                  k++;
            }                  
        }
    }
        
    // Retornar el mínimo número de cambios a aplicar
    return minChanges[Q];
}

// Limpia una cadena de el \n y el \r
void clrStr(char *string)
{
    if ( string[strlen(string)-1] == '\n')
       string[strlen(string)-1] = '\0';
}

int main(int argc, char *argv[])
{
    int i, j, numCases;
    int minCh = 0; // Mínimo número de cambios para cada caso
    char inString[200];
    FILE *inFile;
    FILE *outFile;
    
    inFile = fopen("input.txt", "rt");
    outFile = fopen("output.txt", "wt");
    
    // Leer el número de casos a resolver
    fgets(inString, 200, inFile);
    sscanf(inString, "%d", &numCases);
    
    for (i=0; i<numCases; i++)
    {
        // Leer los datos del número de buscadores
        fgets(inString, 200, inFile);
        sscanf(inString, "%d", &S);
        
        // Leer cada uno de los buscadores
        for (j=0; j<S; j++)
        {
            fgets(inString, 200, inFile);
            clrStr(inString);
            strcpy(searchEngines[j], inString );
        }
            
        // Leer los datos del número de palabras a buscar
        fgets(inString, 200, inFile);
        sscanf(inString, "%d", &Q);
        
        // Leer la lista de palabras a buscar
        for (j=0; j<Q; j++)
        {
            fgets(inString, 200, inFile);
            clrStr(inString);
            strcpy(wordList[j+1],  inString);
        }
        
        // Resolver el caso
        int minCh = SolveCase();
        
        // imprimir la respuesta en el archivo de salida
        fprintf(outFile, "Case #%d: %d\n", i+1, minCh);
    }
    
    fclose(inFile);
    fclose(outFile);

    return 0;
}
