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

long long atolong(char * lpV,int n)
{
	long long nRes=0;
	for(int i=0;i<n;i++)
		nRes = nRes*10 + (lpV[i]-'0');
	return nRes;
}

void RunAlgorithm(LPCTSTR inFileName, LPCTSTR outFileName)
{
	//cout<< inFileName <<endl;
	//cout<< outFileName <<endl;
	CFile inFile,outFile;
	if(! inFile.Open(inFileName,CFile::modeRead|CFile::shareDenyNone)){
		cout << "could not open the file :" << inFileName << endl;
		return ;
	}
	if(! outFile.Open(outFileName,CFile::modeCreate|CFile::modeReadWrite)){
		cout << "could not open the file :" << outFileName << endl;
		inFile.Close();
		return ;
	}
	int nLen = inFile.GetLength();
	char * lpBuf = new char[nLen+1];
	inFile.Read(lpBuf,nLen);
	lpBuf[nLen] = 0;
	int nPos=0;

	char * lpLine=NULL;
	ReadLine( lpLine,lpBuf,nPos,nLen);
	int m_nCaseSum = atoi(lpLine);
	char  buffer[200];
	int nCS=0;

	while(1){
		
		int nLineLen = ReadLine( lpLine,lpBuf,nPos,nLen);
		if( nLineLen == 0)
			break;
		int nP=0;
		int nAS = 0;
		for(int i=0;i< int(pow(3.f,nLineLen-1)+0.1f);i++){
			long long nNumber=0;
			int nP=0;
			int nTemp=i;
			int nPP=0;
			int nPreOpt=1;
			while(nP<nLineLen-1){
				int nOpt= nTemp % 3;
				nTemp = nTemp / 3;
				nP++;
				if(nOpt>0){
					long long lTemp = atolong(lpLine+nPP,nP-nPP);
					nPP=nP;
					if(nPreOpt == 1)
						nNumber += lTemp;
					else
						nNumber -= lTemp;
					nPreOpt = nOpt;
				}
			}
			long long lTemp = atolong(lpLine+nPP,nLineLen-nPP);
			if(nPreOpt == 1)
				nNumber += lTemp;
			else
				nNumber -= lTemp;

			if(nNumber % 2==0 || nNumber % 3==0 || nNumber % 5==0 || nNumber % 7==0)
				nAS ++;

		}

		nCS++;
		sprintf(buffer,"Case #%d: %d\n",nCS,nAS );
		outFile.Write(buffer,strlen(buffer));
	}

	if(nCS!= m_nCaseSum)
		cout << "file is not illege:" << m_nCaseSum<<" VS " << nCS << endl;
	cout << "have deal with "<< m_nCaseSum <<" cases" << endl;
	delete [] lpLine;
	lpLine = NULL;
	delete [] lpBuf;
	inFile.Close();
	outFile.Close();
}


