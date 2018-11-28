#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>

#define LARGE

#ifdef LARGE 
char *sFileIn = "./B-large.in";
char *sFileOut = "./B-large.out";
#else
char *sFileIn = "./B-small-attempt0.in";
char *sFileOut = "./B-small-attempt0.out";
#endif

int g_temp[5];
char ctype[32];
int g_list[32];

typedef struct POINT
{
	int ih;
	int iw;
}POINT;

POINT g_point[32];

enum{NORTH=0, WEST=1, EAST=2, SOUTH=3, SINK=4};

typedef struct MAP
{
	int width;
	int height;

	int **ppData;
	int **ppRlt;
	char **ppMark;

	int numSink;

}MAP;

int **New2DimInt(int numx, int numy);
void Release2DimInt(int **pDim, int numx, int numy);

char **New2DimChar(int numx, int numy);
void Release2DimChar(char **pDim, int numx, int numy);


void CalculateDrain(MAP* pMap);
char GetDirectMark(int center, int north, int west, int east, int south, int& numSink, int idh, int idw);
void Track(MAP *pMap, int ih, int iw, int type);


int main(int argc, char *argv[])
{
	int i, j, k;

	//
	for(i=0; i<32; i++)
	{
		ctype[i] = 'a'+i;
	}

	//=======================================file io
	std::ifstream inFile;
	inFile.open(sFileIn);

	std::ofstream outFile;
	outFile.open(sFileOut);
	//==============================================

	//================================read map======
	int numMap;
	inFile>>numMap;

	MAP *pMap = new MAP[numMap];

	for(i=0; i<numMap; i++)
	{
		inFile>>pMap[i].height;
		inFile>>pMap[i].width;

		pMap[i].ppData = New2DimInt(pMap[i].width+2, pMap[i].height+2);
		pMap[i].ppMark = New2DimChar(pMap[i].width, pMap[i].height);
		pMap[i].ppRlt = New2DimInt(pMap[i].width, pMap[i].height);

		for(j=0; j<pMap[i].height; j++)
		{
			for(k=0; k<pMap[i].width; k++)
			{
				inFile>>pMap[i].ppData[j+1][k+1];

	//			printf("%d ", pMap[i].ppData[j+1][k+1]);
			}
	//		printf("\n");
		}

	//	printf("\n");

	}
	//=============================================

	for(i=0; i<numMap; i++)
	{
		CalculateDrain(&pMap[i]);
		//CalculateDrainEx(&pMap[i]);
	}


	char sOut[256];
	std::string strOut, strAdd;
	for(i=0; i<numMap; i++)
	{
		sprintf(sOut, "Case #%d:\n", i+1);
		outFile<<sOut;
		
		for(j=0; j<pMap[i].height; j++)
		{
			strOut = "";
			for(k=0; k<pMap[i].width; k++)
			{
				//printf("%d ", pMap[i].ppRlt[j][k]);
				sprintf(sOut, "%c ", pMap[i].ppMark[j][k]);

				strAdd = sOut; 

				strOut+=strAdd;
			}
			strOut+="\n";
			outFile<<strOut.c_str();
			//printf("\n");
		}

		printf("Case #%d:\n", i+1);
	}

	printf("finish\n");


	//=======================================file close
	inFile.close();
	outFile.close();

	//========================================release
	for(i=0; i<numMap; i++)
	{
		Release2DimInt(pMap[i].ppData, pMap[i].width+2, pMap[i].height+2);
		Release2DimChar(pMap[i].ppMark, pMap[i].width, pMap[i].height);
		Release2DimInt(pMap[i].ppRlt, pMap[i].width, pMap[i].height);
	}
	delete [] pMap;

	getchar();

	return 0;
}



/*
 * 
 */
