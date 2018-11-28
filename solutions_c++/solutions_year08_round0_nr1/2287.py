//============================================================================
// Name        : GoogleJam.cpp
// Author      : Wang Yunlong
// Version     :
// Copyright   : Copyright 2008
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

#ifndef NULL
#define NULL 0
#endif

#define TRYIT 0
#if TRYIT==1
#	define NOTICE(x) \
		cout<<x<<endl;
#	else
#	define NOTICE(x)
#endif

class CTestCase {
protected:
	int mS;
	//	unsigned long *pSHashTable;
	int mQ;
	unsigned long *pQHashSet;
	int mSwitchCNT;
public:
	CTestCase() {
		mS=0;
		mQ=0;
		mSwitchCNT=0;
		pQHashSet=NULL;

		char tmpSTR[128]= { 0 };//temp string for input
		NOTICE("Input Search Engine Number:")
		cin>>mS;
		NOTICE(mS)
		pQHashSet=new unsigned long[mS];
		cin.getline(tmpSTR, 128);
		for (int i=0; i<mS; i++) {
			cin.getline(tmpSTR, 128);
			NOTICE(tmpSTR)
		}

		NOTICE("Input Query Number:")
		cin>>mQ;
		unsigned long preQHash=0;
		unsigned long curQHash=0;
		int cntQHashSet=0;
		bool isHashValueInQHashSet=false;
		NOTICE(mQ)
		cin.getline(tmpSTR, 128);
		for (int i=0; i<mQ; i++) {
			cin.getline(tmpSTR, 128);
			NOTICE(tmpSTR)
			curQHash=HashString(tmpSTR);
			if (curQHash==preQHash) {
				continue;
			} else {
				preQHash=curQHash;
			}
			isHashValueInQHashSet=false;
			for (int j=0; j<cntQHashSet; j++) {
				if (curQHash==pQHashSet[j]) {
					isHashValueInQHashSet=true;
					break;
				}
			}
			if (isHashValueInQHashSet==false) {
				pQHashSet[cntQHashSet]=curQHash;
				cntQHashSet++;
				NOTICE(cntQHashSet)
			}
			if (cntQHashSet>=mS) {
				cntQHashSet=0;
				pQHashSet[cntQHashSet]=curQHash;
				cntQHashSet++;
				mSwitchCNT++;
			}
		}
	}

	~CTestCase() {
		NOTICE ("One case finished!")
		if (NULL!=pQHashSet)
			delete pQHashSet;
	}

	int Testing() {
		return mSwitchCNT;
	}

	static unsigned long HashString(char *str) {
		unsigned long hash = 5381;
		int c;
		while (c = *str++)
			hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
		return hash;
	}
};

class CProblem {
protected:
	int mCaseNum;
	int mCurCaseID;
	CTestCase *pTC;
public:
	CProblem() {
		NOTICE("Input Case Number:")
		cin>>mCaseNum;
		mCurCaseID=0;
		pTC=NULL;
	}
	void CaseTesting() {
		for (mCurCaseID=0; mCurCaseID<mCaseNum; mCurCaseID++) {
			pTC=new CTestCase();
			cout<<"Case #"<<mCurCaseID+1<<": "<<pTC->Testing()<<endl;
			delete pTC;
		}
	}
};

int main() {
	CProblem gcm;
	gcm.CaseTesting();
	return 0;
}
