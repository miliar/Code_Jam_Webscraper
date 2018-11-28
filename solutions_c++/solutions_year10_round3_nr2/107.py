// Minimum Scalar Product.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <afx.h>
#include <map>
#include <vector>
#include <stdlib.h>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{

	CStdioFile cstdfRead;
	CStdioFile cstdfWrite;
	wchar_t databuffer[16*1024];
	INT64 iNumOfCases;
	wchar_t * seps = L" ";
	wchar_t * pwcToken;
	INT64 iTemp,iResult;
	INT64 L,P,C,T;
	//cstdfRead.Open(L"D:\\A-large-practice.in.txt",CStdioFile::modeRead);
	cstdfRead.Open(L"test.txt",CStdioFile::modeRead);
	cstdfWrite.Open(L"out.txt",CStdioFile::modeCreate);
	cstdfWrite.Close();
	cstdfWrite.Open(L"out.txt",CStdioFile::modeWrite);

	memset(databuffer,0,sizeof(databuffer));
	cstdfRead.ReadString(databuffer,sizeof(databuffer)-1);
	iNumOfCases = _wtoi(databuffer);

	for (int iIndex1 = 0;iIndex1 < iNumOfCases;iIndex1++)
	{
		printf("%d\n",iIndex1+1);
		T=0;
		iResult = 0;
		memset(databuffer,0,sizeof(databuffer));
		cstdfRead.ReadString(databuffer,sizeof(databuffer)-1);
		pwcToken = wcstok(databuffer,seps);
		L = _wtoi64(pwcToken);
		pwcToken = wcstok(NULL,seps);
		P = _wtoi64(pwcToken);
		pwcToken = wcstok(NULL,seps);
		C = _wtoi64(pwcToken);
		while(L<P)
		{
			T++;
			L *= C;
		}
		while(T>1)
		{
			T = (T+1)/2;
			iResult++;
		}
	
		wchar_t num[64];
		_i64tow(iResult,num,10);
		memset(databuffer,0,sizeof(databuffer));
		wsprintf(databuffer,L"Case #%d: %s\n",iIndex1+1,num);
		cstdfWrite.WriteString(databuffer);
	}

	cstdfRead.Close();
	cstdfWrite.Close();
	return 0;
}

