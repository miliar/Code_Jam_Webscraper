// Jam2008.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "Jam2008.h"
#include <math.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>


#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// The one and only application object

CWinApp theApp;

using namespace std;

void RunAlgorithm(LPCTSTR inFileName, LPCTSTR outFileName);

int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
	int nRetCode = 0;

	// initialize MFC and print and error on failure
	if (!AfxWinInit(::GetModuleHandle(NULL), NULL, ::GetCommandLine(), 0))
	{
		// TODO: change error code to suit your needs
		cerr << _T("Fatal Error: MFC initialization failed") << endl;
		nRetCode = 1;
	}

	if(argc<2){
		cout<< "lack parameter!" <<endl;
		return 0;
	}
	if(argc>2)
		RunAlgorithm(argv[1], argv[2]);
	else
		RunAlgorithm(argv[1], "outputfile.out");

	return nRetCode;
}


int ReadLine( char * &lpLine, const char * const lpBuf,int &npos, int nlen)
{
	while(npos<nlen && (lpBuf[npos]==13 || lpBuf[npos]==10)) npos++;
	int i=npos;
	while(npos<nlen && (lpBuf[npos] != 10 && lpBuf[npos] != 13)) npos++;
	if(lpLine != NULL)
		delete [] lpLine;
	lpLine = new char[npos-i+1];

	if(npos>i)
		CopyMemory(lpLine,lpBuf+i,npos-i);
	lpLine[npos-i] = 0;
	return npos-i;
}

int ReadWord( char * &lpWord, const char * const lpBuf,int &npos, int nlen,const char cSplit=' ')
{
	while(npos<nlen && lpBuf[npos]== cSplit) npos++;
	int i=npos;
	while(npos<nlen && lpBuf[npos] != cSplit) npos++;
	if(lpWord != NULL)
		delete [] lpWord;
	lpWord = new char[npos-i+1];

	if(npos>i)
		CopyMemory(lpWord,lpBuf+i,npos-i);
	lpWord[npos-i] = 0;
	return npos-i;
}


int compare( const void * arg1, const void * arg2 )
{
   /* Compare all of both strings: */
	if( *(int*)arg1 > *(int*)arg2) return 1;
	if(*(int*)arg1 == *(int*)arg2)
	   return 0;
	return -1;
}


void RunAlgorithm(LPCTSTR inFileName, LPCTSTR outFileName)
{
	ifstream inf;
	inf.open(inFileName,ios_base::in);
	ofstream outf;
	outf.open(outFileName,ios_base::out);

	int T;
	inf >> T;
	for (int c = 1; c <= T; c++) {
		int P,K,L;
		inf >> P;
		inf >> K;
		inf >> L;
		int * nKP = new int[L+1];
		for(int i=0;i<L;i++)
			inf >> nKP[i];
		qsort(nKP,L,sizeof(int),compare);
		long long ans=0;
		int i=L-1;
		int nPC=1;
		while(i >=0 ){

			ASSERT(nPC <= P);
			for(int j=0;j<K && i>=0;j++){
				ans += ( nPC * nKP[i]);
				i--;
			}
			nPC++;
		}

		outf<< "Case #"<<c<<": "<< ans<< endl;
		delete [] nKP;
	}
	inf.close();
	outf.close();

	cout << "have deal with "<< T <<" cases" << endl;
}


