// ProblemB.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <atlbase.h>
#include <atltypes.h>
#include <vector>
#include <map>
#include <algorithm>
#include <fstream>

using namespace std;

class CCell;
typedef vector<CCell> IntVec;
typedef vector<IntVec> IntMatrix;


vector<CCell*> g_vSinks;
IntMatrix Map;

struct CIsUpLeft   
{
	bool operator()(CPoint pt1, CPoint pt2)
	{
		if( pt1.y < pt2.y )
			return true;
		else if( pt1.y == pt2.y )
		{
			if(pt1.x < pt2.x)
				return true;
		}
		return false;

	}
};

class CCell
{
public:
	CCell() 
		:m_ptCoor(-1, -1),
		m_iAlt(0),
		m_mpCommon(NULL),m_pChar(NULL)
	{}
	~CCell()
	{
		if( m_mpCommon )
		{
			map<CPoint, int, CIsUpLeft>::iterator	itBeg = m_mpCommon->begin(),
													itEnd = m_mpCommon->end();
			for( ; itBeg != itEnd; ++itBeg )
			{
				Map[itBeg->first.y][itBeg->first.x].m_mpCommon = NULL;
			}
			delete m_mpCommon;
			m_mpCommon = NULL;
		}
	}
	void FlowInto()
	{
		CPoint ptTmp = m_ptCoor;
		CPoint ptMin = m_ptCoor;
		int MinAlt = m_iAlt;
		ptTmp.y--;
		if( ptTmp.y >= 0 )
		{
			if(Map[ptTmp.y][ptTmp.x].m_iAlt < MinAlt )
			{
				ptMin = ptTmp;
				MinAlt = Map[ptTmp.y][ptTmp.x].m_iAlt;
			}

		}
		ptTmp.y++;
		ptTmp.x--;
		if( ptTmp.x >= 0 )
		{
			if(Map[ptTmp.y][ptTmp.x].m_iAlt < MinAlt )
			{
				ptMin = ptTmp;
				MinAlt = Map[ptTmp.y][ptTmp.x].m_iAlt;
			}

		}
		ptTmp.x += 2;
		if( ptTmp.x < Map[ptTmp.y].size() )
		{
			if(Map[ptTmp.y][ptTmp.x].m_iAlt < MinAlt )
			{
				ptMin = ptTmp;
				MinAlt = Map[ptTmp.y][ptTmp.x].m_iAlt;
			}

		}
		ptTmp.x--;
		ptTmp.y++;
		if( ptTmp.y < Map.size() )
		{
			if(Map[ptTmp.y][ptTmp.x].m_iAlt < MinAlt )
			{
				ptMin = ptTmp;
				MinAlt = Map[ptTmp.y][ptTmp.x].m_iAlt;
			}
		}
		
		if( ptMin == m_ptCoor )
		{
			g_vSinks.push_back(this);
			if( !m_mpCommon )
				m_mpCommon = new map<CPoint, int, CIsUpLeft>();
			m_mpCommon->insert(pair<CPoint, int>(m_ptCoor, 0));
		}
		else
		{
			if( !m_mpCommon )
			{
				if( !Map[ptMin.y][ptMin.x].m_mpCommon )
				{
					m_mpCommon = new map<CPoint, int, CIsUpLeft>();
					Map[ptMin.y][ptMin.x].m_mpCommon = m_mpCommon;
				}
				else
					m_mpCommon = Map[ptMin.y][ptMin.x].m_mpCommon;
			}
			else
			{
				if( !Map[ptMin.y][ptMin.x].m_mpCommon )
					Map[ptMin.y][ptMin.x].m_mpCommon = m_mpCommon;
				else
				{
					Map[ptMin.y][ptMin.x].m_mpCommon->insert(m_mpCommon->begin(), m_mpCommon->end());
					map<CPoint, int, CIsUpLeft>* mpTmp = m_mpCommon;
					map<CPoint, int, CIsUpLeft>::iterator	itBeg = m_mpCommon->begin(),
															itEnd = m_mpCommon->end();
					for( ; itBeg != itEnd; ++itBeg )
					{
						Map[itBeg->first.y][itBeg->first.x].m_mpCommon = Map[ptMin.y][ptMin.x].m_mpCommon;
					}
					m_mpCommon = Map[ptMin.y][ptMin.x].m_mpCommon;
					delete mpTmp;
					
				}
					
			}
			m_mpCommon->insert(pair<CPoint, int>(ptMin, 0));
			m_mpCommon->insert(pair<CPoint, int>(m_ptCoor, 0));
			
		}

	}
	
	bool IsUpLeft(CCell* pCell)
	{
		CIsUpLeft Cmp;
		return Cmp(m_mpCommon->begin()->first,  pCell->m_mpCommon->begin()->first);
	}
	CPoint		m_ptCoor;
	int			m_iAlt;
	map<CPoint, int, CIsUpLeft>* m_mpCommon;
	char		m_cChar;
	CPoint		m_ptWhere;
	char		*m_pChar;
};


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("B-large.in");//B-small-attempt4.in");
    ofstream out("B-large.out");//B-small-attempt4.out");
    int  iTasks;
	in >> iTasks;
    for( int  iCount = 1; iCount <= iTasks; iCount++ )
    {
		int H, W;
		in >> H >> W;

		for( int i = 0; i < H; i++ )
		{
			Map.push_back(IntVec(W));
			for( int j = 0; j < W; j++ )
			{
				in >> Map[i][j].m_iAlt;
				Map[i][j].m_ptCoor.x = j;
				Map[i][j].m_ptCoor.y = i;
			}
		}

		for( int i = 0; i < H; i++ )
		{
			for( int j = 0; j < W; j++ )
			{
				Map[i][j].FlowInto();
			}
		}
		sort(g_vSinks.begin(), g_vSinks.end(), mem_fun(&CCell::IsUpLeft));
		char c = 'a';
		for( size_t i = 0; i < g_vSinks.size(); i++ )
		{
			map<CPoint, int, CIsUpLeft>::iterator	itBeg = g_vSinks[i]->m_mpCommon->begin(),
													itEnd = g_vSinks[i]->m_mpCommon->end();

			for( ; itBeg != itEnd; ++itBeg )
			{
				Map[itBeg->first.y][itBeg->first.x].m_cChar = c;
			}
			c++;
		}
		out<<"Case #"<< iCount <<":\n";
		for( size_t i = 0; i < Map.size(); i++ )
		{
			for( size_t j = 0; j < Map[i].size(); j++ )
			{
				out << Map[i][j].m_cChar << " ";
			}
			out << "\n";
		}
		Map.clear();
		g_vSinks.clear();

	}

	return 0;
}