void CalculateDrain(MAP* pMap)
{
	int i, j;
	int width = pMap->width;
	int height = pMap->height;

	int idw, idh;

	int numSink=0;
	for(i=1; i<height+1; i++)
	{
		idh = i-1;
		for(j=1; j<width+1; j++)
		{
			idw = j-1;
			pMap->ppMark[idh][idw] = GetDirectMark(pMap->ppData[i][j], 
				pMap->ppData[i-1][j], pMap->ppData[i][j-1], 
				pMap->ppData[i][j+1], pMap->ppData[i+1][j], numSink, idh, idw);

			//printf("%d ", pMap->ppMark[idh][idw]);
		}
		//printf("\n");
	}
	//printf("\n");

	//=======================================================================
	/*
	int type = 0;
	for(i=0; i<height; i++)
	{
		for(j=0; j<width; j++)
		{
			if(pMap->ppMark[i][j]==SINK)
			{
				Track(pMap, i, j, type);
				type++;
			}

		}
	}
	*/
	for(i=0; i<numSink; i++)
	{
		Track(pMap, g_point[i].ih, g_point[i].iw, i);

	}


	//======================================

	pMap->numSink = numSink;
	//pMap->numSink = type+1;


	//char index[26];
	
	//int next;
	
	int lpos=0;

	g_list[lpos] = pMap->ppRlt[0][0];


	bool bhave = false;
	int last=pMap->ppRlt[0][0];
	//int limit;
	for(i=0; i<height; i++)
	{
		for(j=0; j<width; j++)
		{
			if(last!=pMap->ppRlt[i][j])
			{
				//limit = lpos+1;
				bhave=false;
				for(int m=0; m<lpos+1; m++)
				{
					if(pMap->ppRlt[i][j]==g_list[m])
					{
						bhave = true;
						break;
					}
				}
				if(!bhave)
				{
					lpos++;
					g_list[lpos] = pMap->ppRlt[i][j];
					last=pMap->ppRlt[i][j];
				}

			}
				//index[typecount] = pMap->ppRlt[i][j];
		}
	}


	
	for(int k=0; k<pMap->numSink; k++)
	{
		for(i=0; i<height; i++)
		{
			for(j=0; j<width; j++)
			{
				if(g_list[k] == pMap->ppRlt[i][j])
				{
					pMap->ppMark[i][j]=ctype[k];

				}

			}
		}
	}
	

	//}


	//=======================================================================
}


/*
 *
 */
void Track(MAP *pMap, int ih, int iw, int type)
{
	pMap->ppRlt[ih][iw] = type;
	//top or north
	if(ih-1>=0)
	{
		if(pMap->ppMark[ih-1][iw]==SOUTH)
		{
			Track(pMap, ih-1, iw, type);
		}
	}
	
	//
	if(ih+1<pMap->height)
	{
		if(pMap->ppMark[ih+1][iw]==NORTH)
		{
			Track(pMap, ih+1, iw, type);
		}
	}
	//
	if(iw-1>=0)
	{
		if(pMap->ppMark[ih][iw-1]==EAST)
		{
			Track(pMap, ih, iw-1, type);
		}
	}

	//
	if(iw+1<pMap->width)
	{
		if(pMap->ppMark[ih][iw+1]==WEST)
		{
			Track(pMap, ih, iw+1, type);
		}
	}

}


/*
 *
 */
char GetDirectMark(int center, int north, int west, int east, int south, int& numSink, int idh, int idw)
{
	char rlt=0;

	g_temp[0] = center;
	g_temp[1] = north;
	g_temp[2] = west;
	g_temp[3] = east;
	g_temp[4] = south;

	int min = 20000;
	int index=0;
	for(int i=0; i<5; i++)
	{
		if(min>g_temp[i])
		{
			min = g_temp[i];
			index = i;
		}
	}

	if(index==0)
	{
		g_point[numSink].ih = idh;
		g_point[numSink].iw = idw;


		numSink++;
		rlt = SINK;
	}
	else
	{
		rlt = index-1;
	}
	

	return rlt;
}


int **New2DimInt(int numx, int numy)
{
	int **pDim2 = NULL;
	pDim2 = new int*[numy];
	for(int i=0; i<numy; i++)
	{
		pDim2[i] = new int[numx];
		//memset(pDim2[i], 0, numy*4);
		for(int j=0; j<numx; j++)
		{
			pDim2[i][j] = 20000;
		}
	}

	return pDim2;
}

void Release2DimInt(int **pDim, int numx, int numy)
{
	for(int i=0; i<numy; i++)
	{
		delete [] pDim[i];
	}

	delete [] pDim;
}

char **New2DimChar(int numx, int numy)
{
	char **pDim2 = NULL;
	pDim2 = new char*[numy];
	for(int i=0; i<numy; i++)
	{
		pDim2[i] = new char[numx];
		memset(pDim2[i], 0, numx);
	}

	return pDim2;
}

void Release2DimChar(char **pDim, int numx, int numy)
{
	for(int i=0; i<numy; i++)
	{
		delete [] pDim[i];
	}

	delete [] pDim;
}