
#include <list>
#include <iostream>
#include <fstream>
using namespace std;

#include <math.h>

int g_nStep;

///////////////////////////////

class CSequence
{
public:
	char m_cBot;
	int m_nButton;

	CSequence(char cBot, int nButton);
};

CSequence::CSequence(char cBot, int nButton)
{
	m_cBot = cBot;
	m_nButton = nButton;
}

typedef list<CSequence*> SeqList;

///////////////////////////////

class CProcess
{
public:
	enum PROC
	{
		procMove = 1,
		procPush = 2,
	};

	int m_nProc;
	int m_nTime;

	CProcess(int nProc, int nTime);
};

CProcess::CProcess(int nProc, int nTime)
{
	m_nProc = nProc;
	m_nTime = nTime;
}

typedef list<CProcess*> ProcList;

///////////////////////////////

class CBot
{
public:
	char m_cName;
	int m_nTime;
	ProcList m_listProc;

	CBot(char cName, SeqList& listSeq);
	~CBot();
};

CBot::CBot(char cName, SeqList& listSeq)
{
	m_cName = cName;
	m_nTime = 0;

	// Sequence To Process
	int nPos = 1;

	SeqList::iterator itor = listSeq.begin();

	while (itor != listSeq.end())
	{
		CSequence* pSeq = (CSequence*)*itor;
		itor++;
		
		if (pSeq->m_cBot != cName)
			continue;

		// 이동
		if (pSeq->m_nButton != nPos)
		{
			int nTime = abs(pSeq->m_nButton - nPos);
			nPos = pSeq->m_nButton;
			
			CProcess* pMoveProc = new CProcess(CProcess::procMove, nTime);
			m_listProc.push_back(pMoveProc);

			m_nTime += nTime;
		}

		// 버튼
		CProcess* pPushProc = new CProcess(CProcess::procPush, 1);
		m_listProc.push_back(pPushProc);

		m_nTime++;
	}
}

CBot::~CBot()
{
	ProcList::iterator itor = m_listProc.begin();
	while (itor != m_listProc.end())
	{
		CProcess* pProc = (CProcess*)*itor;
		itor++;

		delete pProc;
	}

	m_listProc.clear();
}

///////////////////////////////

class CCrashProcess
{
public:
	CProcess* m_pProcO;
	CProcess* m_pProcB;

	CCrashProcess(CProcess* pProcO, CProcess* pProcB);
};

CCrashProcess::CCrashProcess(CProcess* pProcO, CProcess* pProcB)
{
	m_pProcO = pProcO;
	m_pProcB = pProcB;
}

typedef list<CCrashProcess*> CrashList;

///////////////////////////////

/*
void Recursive_StayProcess(ProcList* pListO, ProcList::iterator itorO, int nTimeO, ProcList* pListB, ProcList::iterator itorB, int nTimeB, CrashList& listCrash, int* pMinTime)
{
	// 구해진 패턴에서 현재 패턴을 검색
	CrashList::iterator itor = listCrash.begin();
	while (itor != listCrash.end())
	{
		CCrashProcess* pCrashProc = (CCrashProcess*)*itor;
		itor++;
	
		// 있다면 더 이상 안해
		if (pCrashProc->m_pProcO == (CProcess*)*itorO && pCrashProc->m_pProcB == (CProcess*)&itorB)
			return;
	}

	// 없다면 동일한 프로세스 발견할 때 까지 찾기.
	while (itorO != pListO->end() && itorB != pListB->end())
	{
		CProcess* pProcO = (CProcess*)*itorO;
		CProcess* pProcB = (CProcess*)*itorB;

		// 있다면
		if (pProcO->m_nProc == CProcess::procPush && pProcB->m_nProc == CProcess::procPush)
		{	
			if (nTimeO == nTimeB)
			{
				// 재귀로 퍼트리기.
				itorO++;
				itorB++;

				Recursive_StayProcess(pListO, itorO, nTimeO+2, pListB, itorB, nTimeB+1, listCrash, pMinTime);
				Recursive_StayProcess(pListO, itorO, nTimeO+1, pListB, itorB, nTimeB+2, listCrash, pMinTime);
				
				// 현재 패턴을 구한적이 있는 패턴으로 저장.
				CCrashProcess* pCrashProc = new CCrashProcess(pProcO, pProcB);
				listCrash.push_front(pCrashProc);
				return;
			}
			else
			{
				if (nTimeO > nTimeB)
				{
					nTimeB += pProcB->m_nTime;
					itorB++;
				}
				else // nTimeO < nTimeB
				{
					nTimeO += pProcO->m_nTime;
					itorO++;
				}
			}
		}
		else
		{
			if (pProcO->m_nProc == CProcess::procMove)
			{
				nTimeO += pProcO->m_nTime;
				itorO++;
			}
			
			if (pProcB->m_nProc == CProcess::procMove)
			{
				nTimeB += pProcB->m_nTime;
				itorB++;
			}
		}
	}

	// 없다면 끝까지 진행 시키고 (pMinTime 과 비교후 저장)
	while (itorO != pListO->end())
	{
		CProcess* pProcO = (CProcess*)*itorO;
		itorO++;

		nTimeO += pProcO->m_nTime;
	}

	while (itorB != pListB->end())
	{
		CProcess* pProcB = (CProcess*)*itorB;
		itorB++;
		
		nTimeB += pProcB->m_nTime;
	}

	int nWorst = 0;
	if (nTimeO > nTimeB)
		nWorst = nTimeO;
	else
		nWorst = nTimeB;

	if (*pMinTime > nWorst)
		*pMinTime = nWorst;
}

int GetStayTime(CBot& Orange, CBot& Blue)
{
	ProcList* pListO = &Orange.m_listProc;
	ProcList* pListB = &Blue.m_listProc;

	ProcList::iterator itorO = pListO->begin();
	ProcList::iterator itorB = pListB->begin();
		
	CrashList listCrash;
	
	int nMinTime = 9999999;

	Recursive_StayProcess(pListO, itorO, 0, pListB, itorB, 0, listCrash, &nMinTime);

	//
	CrashList::iterator itor = listCrash.begin();
	while (itor != listCrash.end())
	{
		CCrashProcess* pCrashProc = (CCrashProcess*)*itor;
		itor++;

		delete pCrashProc;
	}

	listCrash.clear();
	

	return nMinTime;
}
*/


