// Jam2008.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "Jam2008.h"
#include <math.h>

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
const double pi=3.1415926535897932384626;
double f, R, t, r ,g;

double calcProbability()
{	
	double s = pi*R*R;
	r = r+f;
	g = g-2*f;
	if(g<=0.f) return 1.0;
	double R2 = R-t-f;
/*	
	double sPro1 = 1 - g*g / ((g+2*r) * (g+2*r));
	double t1 = R2*R2*sPro1;
	double t2 = R*R-R2*R2;
	double t3 =R*R;
	return (t1+t2 ) / t3;
*/
	double sSub = g*g;
	double s2=0.0f;
	
	double dist = R2 * R2;
	double dx = 0.f;
	double dy = 0.f;
	
	while(dy+r < R2){
		dx = 0.f;
		double xlen = sqrt(R2*R2-(dy+r)*(dy+r));
		while( dx+r < xlen){
			if( (dx + r + g) * (dx + r + g) + (dy + r + g) * ( dy + r + g ) <= dist) {
				s2 += sSub;
			}else if(dx + r + g <= xlen){
				if((dx + r) * (dx + r ) + (dy + r + g) * ( dy + r + g ) <= dist){
					//Case 1:
					double st = acos((dx+r+g)/R2);
					double st2 = asin((dy+r+g)/R2);
					double dirtSt = st2 - st;
					ASSERT(dirtSt>0);
					double sanxing = dirtSt *  R2 * R2 / 2;
					double sanjiaoxing1 = (dx+r+g) * (dy+r+g - R2*sin(st)) / 2;
					double sanjiaoxing2 = (dy+r+g) * (dx+r+g - R2*cos(st2)) / 2;

					ASSERT(sanjiaoxing1 + sanjiaoxing2 > sanxing);
					s2 += sSub + sanxing - sanjiaoxing1 - sanjiaoxing2;					
				}else{
					//Case 2:
					double st = acos((dx+r+g)/R2);
					double st2 = acos((dx+r)/R2);
					double dirtSt = st2 - st;
					ASSERT(dirtSt>0);
					double h2 = R2 * sin(st2);
					double h1 = R2 * sin(st);

					double sanxing = dirtSt *  R2 * R2 / 2;
					double sanjiaoxing1 = (dx+r+g) * (h2 - h1 ) / 2;
					double sanjiaoxing2 = g * h2 / 2;

					ASSERT(sanjiaoxing1 + sanjiaoxing2 > sanxing);
					s2 += (h2 - dy - r) * g + sanxing - sanjiaoxing1 - sanjiaoxing2;					
				}
			}else{
				if((dx + r) * (dx + r ) + (dy + r + g) * ( dy + r + g ) <= dist){
					//Case 3:
					double st = asin((dy+r)/R2);
					double st2 = asin((dy+r+g)/R2);
					double dirtSt = st2 - st;
					ASSERT(dirtSt>0);
					double h2 = R2 * cos(st);
					double h1 = R2 * cos(st2);

					double sanxing = dirtSt *  R2 * R2 / 2;
					double sanjiaoxing1 = (dy+r+g) * (h2 - h1 ) / 2;
					double sanjiaoxing2 = g * h2 / 2;

					ASSERT(sanjiaoxing1 + sanjiaoxing2 > sanxing);
					s2 += (h2 - dx - r) * g + sanxing - sanjiaoxing1 - sanjiaoxing2;					
				}else{
					//Case 4:
					double st  = asin((dy+r)/R2);
					double st2 = acos((dx+r)/R2);
					double dirtSt = st2 - st;
					ASSERT(dirtSt>0);
					double sanxing = dirtSt * R2 * R2 / 2;

					double h2 = R2 * cos(st);
					double h1 = R2 * sin(st2);


					double sanjiaoxing1 = (h1 - dy - r ) * h2 / 2;
					double sanjiaoxing2 = (h2 - dx - r ) * h1 / 2;

					ASSERT(sanjiaoxing1 + sanjiaoxing2 > sanxing);
					s2 += (h1 - dy - r ) * (h2 - dx - r) + sanxing - sanjiaoxing1 - sanjiaoxing2;					
				}
			}
			dx += 2 * r + g;
		}
		dy +=  2 * r + g;
	};

	return 1 - 4*s2/s;
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
		int np=0;
		//f, R, t, r ,g;
		ReadWord(lpWord,lpLine,np,nLineLen);
		f = atof(lpWord);
		ReadWord(lpWord,lpLine,np,nLineLen);
		R = atof(lpWord);
		ReadWord(lpWord,lpLine,np,nLineLen);
		t = atof(lpWord);
		ReadWord(lpWord,lpLine,np,nLineLen);
		r = atof(lpWord);
		ReadWord(lpWord,lpLine,np,nLineLen);
		g = atof(lpWord);

		double fPro = calcProbability();
		nCS++;
		sprintf(buffer,"Case #%d: %f \n",nCS, fPro);
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
