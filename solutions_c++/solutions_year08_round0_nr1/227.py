// Jam2008.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "Jam2008.h"

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
	while(npos<nlen && lpBuf[npos] != 10) npos++;
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


int m_nCaseSum;
int m_nSearchSum;
char * m_nSearchNames[100];
int m_nSearchQ[100];
int m_nQuerysSum;

bool checkQuery(const char * const lpLine)
{	
	int nPos = -1;
	bool hasSpace = false;
	for(int i=0;i<m_nSearchSum;i++){
		if( strcmp(m_nSearchNames[i],lpLine)==0){
			if(m_nSearchQ[i]==1) 
				return false;
			nPos = i;
			m_nSearchQ[i] = 1;
		}
		if(m_nSearchQ[i]==0)
			hasSpace = true;
	}
	if(!hasSpace){
		ZeroMemory(m_nSearchQ ,sizeof(int) * 100);
		m_nSearchQ[nPos] = 1;
		return true;
	}
	return false;
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
	ZeroMemory(m_nSearchNames,sizeof(char * ) * 100);
	char * lpLine=NULL;
	ReadLine( lpLine,lpBuf,nPos,nLen);
	m_nCaseSum = atoi(lpLine);
	char  buffer[200];

	int nCS=0;
	char * lpDesMun=NULL;

	while(1){
		ZeroMemory(m_nSearchQ,sizeof(int) * 100);
		int nLineLen = ReadLine( lpLine,lpBuf,nPos,nLen);
		if( nLineLen == 0)
			break;
		m_nSearchSum = atoi(lpLine);
		for(int i=0;i<m_nSearchSum;i++){
			ReadLine( m_nSearchNames[i],lpBuf,nPos,nLen);
		}
		ReadLine( lpLine,lpBuf,nPos,nLen);
		m_nQuerysSum = atoi(lpLine);
		int sWitchNo=0;
		for(int i=0;i<m_nQuerysSum;i++){
			ReadLine( lpLine,lpBuf,nPos,nLen);
			if( checkQuery(lpLine))
				sWitchNo++;
		}
		nCS++;
		sprintf(buffer,"Case #%d: %d\n",nCS,sWitchNo);
		outFile.Write(buffer,strlen(buffer));
	}
	if(lpDesMun != NULL)
		delete [] lpDesMun;
	if(nCS!= m_nCaseSum)
		cout << "file is not illege:" << m_nCaseSum<<" VS " << nCS << endl;
	cout << "have deal with "<< m_nCaseSum <<" cases" << endl;
	delete [] lpLine;
	lpLine = NULL;
	delete [] lpBuf;
	inFile.Close();
	outFile.Close();
}
