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

	INT64 iNumOfSnappers;
	INT64 iSnaps;
	INT64 iIndex;
	BOOL result;

	cstdfRead.Open(L"D:\\A-large.in.txt",CStdioFile::modeRead);
	cstdfWrite.Open(L"D:\\codejam.out.txt",CStdioFile::modeCreate);
	cstdfWrite.Close();
	cstdfWrite.Open(L"D:\\codejam.out.txt",CStdioFile::modeWrite);

	memset(databuffer,0,sizeof(databuffer));
	cstdfRead.ReadString(databuffer,sizeof(databuffer)-1);
	iNumOfCases = _wtoi(databuffer);

	for (int iIndex1 = 0;iIndex1 < iNumOfCases;iIndex1++)
	{

		memset(databuffer,0,sizeof(databuffer));
		cstdfRead.ReadString(databuffer,sizeof(databuffer)-1);
		pwcToken = wcstok(databuffer,seps);
		iNumOfSnappers = _wtoi64(pwcToken);
		pwcToken = wcstok(NULL,seps);
		iSnaps = _wtoi64(pwcToken);

		INT64 temp = (INT64)pow((double)2,(double)iNumOfSnappers);
		if ((iSnaps+1)%temp == 0)
		{
			result == TRUE;
			memset(databuffer,0,sizeof(databuffer));
			wsprintf(databuffer,L"Case #%d: ON\n",iIndex1+1);
			cstdfWrite.WriteString(databuffer);
		}
		else
		{
			memset(databuffer,0,sizeof(databuffer));
			wsprintf(databuffer,L"Case #%d: OFF\n",iIndex1+1);
			cstdfWrite.WriteString(databuffer);
			result = FALSE;
		}
	}

	cstdfRead.Close();
	cstdfWrite.Close();
	return 0;
}

