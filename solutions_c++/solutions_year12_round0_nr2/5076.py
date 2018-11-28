
#include "liar.h"

/*********************************************************
 Group
 6 2 8 29 20 8 18 18 21
 **********************************************************/
Result::Result( int totalScore )
: isSurprise( false ),
m_total( totalScore )
{
	FillResultSet( );
}

void Result::FillResultSet( )
{
	int divisor = m_total;
	
	for( int i = 3; i > 0; i-- )
	{
		int x = divisor/i;
		
		m_resultSet[i-1] = x;
		
		divisor = divisor - x;
		//cout << x<<"\n";
	}
}

bool Result::SetSurprise( int p )
{
	bool canShift1 = false;
	bool canShift2 = false;
	bool loc1;
	bool loc2;
	
	for( int i = 0; i <= 3; i++ )
	{
		if( (m_resultSet[i]+1) == p )
		{
			if (canShift1 == true)
			{
				canShift2 = true;
				loc2 = i;
			}
			else
			{
				canShift1 = true;
				loc1 = i;
			}
		}
		//cout << x<<"\n";
	}
	
	if( canShift1 && canShift2 )
	{
		int temp1 = m_resultSet[loc1];
		int temp2 = m_resultSet[loc2];
		
		if( (temp1 != 0) && (temp2 != 0) )
		{
			m_resultSet[loc1] = temp1 +1;
			m_resultSet[loc2] = temp2 -1;
			isSurprise = true;
		}
	}
	
	return isSurprise;
}

void Result::PrintResult( )
{
	for( int i = 0; i < 3; i++ )
	{
		cout<<m_resultSet[i]<<"\t";
	}
	cout << "\n";
}

int Result::GetMax( )
{
	int retVal = 0;
	for( int i = 0; i < 3; i++ )
	{
		if( m_resultSet[i] > retVal )
		{
			retVal = m_resultSet[i];
		}
	}
	return retVal;
}

/*****************************

*******************************/
GroupOfGooglers::GroupOfGooglers( vector<int> totalOfGooglers, int numberOfSurprises, int p )
: m_numberOfSurprises( numberOfSurprises ), 
  m_p( p )
{
	for( vector<int>::iterator it = totalOfGooglers.begin( );
							   it != totalOfGooglers.end( ); ++it )
	{
		Result* newResult = new Result(*it);
		m_resultSetOfGooglers.push_back( newResult );
	}
	SetSurprise( );
}
void GroupOfGooglers::SetSurprise( )
{
	int numberOfSurprisesToSet = m_numberOfSurprises;
	
	for (vector<Result*>::iterator it = m_resultSetOfGooglers.begin( );
		 it != m_resultSetOfGooglers.end( ) ; ++it )
	{
		if( numberOfSurprisesToSet == 0 )
		{
			return;
		}
			
		if( (*it)->SetSurprise(m_p) == true )
		{
			numberOfSurprisesToSet--;
			//cout << "\n seted a surprise";
		}
	}
}
int GroupOfGooglers::Solve( )
{
	
	int retValue = 0;
	for (vector<Result*>::iterator it = m_resultSetOfGooglers.begin( );
							it != m_resultSetOfGooglers.end( ) ; ++it )
	{
		if( (*it)->GetMax( ) >= m_p )
		{
			retValue++;
		}
		//(*it)->PrintResult( );
	}
	return retValue;
}