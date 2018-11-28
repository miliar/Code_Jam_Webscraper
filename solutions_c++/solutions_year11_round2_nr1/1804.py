//////////////////
// chul-e		//
// CoconutLabs.	//
//////////////////


#include "stdafx.h"
#include <string>
#include <vector> 
#include <map>
#include <algorithm>

using namespace std;

///파일 입출력
FILE*	fIN;
FILE*   fOUT;

///입력 변수
int TEST; //테스트 개수
int M;
int N;

///입력 변수 범위
#define N_MAX 100
#define N_MIN 3 

#define WIN  100
#define LOOSE  10
#define NO  -10


 

int _tmain(int argc, _TCHAR* argv[])
{
	fIN = fopen("in.txt","rb");
	fOUT = fopen("out.txt","w");
	
 
	 
	fscanf(fIN, "%d", &TEST);


	for(int t = 1; t <= TEST; t++)
	{
	
		fscanf(fIN, "%d", &N);


		int teamScore[100][100];
		int RPI[100];


		
		for(int i = 0; i< N; i++)
		{
			char buf[10000];
			fscanf(fIN, "%s", &buf);

			for(int j = 0; j < N; j++)
			{
				if(buf[j] == '.')
				{
					teamScore[i][j] = NO; 

				}
				else if(buf[j] == '1')
				{
					 teamScore[i][j] = WIN;
				}
				else if(buf[j] == '0')
				{
					 teamScore[i][j] = LOOSE;
				}
				 
			} 

		}

		double WP[100];
		double AgainstWP[100][100];
		double OWP[100];
		double AgainstOWP[100][100];
		double OOWP[100];
		for(int i = 0; i < N; i++)
		{
			int win = count(teamScore[i], teamScore[i]+N,WIN );
			 int loose = count(teamScore[i], teamScore[i]+N,LOOSE );
					
			 WP[i] = (double)win/(double)( win + loose);

 
			  
			 for(int j = 0; j < N ; j++)
			 {
			     int win = count(teamScore[j], teamScore[j]+N,WIN );
				 int loose = count(teamScore[j], teamScore[j]+N,LOOSE );

				 if(teamScore[j][i] == WIN)
				  win--;
				 if(teamScore[j][i] == LOOSE)
				  loose--;

				  AgainstWP[i][j] = (double)win/(double)( win + loose);
			 }
			  
		}

	    for(int i = 0; i < N; i++)
		{
			int nogame = count(teamScore[i], teamScore[i]+N,NO );
		 
			double sum = 0;
			for(int j = 0; j < N; j++)
			{
				if(i!=j)
				{
				if(teamScore[i][j] != NO)
				{
					sum = sum + AgainstWP[i][j]; 
				}
				}

			}
			
				OWP[i] =  (double)sum / (double)(N - nogame); 

			 
			  
		}

	    for(int i = 0; i < N; i++)
		{
			int nogame = count(teamScore[i], teamScore[i]+N,NO );
		 
			double sum = 0;
			for(int j = 0; j < N; j++)
			{
				if(teamScore[i][j] != NO)
				{
					sum = sum + OWP[j]; 
				}

			}
			
				OOWP[i] =  (double)sum / (double)(N - nogame); 
			  
		}

				//결과출력
		fprintf(fOUT,"Case #%d: \r\n",t);

			    for(int i = 0; i < N; i++)
				{
				
					double RPI = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
				
								//결과출력
				fprintf(fOUT,"%f \r\n",RPI);


				}


		


	}


	fclose(fIN);
	fclose(fOUT);

	return 0;
}

