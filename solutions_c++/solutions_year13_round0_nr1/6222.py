#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>

using namespace std;



/* Global Variables*/    
    int base[4][4];
    int total, notComplete;
    char *resultStr[4] =
    {
    	"O won",
    	"X won",
    	"Draw",
    	"Game has not completed"
    };
/*---------*/  



int powCal(int x, int n)
{
    int i = 0, result = 1;
    for(i = 0; i < n; i ++)
    {
        result *= x;
    }
    
    return result;
}


int checkResult()
{
	int i, j, cal;
	
	cal=0;
	
	
	
	for(i=0;i<4;i++)
	{
		cal=0;
		for(j=0;j<4;j++)
		{
			cal+=base[i][j];
		}
		printf("line %d cal %d\n", i, cal);
		if(cal==4 || cal==8)
			return 0;
		if(cal==35 || cal == 40)
			return 1;
	} 
	
	for(i=0;i<4;i++)
	{
		cal=0;
		for(j=0;j<4;j++)
		{
			cal+=base[j][i];
		}
		printf("raw %d cal %d\n", i, cal);
		if(cal==4 || cal==8)
			return 0;
		if(cal==35 || cal == 40)
			return 1;
	} 
	
	cal= 0;
	cal = base[0][0]+base[1][1]+base[2][2]+base[3][3];
	if(cal==4 || cal==8)
			return 0;
		if(cal==35 || cal == 40)
			return 1;
	
	cal= 0;
	cal = base[3][0]+base[2][1]+base[1][2]+base[0][3];
	if(cal==4 || cal==8)
			return 0;
		if(cal==35 || cal == 40)
			return 1;		
	
	if(notComplete ==true)
		return 3;
	else
		return 2;
	
}

int main(int argc, char *argv[])
{

    char *inFileName = "A-large.in";
    char *outFileName = "A-large.out";
    int i, j, k, s;
    int group;
    char charTmp;
/* Local Variables*/    
    int maxVal, endVal, result;
/*---------*/    
    FILE * pInFile, *pOutFile;
    


    if((pInFile = fopen(inFileName, "r")) == NULL)
          printf("error open file\n");

    if((pOutFile = fopen(outFileName, "w")) == NULL)
          printf("error open file\n");


    fscanf(pInFile, "%d\n", &group);
    printf("group %d\n", group);
    for(i =0; i< group; i++)
    {

		  result = 0;
		  notComplete =0;
		  
		  printf("case %d\n", i);
		  
	        for(j = 0; j < 4; j++)
	        {
	            for(k=0;k<5;k++)
	            {
	            	fscanf(pInFile, "%c", &charTmp);
	            	
	            	if(k==4)
	            		break;
	            	switch(charTmp)
	            	{
	            		case 'O':
	            			base[j][k]= 1;
	            		
	            			break;
	            		case 'X':
	            			base[j][k]= 10;
	            			break;
	            		case 'T':
	            			base[j][k]= 5;
	            			break;
	            		case '.':
	            			base[j][k]= 0;
	            			notComplete = 1;
	            			break;
	            	}
	            }
					 
	        }
	        
	        result= checkResult();
			
            fprintf(pOutFile, "Case #%d: %s\n", i+1, resultStr[result]);
            fscanf(pInFile, "%c", &charTmp);
    }
        
    fclose(pInFile);
    fclose(pOutFile);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}



