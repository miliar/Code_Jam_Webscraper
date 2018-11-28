// Solution to Problem A

#include <stdio.h>
#include <fstream>
#include <string.h>
#include <iostream>

using namespace std;

int nN;
int nS;
int nQ = 1;
char ** ptrS = NULL;
unsigned char * ptrMarkers = NULL;
int nSwitches = 0;
char Query[100];
int nSum;

char * strInputFileName;


ofstream OutputFile("./Output.txt");
FILE * InputFile;

int parsecmdline(int c, char* v[]);
void ReadInputFile(void);
void Search(void);
 
int main(int argc, char* argv[])
{
	if(parsecmdline(argc, argv)<0)
		exit(1);
	
	ReadInputFile();

	return 0;
}

int parsecmdline(int c, char* v[])
{
	switch(c)
	{
	case 2:		
		strInputFileName = v[1];
		break;
	default:
		cout << "Usage format:" << endl;
		cout << "InputFileName" << endl;
		return -1;
	}
	return 1;
}


void ReadInputFile()
{
	int i, j, k;
	
	InputFile = fopen(strInputFileName, "r");
	if(!InputFile)
	{
		cout<<"Can't open file: "<<InputFile<<endl;
		exit(1);
	}
	
	fscanf(InputFile,"%d",&nN);
//	cout<<"nN = "<<nN<<endl;
	
	for(k = 0; k < nN; k++)
	{

		fscanf(InputFile,"%d",&nS);
//		cout<<"nS = "<<nS<<endl;

		ptrS = new char * [nS];
		ptrMarkers = new unsigned char [nS];
		nSum = nS;

	

	char ch;

	for (i = 0; i < nS; i++)
	{
	
		while(1)
		{				
		ch = fgetc(InputFile);
		if(isalpha(ch)||isdigit(ch))
		{
		ungetc(ch,InputFile);
		break;
		}	
		}	
		ptrS[i] = new char [100+1];
		//Initialize the markers
		ptrMarkers[i] = 1;

		fgets(ptrS[i], 101, InputFile);

	}
/*
	for (i = 0; i < nS; i++)
	{
			cout<<"Search Engines = "<<i<< ptrS[i]<<endl;
	}
*/
	fscanf(InputFile,"%d",&nQ);
//	cout<<"nQ = "<<nQ<<endl;

	for (i = 0; i < nQ; i++)
	{

	while(1)
	{				
		ch = fgetc(InputFile);
		if(isalpha(ch)||isdigit(ch))
		{
		ungetc(ch,InputFile);
		break;
		}	
	}	

		fgets(Query, 101, InputFile);
		Search();
	//	cout<<"Query = "<<Query<<endl;

	}

	cout<<"Case #"<<k+1<<": "<<nSwitches<<endl;
	OutputFile<<"Case #"<<k+1<<": "<<nSwitches<<endl;
	nSwitches = 0;
	//free the allocated memory
	
	for (int i = 0; i < nS; i++)
	{
		delete ptrS[i];
	}
	delete ptrS;
	delete ptrMarkers;
	
	}//k loop

	
//	InputFile.close();
fclose(InputFile);
	OutputFile.close();
}


void Search()
{
	for (int i = 0; i < nS; i++)
	{
		if( strcmp(ptrS[i], Query) == 0)
		{
			if(ptrMarkers[i])
			{
				nSum = nSum - 1;
				if(nSum == 0)
				{
					nSwitches = nSwitches + 1;
					//reinitialize the markers
					for (int k = 0; k < nS; k++)
					{
						ptrMarkers[k] = 1;
					}
					nSum = nS - 1;

				}
				ptrMarkers[i] = 0;								
			}
			break;
		}
	}
		
}

