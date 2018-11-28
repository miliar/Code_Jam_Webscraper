#include <Windows.h>
#include <fstream>
#include <string>

int suprise = 0;
/******************************************************************/
/******************************************************************/

bool checkTriple(int summe, int p)
{
	bool noWinner = false;
	if(p == 0)
		return true;

	/*printf("_-----------------_\n");
	printf("Value %i  and  P %i \n",summe,p);*/

	// if value greater  3*p
	if(summe >= 3*p)
	{
		//int tripleBIG[3] = {10,10,10};
		//int ptr = 0;
		//while( tripleBIG[0] + tripleBIG[1] + tripleBIG[2] != summe)
		//{
		//	tripleBIG[ptr]--;

		//	ptr++;
		//	ptr%=3;

		//	if(tripleBIG[0] < p && tripleBIG[1] < p && tripleBIG[2] < p)
		//	{
		//		noWinner = true;
		//		break;
		//	}
		//}

		////printf("BIG: %i %i %i  | %s\n",tripleBIG[0],tripleBIG[1],tripleBIG[2], (noWinner)? "true" : "false");
		//if(!noWinner && (tripleBIG[0] + tripleBIG[1] + tripleBIG[2] == summe))
			return true;
	}

	// if value less than 3*p
	// first chance
	int tripleFirst[3] = {p,p,p};
	int ptr = 0;
	while( tripleFirst[0] + tripleFirst[1] + tripleFirst[2] != summe)
	{
		tripleFirst[ptr]--;

		ptr++;
		ptr%=3;

		if(tripleFirst[0] != p && tripleFirst[1] != p && tripleFirst[2] != p)
		{
			noWinner = true;
			break;
		}
	}

	//printf("First: %i %i %i  | %s\n",tripleFirst[0],tripleFirst[1],tripleFirst[2], (noWinner)? "true" : "false");
	if(!noWinner && (tripleFirst[0] + tripleFirst[1] + tripleFirst[2] == summe))
		return true;

	// second chance !!!
	ptr = 0;
	noWinner = false;
	int tripleSecond[3] = {p,p,p};

	if(suprise>0)
	{
		while( tripleSecond[0] + tripleSecond[1] + tripleSecond[2] != summe)
		{
			if(ptr==1 || ptr == 0)
				tripleSecond[0]--;
			if(ptr==2 || ptr == 3)
				tripleSecond[1]--;
			if(ptr==4 || ptr == 5)
				tripleSecond[2]--;

			ptr++;
			ptr%=6;

			if(tripleSecond[0] != p && tripleSecond[1] != p && tripleSecond[2] != p)
			{
				noWinner = true;
				break;
			}
		}
	}
	//printf("Second: %i %i %i | %s\n",tripleSecond[0],tripleSecond[1],tripleSecond[2], (noWinner)? "true" : "false");
	if( !noWinner && tripleSecond[0] + tripleSecond[1] + tripleSecond[2] == summe)
	{
		suprise--;
		return true;
	}
	else return false;
}

/******************************************************************/
/******************************************************************/

int main(int argc, char* argv[])
{
	std::ifstream infile;
	if(argc>1)
	{
		infile.open(argv[1]);
	}
	else { infile.open("input.in"); }

	int size = 0;
	infile >> size;

	if(size == 0)
	{
		printf("Keine Datei gefunden\n");
		return 0;
	}

	std::ofstream outfile;
	outfile.open("outfile.out",std::ios::out | std::ios::app );

	for(int i=0; i < size; i++)
	{
		int winners = 0;
		int numbers = 0;
		suprise=0;

		int p = 0;

		infile >> numbers;
		infile >> suprise;
		infile >> p;

		int currentVal = 0;
		for(int n=0; n < numbers; n++)
		{
			infile >> currentVal;

			if(currentVal != 0 || currentVal >= p)
			{
				if( checkTriple(currentVal,p) )
					winners++;
			}
		}
		outfile << "Case #"<< i+1 <<": " << winners << "\n";
	}

	return 0;
}