int GetTime(SeqList& listSeq)
{
	int nPosO = 1;
	int nPosB = 1;

	int nSpareTimeO = 0;
	int nSpareTimeB = 0;

	int nTime = 0;

	SeqList::iterator itor = listSeq.begin();
	while (itor != listSeq.end())
	{
		CSequence* pSeq = (CSequence*)*itor;
		itor++;

		if (pSeq->m_cBot == 'O')
		{
			int nConsumeTime = 0;

			// 이동
			nConsumeTime += abs(nPosO - pSeq->m_nButton) + 1;
			nPosO = pSeq->m_nButton;

			if (nSpareTimeO < nConsumeTime)
			{
				nTime += nConsumeTime - nSpareTimeO;
				nSpareTimeB += nConsumeTime - nSpareTimeO;
			}
			else
			{
				nTime += 1;
				nSpareTimeB++;
			}
			
			nSpareTimeO = 0;
		}
		else // pSeq->m_cBot == 'C'
		{
			int nConsumeTime = 0;
			
			// 이동
			nConsumeTime += abs(nPosB - pSeq->m_nButton) + 1;
			nPosB = pSeq->m_nButton;
			
			if (nSpareTimeB < nConsumeTime)
			{
				nTime += nConsumeTime - nSpareTimeB;
				nSpareTimeO += nConsumeTime - nSpareTimeB;
			}
			else
			{
				nTime += 1;
				nSpareTimeO++;
			}

			
			nSpareTimeB = 0;
		}
	}

	return nTime;
}

///////////////////////////////

void main()
{
	// 입력 준비
	ifstream ifs;
	ifs.open("input.txt");
	
	ofstream ofs;
	ofs.open("output.txt");

	// case
	int nCase = 0;
	ifs >> nCase;

	for (int i=0; i<nCase; i++)
	{
		int nSeq = 0;
		ifs >> nSeq;

		SeqList listSeq;

		for (int j=0; j<nSeq; j++)
		{
			char cBot = 0;
			int nButton = 0;

			ifs >> cBot;
			ifs >> nButton;


			CSequence* pSeq = new CSequence(cBot, nButton);
			listSeq.push_back(pSeq);
		}

		/*
		// Bot
		CBot Orange('O', listSeq);
		CBot Blue('B', listSeq);

		// 비교 후 추가 시간 계산
		//int nTime = GetStayTime(Orange, Blue);
		*/

		int nTime = GetTime(listSeq);

		// 출력
		ofs << "Case #" << i+1 << ": " << nTime << "\12";

		// SeqList 삭제
		SeqList::iterator itor = listSeq.begin();
		while (itor != listSeq.end())
		{
			CSequence* pSeq = (CSequence*)*itor;
			itor++;

			delete pSeq;
		}

		listSeq.clear();
	}
}