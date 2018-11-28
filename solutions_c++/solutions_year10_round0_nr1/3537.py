// Codejam0.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdlib.h"


int _tmain(int argc, _TCHAR* argv[])
{
    int items = 0;
    int N;
    int K;

    FILE * inFile;
    FILE * outFile;

    inFile = fopen ("C:/Documents and Settings/Mike/My Documents/Visual Studio 2008/Projects/Codejam0/Debug/A-large.in","r");
    outFile = fopen ("C:/Documents and Settings/Mike/My Documents/Visual Studio 2008/Projects/Codejam0/Debug/mikeh.txt","w");

    fscanf (inFile, "%d", &items);

    printf("items: %d", items);

    for (int i = 0; i < items; i++)
    {
        fscanf (inFile, "%d", &N);
        fscanf (inFile, "%d", &K);

        if (((K + 1) % (1<<N)) == 0)
        {    
            fprintf (outFile, "Case #%d: ON\n",i+1);
        } 
        else
        {
            fprintf (outFile, "Case #%d: OFF\n",i+1);
        }

        //printf("items: %d", items);
    }    
        
    system("PAUSE");
    fclose (inFile);
    fclose (outFile);
	return 0;
}

