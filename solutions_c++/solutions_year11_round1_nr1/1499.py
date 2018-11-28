//////////////////
// chul-e		//
// CoconutLabs.	//
//////////////////


#include "stdafx.h"
#include <string>
#include <vector> 
#include <map>

using namespace std;

///파일 입출력
FILE*	fIN;
FILE*   fOUT;

///입력 변수
int TEST; //테스트 개수
 
long N;
int PD; //오늘 승률
int PG; //토탈 승률

///입력 변수 범위
#define N_MAX 1000
#define N_MIN 0
#define M_MAX 1000
#define M_MIN 0


int _tmain(int argc, _TCHAR* argv[])
{
	fIN = fopen("in.txt","rb");
	fOUT = fopen("out.txt","w");
	
 
	 
	fscanf(fIN, "%d", &TEST);


	for(int t = 1; t <= TEST; t++)
	{
	 	fscanf(fIN, "%d", &N);
	 	fscanf(fIN, "%d", &PD);
		fscanf(fIN, "%d", &PG);


		bool bPossible = false;

		if(PG == 100)
		{
			if(PD != 100)
			{
				bPossible = false;
			}
			else 
			{
				bPossible = true;
			}


		}
		else if(PG == 0)
		{
			if(PD == 0)
				bPossible = true;
			else
				bPossible = false;

		} 
		else
		{


			for(int i = 1; i <= N; i++)
			{

				int x = i * PD;

				if((x % 100) == 0)
				{ 
					bPossible = true;
					break;
				}

			}
		}
	 




		//결과출력
		if(bPossible)
			fprintf(fOUT,"Case #%d: Possible\r\n",t);
		else
			fprintf(fOUT,"Case #%d: Broken\r\n",t);

	}


	fclose(fIN);
	fclose(fOUT);

	return 0;
}

