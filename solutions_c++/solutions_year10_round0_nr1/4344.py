#include <cstdlib>
#include <iostream>
#define LINE_MAX 20000
#define MAX_LEN_INT 30

using namespace std;


long unsigned evalpwout (long unsigned pwout) 
{
    unsigned long out = 0;
    for (int i = 0; i < MAX_LEN_INT; i++)
    {
        if (pwout & 1) out = (out << 1) | 1;
        else return out;
        pwout = pwout >> 1;
    }
    return out;
}

unsigned snapperON_OFF(long unsigned Nsnapper, long unsigned Ktimes) 
{
    long unsigned pwinp = 0;
    long unsigned pwout = 0;
    long unsigned state = 0;
    unsigned ret = 0;
    long unsigned mask = 0;
    
    for (int i = 0; i < Nsnapper; i++) mask = (mask << 1) | 1;
    
    //printf ("N_snapper: %4lu, K_Times: %4lu \n", Nsnapper, Ktimes);
    
    for (unsigned k = 0; k < Ktimes; k++)
    {
        // Valori ad S-
        pwinp = ((pwout << 1) | 1) & mask;
        pwout = (pwinp & state) & mask;
        pwout = evalpwout(pwout);        
        //printf ("S- Run: %4lu, PW_Input: %4lu, State: %4lu, PW_Output: %4lu \n", k, pwinp, state, pwout);
        
        // Valori ad S+
        pwinp = ((pwout << 1) | 1) & mask;
        state = (pwinp ^ state) & mask;
        pwout = (pwinp | state) & mask;
        pwout = evalpwout(pwout);                     
        
        //printf ("S+ Run: %4lu, PW_Input: %4lu, State: %4lu, PW_Output: %4lu \n", k, pwinp, state, pwout);
    }
    pwinp = ((pwout << 1) | 1) & mask;
    pwout = (pwinp & state) & mask;
    pwout = evalpwout(pwout);
    ret = (pwout >> (Nsnapper - 1)) & 1;
    //printf ("Final PW_Out: %4lu, Result: %4lu \n\n", pwout, ret);
    return ret;
}

int main(int argc, char *argv[])
{
    FILE *pFileINP = fopen ("A-small-attempt1.in","r");
    FILE *pFileOUT = fopen ("A-small-attempt1.out","w");
    char lineINP[LINE_MAX];
    char lineOUT[LINE_MAX];

    long unsigned Tcases, Nsnapper, Ktimes;
    
    if (fgets(lineINP, LINE_MAX, pFileINP) != NULL)
    {
       sscanf (lineINP, "%lu", &Tcases);
       printf ("I have read: %lu \n", Tcases); 
       for (unsigned i = 1;(fgets(lineINP, LINE_MAX, pFileINP) != NULL); i++)
       {      
          sscanf (lineINP, "%lu %lu", &Nsnapper, &Ktimes);
          sprintf (lineOUT, "Case #%u: %s\n", i, snapperON_OFF(Nsnapper, Ktimes)?"ON":"OFF");
          printf ("%s", lineOUT);
          fputs(lineOUT, pFileOUT);
       }
    }
    
    fclose (pFileINP);
    fclose (pFileOUT);
    system("PAUSE");
    return EXIT_SUCCESS;
}
