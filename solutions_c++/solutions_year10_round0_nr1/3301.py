/*
 // Code Jam 2010
 // Code By Igor Barros Barbosa
 //-----------------------------
 //  Snapper Problem
 //  Use with two arguments : <inputfile> <outputfile>
  */
#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[])
{

    FILE *pInput;
    FILE *pOutput;
    // Operator used to check what will be the result
    int operador;
    //result
    int result;
    //result string
    char str_result[4];
    // Numbers of cases
    int n_cases;
    // NUmber of Devices
    int n_devices;
    //Number of Snapps
    int n_snapps;
    // One Argument
    if( argc == 1)
    {
        printf("Erro - Missing input file\n");
        return -1;
    }
    // Two Arguments
    else if( argc==2 )
    {
        printf("Erro - Missing output File file\n");
        return -1;
    }
    // Three Arguments
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
    // Reade numbers of cases
    fscanf(pInput,"%d",&n_cases);
    //printf("Cases :%d",n_cases);
    for(int i =1 ; i<=n_cases; i++ )
    {
        //Get Devices
        fscanf(pInput,"%d",&n_devices);
        //Get Snapps
        fscanf(pInput,"%d",&n_snapps);
        //Operador
        operador=pow(2,n_devices)-1;
        // Calculate if is on
        result = n_snapps & operador;
        //printf("\NResults = %d",result);
        if(result == operador)
            sprintf(str_result,"ON");
        else
            sprintf(str_result,"OFF");
        fprintf(pOutput,"Case #%d: %s\n",i,str_result);
    }
    fclose(pOutput);
    fclose(pInput);
    return 1;
}
