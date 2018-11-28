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
int m_nNA;
int m_nNB;
int m_nT;
int m_tripNA[100][3];
int m_tripNB[100][3];

void checkTrain()
{	
	int nA=m_nNA;
	int nB=m_nNB;
	for(int i=0; i<m_nNB;i++){
		int nNext = -1; 
		int nNextPoint=50000;
		for(int j=0; j<m_nNA; j++){
			if(m_tripNA[j][0]==0 && 
				m_tripNA[j][1] < nNextPoint &&
				m_tripNA[j][1] >= m_tripNB[i][2]){
					nNext = j;
					nNextPoint = m_tripNA[j][1];
			}
		}
		if(nNext>=0){
			nA--;
			m_tripNA[nNext][0]=1;
		}
	}

	for(int i=0; i<m_nNA;i++){
		int nNext = -1; 
		int nNextPoint=50000;
		for(int j=0; j<m_nNB; j++){
			if(m_tripNB[j][0]==0 && 
				m_tripNB[j][1] < nNextPoint &&
				m_tripNB[j][1] >= m_tripNA[i][2]){
					nNext = j;
					nNextPoint = m_tripNB[j][1];
			}
		}
		if(nNext>=0){
			nB--;
			m_tripNB[nNext][0]=1;
		}
	}

	m_nNB=nB;
	m_nNA=nA;
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
	m_nCaseSum = atoi(lpLine);
	char  buffer[200];
	char * lpWord = NULL;
	int nCS=0;

	while(1){
		
		int nLineLen = ReadLine( lpLine,lpBuf,nPos,nLen);
		if( nLineLen == 0)
			break;
		m_nT = atoi(lpLine);
		int nl = ReadLine( lpLine,lpBuf,nPos,nLen);
		int np=0;
		ReadWord(lpWord,lpLine,np,nl);
		m_nNA = atoi(lpWord);
		ReadWord(lpWord,lpLine,np,nl);
		m_nNB = atoi(lpWord);
		ZeroMemory(m_tripNA,sizeof(int) * 100 * 3);
		ZeroMemory(m_tripNB,sizeof(int) * 100 * 3);

		for(int i=0;i<m_nNA;i++){
			np=0;
			nl = ReadLine(lpLine,lpBuf,nPos,nLen);
			ReadWord(lpWord,lpLine,np,nl,':');
			int nH = atoi(lpWord);
			np++;
			ReadWord(lpWord,lpLine,np,nl);
			int nM = atoi(lpWord);
			m_tripNA[i][1] = nH*60+nM;
			ReadWord(lpWord,lpLine,np,nl,':');
			nH = atoi(lpWord);
			np++;
			ReadWord(lpWord,lpLine,np,nl);
			nM = atoi(lpWord);
			m_tripNA[i][2] = nH*60+nM+m_nT;
		}

		for(int i=0;i<m_nNB;i++){
			np=0;
			nl = ReadLine(lpLine,lpBuf,nPos,nLen);
			ReadWord(lpWord,lpLine,np,nl,':');
			int nH = atoi(lpWord);
			np++;
			ReadWord(lpWord,lpLine,np,nl);
			int nM = atoi(lpWord);
			m_tripNB[i][1] = nH*60+nM;
			ReadWord(lpWord,lpLine,np,nl,':');
			nH = atoi(lpWord);
			np++;
			ReadWord(lpWord,lpLine,np,nl);
			nM = atoi(lpWord);
			m_tripNB[i][2] = nH*60+nM+m_nT;
		}
		checkTrain();
		nCS++;
		sprintf(buffer,"Case #%d: %d %d\n",nCS, m_nNA,m_nNB);
		outFile.Write(buffer,strlen(buffer));
	}

	if(nCS!= m_nCaseSum)
		cout << "file is not illege:" << m_nCaseSum<<" VS " << nCS << endl;
	cout << "have deal with "<< m_nCaseSum <<" cases" << endl;
	delete [] lpLine;
	lpLine = NULL;
	delete [] lpBuf;
	delete [] lpWord;
	lpWord = NULL;
	inFile.Close();
	outFile.Close();
}
