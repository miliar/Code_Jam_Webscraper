// Jam2008.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "Jam2008.h"
#include <math.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include<string>
#include<cstdio>
#include<map>

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
//qsort(v1,nF,sizeof(int),compare);

long long atolong(char * lpV,int n)
{
	long long nRes=0;
	for(int i=0;i<n;i++)
		nRes = nRes*10 + (lpV[i]-'0');
	return nRes;
}

int M;
bool node[6000];
bool change[6000];
bool node2[10000];
bool leaf[10000];

int MIN(int a,int b){
	return a<b?a:b;
}

int fchange(int n,const bool v){
	if (leaf[n]==v) return 0;
	if (n >= (M-1)/2 ) return M+1;
	if ( ( (leaf[2*n+1] && leaf[2*n+2]) != (leaf[2*n+1] || leaf[2*n+2] ) ) && change[n] ) 
		return 1;

	int nMin1 = M+1,nMin2;
	if (change[n]){
		if(v)
			nMin1 = MIN(fchange(2*n+1,true) , fchange(2*n+2,true)) +1;
		else
			nMin1 = MIN(fchange(2*n+1,false) , fchange(2*n+2,false) )+1;
	}
	if(node[n] ){
		if(v)
			nMin2 = fchange(2*n+1,true) + fchange(2*n+2,true);
		else
			nMin2 = MIN(fchange(2*n+1,false) , fchange(2*n+2,false) );
	}else{
		if(v) 
			nMin2 = MIN(fchange(2*n+1,true) , fchange(2*n+2,true) );
		else 
			nMin2 =  fchange(2*n+1,false) + fchange(2*n+2,false);
	}
	return MIN(nMin2,nMin1);
}

void RunAlgorithm(LPCTSTR inFileName, LPCTSTR outFileName)
{

	ifstream inf;
	inf.open(inFileName,ios_base::in);
	ofstream outf;
	outf.open(outFileName,ios_base::out);

	int nCase;
	inf >> nCase;
	for( int CC = 1; CC <= nCase; CC ++ ){
		int  V, t;
		inf >> M;
		inf >> V;
		bool bV = V==1;
		for(int i=0;i<(M-1)/2;i++){
			inf >> t;
			node[i] = t==1;
			inf >> t;
			change[i] = t==1;
		}
		int nBL = (M-1)/2;
		for(int i=0;i<(M+1)/2;i++){
			inf >> t;
			leaf[nBL+i] = t==1;
		}
		int nMinC = 0;
		for(int i = nBL-1;i>=0;i--){
			leaf[i] = node[i] ? leaf[2*i+1] && leaf[2*i+2] : leaf[2*i+1] || leaf[2*i+2];
		}
		int nMin = fchange(0,bV);

		if(nMin> M-1){
			outf << "Case #" << CC << ": IMPOSSIBLE" << endl;
			cout << "Case #" << CC << ": IMPOSSIBLE" << endl;
		}else{
			outf << "Case #" << CC << ": " << nMin << endl;
			cout << "Case #" << CC << ": " << nMin << endl;
		}
	}

	inf.close();
	outf.close();
	cout << "have deal with "<< nCase <<" cases" << endl;
}