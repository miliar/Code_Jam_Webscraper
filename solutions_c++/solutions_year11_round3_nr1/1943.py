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
int R;
int C;

///입력 변수 범위
#define N_MAX 1000
#define N_MIN 0
#define M_MAX 1000
#define M_MIN 0

vector<int> intVec;
map<int, int> intMap;

#define WHITE 0
#define BLUE 1
#define RED  2

int pic[50][50];
char OPic[50][50];


int _tmain(int argc, _TCHAR* argv[])
{
	fIN = fopen("in.txt","rb");
	fOUT = fopen("out.txt","w");



	fscanf(fIN, "%d", &TEST);


	for(int t = 1; t <= TEST; t++)
	{

		fscanf(fIN, "%d", &R);
		fscanf(fIN, "%d", &C);

		for(int i = 0; i < R ; i++)
		{
			char buf[500];
			fscanf(fIN, "%s", &buf);
			for(int j = 0; j < C; j++)
			{ 
				if(buf[j] == '.')
				{
					pic[i][j] = WHITE;
				}
				else
				{
					pic[i][j] = BLUE;
				}



			} 
		}
		bool bEnable = true;

		for(int i = 0; i < R ; i++)
		{
			
			for(int j = 0; j < C; j++)
			{
				if(pic[i][j]  == BLUE)
				{
					if( j+1< C)
					{
						if(pic[i][j+1] == BLUE)
						{ 
							j++;
						}
						else
						{
							bEnable = false;
							break;
						}
					}
					else
					{
						bEnable = false;
						break;
					}

				}  
			}
			if(!bEnable)
				break;

		} 
		bool bAllEnable = false;
		if(bEnable)
		{
			bAllEnable = true;

			for(int j = 0; j < C; j++)
			{
				for(int i = 0; i < R ; i++)
				{
					if(pic[i][j]  == BLUE)
					{
						if( i+1< R)
						{
							if(pic[i+1][j] == BLUE)
							{
								i++;
							}
							else
							{
								bAllEnable = false;
								break;
							}
						}
						else
						{
							bAllEnable = false;
							break;
						}

					}  
				}
				if(!bAllEnable)
					break;
			}

		}


		for(int i = 0; i < R ; i++)
		{
			for(int j = 0; j < C; j++){
				OPic[i][j] = '.';
			}
		}


			//
			if(!bAllEnable)
			{
			fprintf(fOUT,"Case #%d: \r\n",t);
			fprintf(fOUT,"Impossible \r\n",t);
			}
			else 
			{
				 //결과출력
				fprintf(fOUT,"Case #%d: \r\n",t);
				for(int i = 0; i < R ; i++)
				{
					for(int j = 0; j < C; j++)
					{
						if(pic[i][j]  == BLUE)
						{
							OPic[i][j] = '/';
						 	OPic[i][j+1] = '\\' ;
						 	OPic[i+1][j] = '\\' ;
						 	OPic[i+1][j+1] = '/';
							
							pic[i][j] = WHITE;
						 	pic[i][j+1] = WHITE ;
						 	pic[i+1][j] = WHITE ;
						 	pic[i+1][j+1] = WHITE;

						}
					}
				}

				for(int i = 0; i < R ; i++)
				{
					for(int j = 0; j < C; j++){
						fprintf(fOUT,"%c",OPic[i][j]);
					}
					fprintf(fOUT,"\r\n",t);
				}

			}





	

	}


	fclose(fIN);
	fclose(fOUT);

	return 0;
}

