#include <cstdlib>
#include <iostream>

#define LINE_MAX 200
#define MAX_Q 10

using namespace std;

long unsigned evalEuros(long unsigned Rruns, long unsigned kpeople, long unsigned Nqueues, long unsigned *g)
{
    long unsigned res = 0;
    long unsigned start = 0;
    for (int r = 0; r < Rruns; r++) 
    {
        long unsigned sm = 0;
        int sm_add = 0;
        for (int k = 0; k < Nqueues; k++)
        {
           sm_add = (k + start)%Nqueues;
           //printf ("sumAdd: %lu, k: %lu, sum: %lu, g[%d]: %lu \n", sm_add, k, sm, sm_add, g[sm_add]);
           if (sm + g[sm_add] > kpeople) break;
           sm += g[sm_add];  
           // ??? se al prox ciclo uscirò aggiorno sm_add
           if (k + 1 >= Nqueues) sm_add = (k + 1 + start)%Nqueues;
        }
        res += sm;
        start = sm_add; 
        //printf ("RUN: %lu, Added: %lu, New Sum: %lu, Start_at: %lu \n", r, sm, res, sm_add); 
    }
    return res;  
}

int main(int argc, char *argv[])
{
    FILE *pFileINP = fopen ("C-small-attempt2.in","r");
    FILE *pFileOUT = fopen ("C-small-attempt2.out","w");
    char lineINP[LINE_MAX];
    char lineOUT[LINE_MAX];

    long unsigned Tcases, Rruns, kpeople, Nqueues;
    long unsigned g[MAX_Q];
    
    if (fgets(lineINP, LINE_MAX, pFileINP) != NULL)
    {
       sscanf (lineINP, "%lu", &Tcases);
       printf ("I have read: %lu \n", Tcases); 
       for (unsigned i = 1;; i++)
       {      
          if (fgets(lineINP, LINE_MAX, pFileINP) == NULL) break;
          sscanf (lineINP, "%lu %lu %lu", &Rruns, &kpeople, &Nqueues);
          if (fgets(lineINP, LINE_MAX, pFileINP) == NULL) break;
          
          /*
          for (int k = 0, el = 0; k < Nqueues ;k++) 
          {
              el += sscanf (&lineINP[el], "%lu", &g[k]);
              printf ("RUN: %lu, Element: %lu\n", k, el);                     
          }
          */
          
          sscanf (lineINP, "%lu %lu %lu %lu %lu %lu %lu %lu %lu %lu", g, g+1, g+2, g+3, g+4, g+5, g+6, g+7, g+8, g+9);
          
          sprintf (lineOUT, "Case #%u: %u\n", i, evalEuros(Rruns, kpeople, Nqueues, g));
          fputs(lineOUT, pFileOUT);
       }
    }
    
    //for (long unsigned i=0; i < 32; i++) printf("%lu -> %lu\n", i, evalpwout(i));
    
    fclose (pFileINP);
    fclose (pFileOUT);
    system("PAUSE");
    return EXIT_SUCCESS;
}
