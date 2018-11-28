// Minimum Scalar Product.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <afx.h>
#include <map>
#include <vector>
#include <stdlib.h>

using namespace std;
class Line
{
public:
	int a;
	int b;
	Line(int a,int b)
	{
		this->a = a;
		this->b = b;
	}
	Line()
	{
		;
	}
	void operator = (const Line & l)
	{
		this->a = l.a;
		this->b = l.b;
	}
};
int _tmain(int argc, _TCHAR* argv[])
{

	CStdioFile cstdfRead;
	CStdioFile cstdfWrite;
	wchar_t databuffer[16*1024];
	INT64 iNumOfCases;
	wchar_t * seps = L" ";
	wchar_t * pwcToken;
	INT64 iTemp,iResult,iNumOfWires;
	int a,b;
	vector<Line> lines;
	vector<Line>::iterator iter;
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
		iResult = 0;
		lines.clear();
		memset(databuffer,0,sizeof(databuffer));
		cstdfRead.ReadString(databuffer,sizeof(databuffer)-1);
		iNumOfWires = _wtoi64(databuffer);
		for (int iIndex2 = 0;iIndex2 < iNumOfWires;iIndex2++)
		{
			memset(databuffer,0,sizeof(databuffer));
			cstdfRead.ReadString(databuffer,sizeof(databuffer)-1);
			pwcToken = wcstok(databuffer,seps);
			a = _wtoi(pwcToken);
			pwcToken = wcstok(NULL,seps);
			b = _wtoi(pwcToken);
			lines.push_back(Line(a,b));
		}
		while(lines.size() > 1)
		{
			Line l1,l2;
			iter = lines.begin();
			l1 = *iter;
			iter++;
			for (;iter!=lines.end();iter++)
			{
				l2 = *iter;
				if ((l1.a-l2.a)*(l1.b-l2.b)<0)
				{
					iResult++;
				}
			}
			lines.erase(lines.begin());
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

