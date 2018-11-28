#include "ElevationMap.h"
#include <iostream>

using namespace std;
//--------------------------- class cell -----------------------------


char cell::m_sNextCharacter = 'a';
char cell::GetBasin()
{
	if(m_pBasin)
	{
		return m_pBasin->GetBasin();
	}
	else
	{
		// If i am basin, then i am getting a sink character and inc next character.
		// basin character assignement will start when water will start to flow.
		// so i don't know who is setting this value.
		if(m_Sink == 0)
			m_Sink = m_sNextCharacter++;
		
		return m_Sink;
	}
}

void cell::SetBasin(cell* pMinNeighbour)
{

	if(pMinNeighbour == 0)
	{
		//if there were no neighbours , pMinNeighbour will be null .. :)
		m_pBasin = 0;
	}
	else
	{
		if ( pMinNeighbour->GetElevation() < GetElevation() )
			m_pBasin = pMinNeighbour;
		else
		{
			// I am the basin then. So just keeping zero here to indicate so.
			m_pBasin = 0;
		}
	}
	
}

//----------------------------------------------------------------------------

map::map(int r, int c)
:m_rows(r), m_cols(c)
{
	m_ppElevationMatrix = new cell* [m_rows];
	for ( int i = 0; i < m_rows; i++)
	{
		m_ppElevationMatrix[i] = new cell[m_cols];
	}

	//lets us reinit the first character. so that main doesn't have to worry.
	cell::m_sNextCharacter = 'a';
}
map::~map()
{
	for ( int i = 0; i < m_rows; i++)
	{
		delete[] m_ppElevationMatrix[i];
	}

	delete[] m_ppElevationMatrix;
}
void map::SetElevationData(int r, int c, int elevation)
{
	m_ppElevationMatrix[r][c].SetElevation(elevation);
}

bool map::IsValid(int r, int c)
{
	return (r >=0 && r < m_rows && c >=0 && c < m_cols);
}
void map::SetupBasins()
{
	for ( int r = 0; r < m_rows; r++)
	{
		for (int c = 0; c < m_cols; c++)
		{
			cell* pMin = 0;

			//if north is valid
			if(IsValid(r-1,c))
			{
				pMin = &(m_ppElevationMatrix[r-1][c]);
			}
			//if west is valid
			if ( IsValid ( r, c - 1))
			{
				if(!pMin)
					pMin = &(m_ppElevationMatrix[r][c-1]);
				else if( m_ppElevationMatrix[r][c-1].GetElevation() < pMin->GetElevation() )
					pMin = &(m_ppElevationMatrix[r][c-1]);
			}
			// if east is valid
			if ( IsValid ( r, c + 1))
			{
				if(!pMin)
					pMin = &(m_ppElevationMatrix[r][c+1]);
				else if( m_ppElevationMatrix[r][c+1].GetElevation() < pMin->GetElevation() )
					pMin = &(m_ppElevationMatrix[r][c+1]);
			}
			// if south is valid
			if ( IsValid ( r + 1, c ))
			{
				if(!pMin)
					pMin = &(m_ppElevationMatrix[r+1][c]);
				else if( m_ppElevationMatrix[r+1][c].GetElevation() < pMin->GetElevation() )
					pMin = &(m_ppElevationMatrix[r+1][c]);
			}

			m_ppElevationMatrix[r][c].SetBasin(pMin);
		}
	}	
}
void map::PrintBasins()
{
	for ( int r = 0; r < m_rows; r++)
	{
		for (int c = 0; c < m_cols; c++)
		{
			cout << m_ppElevationMatrix[r][c].GetBasin() ;
			
			//If not last then do it... being skeptic.
			if ( c < m_cols - 1 )
				cout << " " ;
		}
		cout << endl;
	}
}