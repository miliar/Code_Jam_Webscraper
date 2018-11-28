#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

// Los números primos entre 1 y 1000
int primes[] = {2,
3,
5,
7,
11,
13,
17,
19,
23,
29,
31,
37,
41,
43,
47,
53,
59,
61,
67,
71,
73,
79,
83,
89,
97,
101,
103,
107,
109,
113,
127,
131,
137,
139,
149,
151,
157,
163,
167,
173,
179,
181,
191,
193,
197,
199,
211,
223,
227,
229,
233,
239,
241,
251,
257,
263,
269,
271,
277,
281,
283,
293,
307,
311,
313,
317,
331,
337,
347,
349,
353,
359,
367,
373,
379,
383,
389,
397,
401,
409,
419,
421,
431,
433,
439,
443,
449,
457,
461,
463,
467,
479,
487,
491,
499,
503,
509,
521,
523,
541,
547,
557,
563,
569,
571,
577,
587,
593,
599,
601,
607,
613,
617,
619,
631,
641,
643,
647,
653,
659,
661,
673,
677,
683,
691,
701,
709,
719,
727,
733,
739,
743,
751,
757,
761,
769,
773,
787,
797,
809,
811,
821,
823,
827,
829,
839,
853,
857,
859,
863,
877,
881,
883,
887,
907,
911,
919,
929,
937,
941,
947,
953,
967,
971,
977,
983,
991,
997};

int A, B, P;

int setNumber[1001];

int differentSets;

void InitSets()
{
     for (int i=A; i<=B; i++)
         setNumber[i] = i; 
}

int Share(int a, int b)
{
    // probar con cada primo
    int i;
    
    for (i=0; i<sizeof(primes); i++)
    {
        if (primes[i] < P)
           continue;
           
        if (a%primes[i] == 0 && b%primes[i] == 0)
           return 1;
    }
    return 0;
}

void UnifySets(int a, int b)
{
     int min;
     int setA, setB;
     
     setA = setNumber[a];
     setB = setNumber[b];
     
     if (setA < setB)
        min = setA;
     else
         min = setB;
         
     for (int i=A; i<=B; i++)
     {
         if (setNumber[i] == setA)
            setNumber[i] = min;
            
         if (setNumber[i] == setB)
            setNumber[i] = min;
     }
}

void SolveCase()
{
     int i, j;
     InitSets();
     
     // probar cada par de números para ver si quedan en el mismo set
     for (i=A; i<B; i++)
         for (j=A+1; j<=B; j++)
         {
             // Verificar si i y j comparten un factor primo mayor que P
             if ( Share(i, j) )
             {
                  // unificar los conjuntos
                  UnifySets(i, j);
             }
         }
         
     // Contar cuantos conjuntos diferentes quedaron
     differentSets = 0;
     
     int found;
     
     for (i=A; i<=B; i++)
     {
         
         // verificar si este es un conjunto nuevo revisando que no este contado atrás
         found = 0;
         for (j=A; j<i; j++)
             if (setNumber[i] == setNumber[j])
                found = 1;
                
         if (!found)
            differentSets++;
     }
}

int main()
{
	FILE *inFile, *outFile;

	inFile = fopen("input.txt", "rt");
	outFile = fopen("output.txt", "wt");

	int i, numCases;

	fscanf(inFile, "%d", &numCases);

	for (i=0; i<numCases; i++)
	{
        fscanf(inFile, "%d %d %d", &A, &B, &P);
		SolveCase();

		fprintf(outFile, "Case #%d: %d\n", i+1, differentSets);
	}

	fclose(inFile);
	fclose(outFile);

	return 0;
}
