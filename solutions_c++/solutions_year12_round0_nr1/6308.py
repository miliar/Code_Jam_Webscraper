// googlerese.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "googlerese.h"
#include <iostream>
#include <fstream>
#include <string>
#include <map>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// The one and only application object

CWinApp theApp;

using namespace std;

map<char,char> googlereseMap;
void init()
{
	googlereseMap.insert(std::pair<char,char>('y','a'));
	googlereseMap.insert(std::pair<char,char>('n','b'));
	googlereseMap.insert(std::pair<char,char>('f','c'));
	googlereseMap.insert(std::pair<char,char>('i','d'));
	googlereseMap.insert(std::pair<char,char>('c','e'));
	googlereseMap.insert(std::pair<char,char>('w','f'));
	googlereseMap.insert(std::pair<char,char>('l','g'));
	googlereseMap.insert(std::pair<char,char>('b','h'));
	googlereseMap.insert(std::pair<char,char>('k','i'));
	googlereseMap.insert(std::pair<char,char>('u','j'));
	googlereseMap.insert(std::pair<char,char>('o','k'));
	googlereseMap.insert(std::pair<char,char>('m','l'));
	googlereseMap.insert(std::pair<char,char>('x','m'));
	googlereseMap.insert(std::pair<char,char>('s','n'));
	googlereseMap.insert(std::pair<char,char>('e','o'));
	googlereseMap.insert(std::pair<char,char>('v','p'));
	googlereseMap.insert(std::pair<char,char>('z','q'));
	googlereseMap.insert(std::pair<char,char>('p','r'));
	googlereseMap.insert(std::pair<char,char>('d','s'));
	googlereseMap.insert(std::pair<char,char>('r','t'));
	googlereseMap.insert(std::pair<char,char>('j','u'));
	googlereseMap.insert(std::pair<char,char>('g','v'));
	googlereseMap.insert(std::pair<char,char>('t','w'));
	googlereseMap.insert(std::pair<char,char>('h','x'));
	googlereseMap.insert(std::pair<char,char>('a','y'));
	googlereseMap.insert(std::pair<char,char>('q','z'));
}

int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
	int nRetCode = 0;

	HMODULE hModule = ::GetModuleHandle(NULL);

	if (hModule != NULL)
	{
		// initialize MFC and print and error on failure
		if (!AfxWinInit(hModule, NULL, ::GetCommandLine(), 0))
		{
			// TODO: change error code to suit your needs
			_tprintf(_T("Fatal Error: MFC initialization failed\n"));
			nRetCode = 1;
		}
		else
		{
			// TODO: code your application's behavior here.
			USES_CONVERSION;
			init();
			string line,googlerese;
			ifstream myfile (argv[1]);
			ofstream myOutFile("E:\\CodeJam\\output.txt");
			if (myfile.is_open())
			{
				while ( myfile.good() )
				{
					getline(myfile,line);
					int lines = atoi(line.c_str());
					int linecounter = 0;
					while(linecounter < lines)
					{
						getline(myfile,line);
						int len = line.length();
						int i = 0;
						char * newLine = new char[len];
						while(i < len)
						{
							char b = line.at(i);
							if(b != ' ')
							{
								map<char,char>::iterator aIter = googlereseMap.find(b);
								char dest  = aIter->second;
								newLine[i] = dest;
							}
							else
							{
								newLine[i] = ' ';
							}
							++i;
						}
						newLine[i] = '\0';
						
						CString a_csOUt(newLine);
						CString a_Line;
						string a_Line1;
						a_Line.Format(_T("Case #%d: %s\n"),(linecounter + 1),a_csOUt);
						a_Line1 = T2A(a_Line);
						myOutFile.write(a_Line1.c_str(),a_Line1.length());
						++linecounter;
					}
				}
				myfile.close();
			}
			if(myOutFile.is_open())
			{
				myOutFile.close();
			}
		}
	}
	else
	{
		// TODO: change error code to suit your needs
		_tprintf(_T("Fatal Error: GetModuleHandle failed\n"));
		nRetCode = 1;
	}

	return nRetCode;
}
