#include <iostream>

void Sort(int* array, int size);

int main(int argc, char* argv[])
{
    
    if( argc < 2 )
    {
	std::cout << "Please enter test file!" << std::endl;
	exit(1);
    }
    
    //std::cout << argv[1] << std::endl;
    FILE* fp = fopen(argv[1], "r");
    if( fp == NULL )
    {
	std::cout << "Input file open failed!" << std::endl;
	exit(1);
    }

    FILE* fpout = fopen("output", "w");
    if( fpout == NULL )
    {
	std::cout << "Output file create failed!" << std::endl;
	exit(1);
    }

    int caseNum = 0;
    int T = 0;
    int NA = 0, NB = 0;
    fscanf(fp, "%d", &caseNum);
    //std::cout << caseNum << T << NA << NB << std::endl;

    int AtoB_d[100];
    int AtoB_a[100];
    int BtoA_d[100];
    int BtoA_a[100];

    int hour, minute;
    
    for( int j = 0; j < caseNum; j++ )
    {
	fscanf(fp, "%d%d%d", &T, &NA, &NB);
	//std::cout << T << " " << NA << " " << NB << std::endl;
    	for( int i = 0; i < NA; i++ )
    	{
    	    fscanf(fp, "%d:%d", &hour, &minute);
    	    AtoB_d[i] = hour*60 + minute;
	    //std::cout << hour << " " << minute << std::endl;
    	    fscanf(fp, "%d:%d", &hour, &minute);
    	    AtoB_a[i] = hour*60 + minute + T;
	    //std::cout << hour << " " << minute << std::endl;
	    //std::cout << AtoB_d[i] << "\t" << AtoB_a[i] << std::endl;
    	}

	Sort(AtoB_d, NA);
	Sort(AtoB_a, NA);

    	for( int i = 0; i < NB; i++ )
    	{
    	    fscanf(fp, "%d:%d", &hour, &minute);
    	    BtoA_d[i] = hour*60 + minute;
	    //std::cout << hour << " " << minute << std::endl;
    	    fscanf(fp, "%d:%d", &hour, &minute);
    	    BtoA_a[i] = hour*60 + minute + T;
	    //std::cout << hour << " " << minute << std::endl;
	    //std::cout << BtoA_d[i] << "\t" << BtoA_a[i] << std::endl;
    	}

	Sort(BtoA_d, NB);
	Sort(BtoA_a, NB);

	int a = 0, b = 0;
	int countA = 0;
	int stayA = 0;
	int countB = 0;
	int stayB = 0;
	

	while(1)
	{
	    if( a > NA -1 || b > NB -1 )
		break;

	    if( BtoA_a[b] < AtoB_d[a] )
	    {
		stayA++;
		b++;
	    }
	    else if ( BtoA_a[b] > AtoB_d[a] )
	    {
		if( stayA > 0 )
		    stayA--;
		else countA++;

		a++;
	    }
	    else
	    {
		a++;
		b++;
	    }
		
	}

	if( a < NA )
	{
	    if( stayA < (NA-a) )
	    	countA += (NA-a) - stayA;
	}
	
	//std::cout << "Case #" << j << ": " << countA;	
	fprintf(fpout, "Case #%d: %d", j+1, countA);
	
	a = 0, b = 0;
	while(1)
	{
	    if( a > NA -1 || b > NB -1 )
		break;

	    if( AtoB_a[a] < BtoA_d[b] )
	    {
		stayB++;
		a++;
	    }
	    else if ( AtoB_a[a] > BtoA_d[b] )
	    {
		if( stayB > 0 )
		    stayB--;
		else countB++;

		b++;
	    }
	    else
	    {
		a++;
		b++;
	    }
		
	}

	if( b < NB )
	{
	    if( stayB < (NB-b) )
	    	countB += (NB-b) - stayB;
	}

	//std::cout << " " << countB << std::endl;
	fprintf(fpout, " %d\n", countB);
    }	

    fclose(fp);
    fclose(fpout);
    

    
    
    return 0;
}

void Sort(int* array, int size)
{
    int tmp;
    for( int i = 0; i < size ; i++ )
    {
	for( int j = size-1; j > i; j-- )
	{
	    if( array[j] < array[j-1] )
	    {
		tmp = array[j];
		array[j] = array[j-1];
		array[j-1] = tmp;
	    }
	}
    }

    /*std::cout << "After sort" << std::endl;
    for( int i = 0; i < size; i++ )
    {
	std::cout << array[i] << std::endl;
    }*/
}
