#include <iostream.h>
#include <fstream.h>
#include <list.h>


int main(void)
{
	int iCases;
	int iEngines;
	int iSearches;
	int i,j,k;
	int iSwitches;
	int iCount[100];
	int iDone;
	int iCurrentEngine;
	int max;
	string sLine;
	list<string> sEngines;
	list<string> sSearches;
	list<string>::iterator iter;
	list<string>::iterator iterb;
	
	ifstream inFile;
	
	inFile.open("A-large.in");
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> iCases;

	
	for (i=0;i<iCases;i++)
	{
		iSwitches = 0;
		sEngines.clear();
		inFile >> iEngines;
		//cout << "numengines: " << iEngines << endl;
		getline(inFile,sLine);
		for (j=0;j<iEngines;j++)
		{
			getline(inFile,sLine);
			//cout << "engine # " << j+1 << " : " << sLine << endl;
			sEngines.push_back(sLine);
		}
/*
		j = 0;
		for (iter=sEngines.begin();iter!=sEngines.end();iter++)
		{
			j++;
			cout << "engine # " << j << " : " << *iter << endl;
		}
*/
		inFile >> iSearches;
		getline(inFile,sLine);
		//cout << "Numsearches: " << iSearches << endl;
		
		sSearches.clear();
		for (j=0;j<iSearches;j++)
		{
			getline(inFile,sLine);
			sSearches.push_back(sLine);
			//cout << "search # " << j+1 << " : " << sLine << endl;
		}
		iDone = 0;
		while ( iDone == 0 )
		{
			for (j=0;j<iEngines;j++)
			{
				iCount[j] = 0;
			}
			j = 0;
			for (iter=sEngines.begin();iter!=sEngines.end();iter++)
			{
				k = 1;
				for(iterb=sSearches.begin();iterb!=sSearches.end();iterb++)
				{
				//cout << "k: " << k << "j: " << j << "*iter: " << *iter << " *iterb: " << *iterb << endl;
					if ( *iterb == *iter )
					{
						iCount[j]=k;
						break;
					}
					k++;
				}
				j++;
			}
/*	
			for (k=0;k<iEngines;k++)
				cout << "iCount[" << k << "] : " << iCount[k] << endl;
			for(iterb=sSearches.begin();iterb!=sSearches.end();iterb++)
				cout << "*iterb: " << *iterb << endl;
*/


			max = 0;
			for (j=0;j<iEngines;j++)
			{
				if ( iCount[j] > max )
				{
					max = iCount[j];
					iCurrentEngine = j;
				}
				if (iCount[j] == 0)
				{
					iDone = 1;
				}
			}
			if ( iDone == 0 )
			{
				iSwitches++;
			}
			if ( max>0 )
			{
				for (j=0;j<max-1;j++)
				{
					sSearches.pop_front();
				}
			}
		}
			
		cout << "Case #" << i+1 << ": " << iSwitches << endl;
	}
		
	inFile.close();
	return 0;
}