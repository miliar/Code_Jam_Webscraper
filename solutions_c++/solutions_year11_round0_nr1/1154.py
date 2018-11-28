#include <cstdio>
#include <algorithm>
#include <vector>
#include <cassert>
#include <cmath>
using namespace std;

vector<pair<char, int> > sequence;

void readSequence()
{
	sequence.clear();
	int iNumber;
	char cRobot;
	scanf("%d%c", &iNumber, &cRobot);
	assert(cRobot == ' ');
	int iButton;
	for(int i=0; i<iNumber; i++)
	{
		scanf("%c %d", &cRobot, &iButton);
		assert(cRobot == 'O' || cRobot == 'B');
		sequence.push_back(make_pair(cRobot, iButton));
		if(i!=iNumber-1)
		{
			scanf("%c", &cRobot);
			assert(cRobot==' ');
		}	
	}
}

int compute()
{
	struct Position
	{
		int m_iButton, m_iTime;
	};
	
	Position orange, blue;
	orange.m_iButton = blue.m_iButton = 1;
	orange.m_iTime = blue.m_iTime = 0;
	
	int iCurrTime = 0;
	for(int iSeq = 0; iSeq < sequence.size(); iSeq++)
	{
		Position* p;
		if (sequence[iSeq].first == 'O')
			p = &orange;
		else
			p = &blue;
		
		const int iArriveTime = p->m_iTime + abs(p->m_iButton-sequence[iSeq].second);
		if (iArriveTime >= iCurrTime)
		{
			iCurrTime = iArriveTime + 1;	
		}
		else
		{
			iCurrTime++;
		}
		
		p->m_iButton = sequence[iSeq].second;
		p->m_iTime = iCurrTime;
	}
	
	return iCurrTime;
}

int main()
{
	int iTests;
	scanf("%d", &iTests);
	for(int iTestCase = 1; iTestCase <= iTests; iTestCase++)
	{
		readSequence();
		printf("Case #%d: %d\n", iTestCase, compute());
	}
	
	return 0;
}
