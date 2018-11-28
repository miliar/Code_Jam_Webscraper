// SvUniverse.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdio.h"
#include <iostream> 
#include <fstream> 
#include <vector> 
#include <list> 
#include <algorithm> 
#include <string> 
using namespace std; 


int _tmain(int argc, _TCHAR* argv[])
{
	fstream file_op("arq.txt",ios::in);
	fstream file_Out("arqOut.txt",ios::out); 
	int Ncases; 
	vector<string> vcStr;  
	char ch[255]; 

	file_op >> Ncases; 
    

	for(int k =0 ; k < Ncases; k++)
	{
		int nEngines, nQueries; 
		int nSwicth =0;
		file_op >> nEngines; 
		vcStr.erase(vcStr.begin(),vcStr.end()); 
		string str; 
		
		getline(file_op,str);
		for(int i =0 ; i < nEngines; i++)
		{
			
			getline(file_op,str);
			vcStr.push_back(str); 
		}

		file_op >> nQueries; 
		getline(file_op,str); 
		
		vector<string> vecAux = vcStr; 
		for(int j =0 ; j < nQueries; j++)
		{
			getline(file_op,str);
			std::vector<string>::iterator it = std::find(vecAux.begin(), vecAux.end(), str);
			if(it != vecAux.end())
			{
				int pos = std::distance(vecAux.begin(),it);
				vecAux.erase(vecAux.begin()+pos); 
				if(vecAux.size() == 0)
				{
					nSwicth++;
					vecAux = vcStr; 
					std::vector<string>::iterator it = std::find(vecAux.begin(), vecAux.end(), str);
					pos = std::distance(vecAux.begin(),it);
					vecAux.erase(vecAux.begin()+pos); 
				}

			} 
			
		}

		cout << "Case #" << k+1 << ": " << nSwicth << endl; 
		file_Out << "Case #" << k+1 << ": " << nSwicth << endl; 

			


		

	}



	return 0;
}

