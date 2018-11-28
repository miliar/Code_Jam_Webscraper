// AlienLanguage.cpp : Defines the entry point for the console application.
//


#include <stdafx.h>
#include<vector>
#include<afx.h>
#include<algorithm>
#include<iostream>
#include<fstream>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	int N = 0;
	int D = 0;
	int L = 0;
	char nstr[6001];
	
	//*********************** File Operations **************************//
	fstream file_in("c:\\abirami\\A-large.in",ios::in);
	fstream file_out("c:\\abirami\\A-large.out",ios::out);
	if (!file_in.is_open()) ASSERT(false); 	


	file_in >> L >> D >> N ;
	file_in.getline(nstr,6001);
	string cstr;
	std::vector<CString> Dictionary;
	for(int nWords = 0; nWords < D; nWords++)
	{
		file_in.getline(nstr,6001);
		cstr = nstr;			
		CString s(cstr.c_str());			
		Dictionary.push_back(s);
	}

	for( int nCase = 0; nCase < N; nCase++)
	{	
		file_in.getline(nstr,6001);
		cstr = nstr;			
		CString s(cstr.c_str());
		int nPatternLen = s.GetLength();
		int nPattern = 0;
		TCHAR strL;
		std::vector<std::vector<CString>> vctWords;

		
		while(nPattern < nPatternLen)
		{
			strL = s.GetAt(nPattern++);
			std::vector<CString> vctLetters;
			if(('a'<=strL && strL<= 'z') || ('A'<=strL && strL<= 'Z'))
			{
				vctLetters.push_back(strL);
				vctWords.push_back(vctLetters);
			}
			else if ( strL == '(')
			{
				while((strL = s.GetAt(nPattern++)) != ')')
				{
					vctLetters.push_back(strL);
				}
				vctWords.push_back(vctLetters);
			}
		}	
	

		int nCount = 0;
		for(int nDictWords = 0; nDictWords < D; nDictWords++)
		{
			bool bMatch = false;			
			CString s = Dictionary[nDictWords];
			for(int nLetters = 0; nLetters < L; nLetters++)
			{
				TCHAR l = s.GetAt(nLetters);
				std::vector< CString >::iterator location;
				location = std::find(vctWords[nLetters].begin(),vctWords[nLetters].end(),l);			
				if(location != vctWords[nLetters].end())
				{
					bMatch = true;
				}
				else
				{
					bMatch = false;
					break;
				}
			}
			if(bMatch) nCount++;
		}			

		file_out << "Case #"<< nCase+1<< ": "<< nCount<< endl;
					
	} // for each case	

	file_in.close();
	file_out.close();
	return 0;
}

