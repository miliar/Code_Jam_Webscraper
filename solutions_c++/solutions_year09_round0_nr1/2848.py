#include <iostream>
#include <iomanip>
#include <fstream>
#include <conio.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
using namespace std;

void main() 
{
	//Index Variables
	int i,j,k,l,m,n;
	int L, D, N;
	int bracket=0;

	int noOfMatches;
	int loopCounter;

	char DWords[5000][20];
	char caseWord[400];
	char caseWordArray[20][30];

	ifstream inFile;
	fstream outFile;

    inFile.open("A-large.in");
	outFile.open("output.in");
    if (!inFile) 
	{
        cout << "Unable to open file";
    }
	else
	{
		inFile >> L;
		inFile >> D;
		inFile >> N;

		for(i=0; i<D; i++)
		{
			inFile.getline(DWords[i], 20);
			if(DWords[i][0]=='\0')
				i--;
		}
		
		for(i=1; i<=N; i++)
		{
			//printf("%d\n",i);			
			inFile.getline(caseWord, 400);
			//printf("%s\n", caseWord);
			
			m=0;
			n=0;
			bracket=0;

			for(j=0; j<strlen(caseWord);j++)
			{
				
				if(caseWord[j]=='(')
				{
					bracket=1;
					continue;
				}
				
				else if(caseWord[j]==')')
				{
					bracket=0;
					caseWordArray[m][n]='\0';
					m++;
					n=0;
					continue;
				}
				else
				{
					caseWordArray[m][n]=caseWord[j];
					n++;	
					if(caseWord[j+1]=='\0' || caseWord[j+1]=='(' || bracket==0)
					{
						caseWordArray[m][n]='\0';
						m++;
						n=0;
					}
					
				}
			}
			
			/*
			for(j=0;j<m;j++)
				printf("%s....\n", caseWordArray[j]);
			*/

			noOfMatches=0;

			for(j=0; j<D; j++)
			{
				
				loopCounter=0;
				k=0;
				l=0;
				
				if(strlen(DWords[j])!=m)
				{
					//printf("%d\n",j);
					continue;
				}

				while(loopCounter<strlen(DWords[j]))
				{
					if(caseWordArray[k][l]==DWords[j][loopCounter])
					{
						k++;
						loopCounter++;
						l=0;
						continue;
					}
					else
					{
						if(caseWordArray[k][l]=='\0')
							break;						
						l++;	
					}
				}
				if(loopCounter==strlen(DWords[j]))
					noOfMatches++;
			}
			outFile << "Case #" << i << ": " << noOfMatches << "\n";
			//printf("Case #%d : %d\n", i, noOfMatches);
		}
	}

	inFile.close();
	outFile.close();
	
    getch();
}