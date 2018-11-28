/*
  // Code Jam 2010
  // Code By Igor Barros Barbosa
  //-----------------------------
  //  Roller Coaster Problem
  //  Use with two arguments : <inputfile> <outputfile>
  */
#include <stdio.h>
#include <math.h>


int main(int argc, char *argv[])
{

    FILE *pInput;
    FILE *pOutput;
    // Numbers of cases
    int n_cases;
    // Number of Places
    int n_Kapcity;
    //  Number runs
    int n_runs;
    //  Number of Groups
    int n_groups;
    // Actual Run


    //  One Argument
    if( argc == 1)
    {
        printf("Erro - Missing input file\n");
        return -1;
    }
    //  Two Arguments
    else if( argc==2 )
    {
        printf("Erro - Missing output File file\n");
        return -1;
    }
    //  Three Arguments
    else if ( argc==3 )
    {
        pInput = fopen(argv[1],"r");
        if(pInput == NULL)
        {
            printf("ERROR - Cannot open Input file %s",argv[1]);
            return 0;
        }
        pOutput= fopen(argv[2],"w+");
        if(pOutput== NULL)
        {
            printf("ERROR - Cannot open Output file %s",argv[2]);
            return 0;
        }
    }
    //Read number of case
    fscanf(pInput,"%d",&n_cases);


    for(long int cases =1 ; cases<=n_cases; cases++)
    {
        //  Get Number of runs
        fscanf(pInput,"%d",&n_runs);
        //  Get 'K'apcity
        fscanf(pInput,"%d",&n_Kapcity);
        // Get Number of groups
        fscanf(pInput,"%d",&n_groups);
        n_groups--;
        //populate group
        long int grupos[(n_groups)];
        long int soma_grupos=0;
        long int i=0;
        int pos;
        soma_grupos=0;
        for(i =0 ; i <= n_groups ; i++)
        {
            fscanf(pInput,"%li",&grupos[i]);
            //printf("\nGrupos[%d]=%d",i,grupos[i]);

        }
        int aux=0;
        i=0;
        int j=0;
        int q=0;
        while(n_runs)
        {
            if(( grupos[i] +aux )<= n_Kapcity)
            {
                if(aux!=0)
                {
                    if(pos!=i)
                    {
                        aux+=grupos[i];

                    }
                    else
                    {
                        soma_grupos+=aux;
                        j++;
                        n_runs--;
                        aux=0;
                    }
                }

                else
                {
                    aux=grupos[i];
                    pos=i;
                }
                i++;
                if(i>n_groups)
                    i=0;
            }
            else
            {
                soma_grupos+=aux;
                j++;
                n_runs--;
                aux=0;
            }

        }
        fprintf(pOutput,"Case #%li: %li\n",cases,soma_grupos);
    }
    fclose(pOutput);
    fclose(pInput);
    return 1;
}


