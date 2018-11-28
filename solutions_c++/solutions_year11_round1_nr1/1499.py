//////////////////
// chul-e		//
// CoconutLabs.	//
//////////////////


#include "stdafx.h"
#include <string>
#include <vector> 
#include <map>

using namespace std;

///���� �����
FILE*	fIN;
FILE*   fOUT;

///�Է� ����
int TEST; //�׽�Ʈ ����
 
long N;
int PD; //���� �·�
int PG; //��Ż �·�

///�Է� ���� ����
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
	 




		//������
		if(bPossible)
			fprintf(fOUT,"Case #%d: Possible\r\n",t);
		else
			fprintf(fOUT,"Case #%d: Broken\r\n",t);

	}


	fclose(fIN);
	fclose(fOUT);

	return 0;
}

