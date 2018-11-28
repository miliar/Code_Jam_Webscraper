// saveuniverse.cpp : Defines the entry point for the console application.
//

#include<vector>
#include<afx.h>
#include<algorithm>
#include<iostream>
#include<fstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int N = 0;
	char nstr[101];
	
	//*********************** File Operations **************************//
	fstream file_in("e:\\A-large.in",ios::in);
	fstream file_out("e:\\A-large.out",ios::out);
	if (!file_in.is_open()) ASSERT(false); 
	
	file_in.getline(nstr,101);	
	N = atoi(nstr);	

	for( int nCase = 0; nCase < N; nCase++)
	{
		int S = 0;	
		string cstr;
		std::vector<CString> engineNames;
		std::vector<int> search_engines;
		std::vector< CString >::iterator location;
		engineNames.clear();
		search_engines.clear();
		
		
		file_in.getline(nstr,101);
		S = atoi(nstr);		

		for( int nEngines = 0; nEngines < S; nEngines++)
		{
			file_in.getline(nstr,101);
			cstr = nstr;			
			CString s(cstr.c_str());	
			
			engineNames.push_back(s);  //assign search engine names 
			search_engines.push_back(1); //default set to 1
		}
		int nSwitch = 0;
		int nCount = 0;
		int Q = 0;
		
		file_in.getline(nstr,101);
		Q = atoi(nstr);	

		for( int nQuery = 0; nQuery < Q; nQuery++)
		{
			file_in.getline(nstr,101);
			cstr = nstr;			
			CString s(cstr.c_str());
			
			location = std::find(engineNames.begin(),engineNames.end(),s);
			if(location != engineNames.end())
			{
				_w64 int n = location - engineNames.begin();
				if(search_engines[n] == 1 && nCount+1 < S)
				{
					search_engines[n] = 0;
					nCount++;
				}
				else if (search_engines[n] == 1 && nCount+1 == S)
				{
					nSwitch++;
					//reset the vector
					for( int nEngines = 0; nEngines < S; nEngines++)
						search_engines[nEngines] = 1;
					search_engines[n] = 0;
					nCount = 1;
				}
				else 
				{ 
					//don't do any thing 
				}
			} // if location not found
			//else
				 //do nothing 
		} // for number of queries

		file_out << "Case #"<< nCase+1<< ": "<< nSwitch<< endl;
	} // for each case	

	file_in.close();
	file_out.close();
	return 0;
}

