// TEST.cpp : définit le point d'entrée pour l'application console.
//

#include "stdafx.h"
#include <string>
#include <list>
#include <iostream>

#define maxL 15
#define maxD 5000

using namespace std;

void main()
{
    string basePath = "C:\\Users\\MAGALIE\\Downloads\\";
    string inFile = basePath + "A-small-attempt0.in";
    string outFile = basePath + "output.txt";

    freopen(inFile.c_str(),"r",stdin);
    freopen(outFile.c_str(),"w",stdout);

	int nLinePos,j,nLineLength,i,nFileLength;
	char szLine[4096];
	string strLetter;
	scanf("%d",&nFileLength);
	for(nLinePos=0; nLinePos<nFileLength; ++nLinePos) 
	{
		scanf("\n%[^\n]",szLine);
		nLineLength = strlen(szLine);
		printf("Case #%d: ", nLinePos+1);
		for(i=0; i<nLineLength; i++)
		{
			switch(szLine[i])
			{
				case 'a':
					szLine[i] = 'y';
				break;
				case 'b':
					szLine[i] = 'h';
				break;
				case 'c':
					szLine[i] = 'e';
				break;
				case 'd':
					szLine[i] = 's';
				break;
				case 'e':
					szLine[i] = 'o';
				break;
				case 'f':
					szLine[i] = 'c';
				break;
				case 'g':
					szLine[i] = 'v';
				break;
				case 'h':
					szLine[i] = 'x';
				break;
				case 'i':
					szLine[i] = 'd';
				break;
				case 'j':
					szLine[i] = 'u';
				break;
				case 'k':
					szLine[i] = 'i';
				break;
				case 'l':
					szLine[i] = 'g';
				break;
				case 'm':
					szLine[i] = 'l';
				break;
				case 'n':
					szLine[i] = 'b';
				break;
				case 'o':
					szLine[i] = 'k';
				break;
				case 'p':
					szLine[i] = 'r';
				break;
				case 'q':
					szLine[i] = 'z';
				break;
				case 'r':
					szLine[i] = 't';
				break;
				case 's':
					szLine[i] = 'n';
				break;
				case 't':
					szLine[i] = 'w';
				break;
				case 'u':
					szLine[i] = 'j';
				break;
				case 'v':
					szLine[i] = 'p';
				break;
				case 'w':
					szLine[i] = 'f';
				break;
				case 'x':
					szLine[i] = 'm';
				break;
				case 'y':
					szLine[i] = 'a';
				break;
				case 'z':
					szLine[i] = 'q';
				break;
			}
			printf("%c",szLine[i]);
		}
		printf("\n");
	}
}