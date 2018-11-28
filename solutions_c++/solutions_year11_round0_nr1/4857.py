
#include <queue>
#include "stdio.h"
#include "Bot Trust.h"

using namespace std;

CBotTrust		BotTrust;


CBotTrust::CBotTrust()
{
	m_nPositionOrange	= 1;
	m_nPositionBlue		= 1;
	m_nMovements		= 0;
}



CBotTrust::~CBotTrust()
{
}



queue<CBotTrust::element> CBotTrust::FillQueue( queue<element>& InputQueue, const queue<element>& OtherQueue )
{
	queue<element> Queue;
	const bool bOrange = OtherQueue.empty() ? !InputQueue.front().m_bOrange : OtherQueue.front().m_bOrange;
	while( !InputQueue.empty() && InputQueue.front().m_bOrange != bOrange )
	{
		element Elem( InputQueue.front() );
		InputQueue.pop();
		Queue.push( Elem );
	}

	return Queue;
}



inline const bool CBotTrust::InPosition( const queue<element>& Queue )
{
	if( !Queue.empty() && Queue.front().m_bOrange == m_InputQueue.front().m_bOrange )
	{
		if( Queue.front().m_bOrange )
			return ( m_InputQueue.front().m_nButton == Queue.front().m_nButton ) && ( Queue.front().m_nButton == m_nPositionOrange );
		else
			return ( m_InputQueue.front().m_nButton == Queue.front().m_nButton ) && ( Queue.front().m_nButton == m_nPositionBlue );
	}
	else
		return false;
}



void CBotTrust::MoveToPosition( const queue<element>& Queue )
{
	if( Queue.front().m_bOrange )
	{
		if( Queue.front().m_nButton > m_nPositionOrange )
			++m_nPositionOrange;
		else if( Queue.front().m_nButton < m_nPositionOrange )
			--m_nPositionOrange;
	}
	else
	{
		if( Queue.front().m_nButton > m_nPositionBlue )
			++m_nPositionBlue;
		else if( Queue.front().m_nButton < m_nPositionBlue )
			--m_nPositionBlue;
	}
}



inline void CBotTrust::PushButton( queue<element>& Queue )
{
	Queue.pop();
	m_InputQueue.pop();
}



void CBotTrust::ComputeCase( queue<element>& InputQueue )
{
	queue<element>	FirstQueue;
	queue<element>	SecondQueue;
	while( !m_InputQueue.empty() )
	{
		if( FirstQueue.empty() )
			FirstQueue = FillQueue( InputQueue, SecondQueue );
		if( SecondQueue.empty() )
			SecondQueue = FillQueue( InputQueue, FirstQueue );

		bool bPushed = false;
		if( InPosition( FirstQueue ) )
		{
			PushButton( FirstQueue );
			bPushed = true;
		}
		else if( !FirstQueue.empty() )
			MoveToPosition( FirstQueue );

		if( InPosition( SecondQueue ) && !bPushed )
			PushButton( SecondQueue );
		else if( !SecondQueue.empty() )
			MoveToPosition( SecondQueue );
				
		++BotTrust.m_nMovements;
	}
}



int main(int argc, char* argv[])
{
	int T;
	scanf_s( "%d", &T );
	for( int nCase = 0; nCase < T; ++nCase )
	{
		BotTrust.m_nPositionOrange = 1;
		BotTrust.m_nPositionBlue = 1;
		BotTrust.m_nMovements = 0;
		int N;
		scanf_s( "%d", &N );
		queue<CBotTrust::element> InputQueue;
		for( int nButton = 0; nButton < N; ++nButton )
		{
			CBotTrust::element Elem;
			char chType;
			scanf_s( "%c", &chType );
			while( chType == ' ' || chType == '\t' )
				scanf_s( "%c", &chType );
			switch( chType )
			{
				case 'O':
					Elem.m_bOrange = true;
					break;
				case 'B':
					Elem.m_bOrange = false;
					break;
				default:
					return 1;
			}
			scanf_s( "%d", &Elem.m_nButton );
			InputQueue.push( Elem );
		}
		BotTrust.m_InputQueue = InputQueue;
		BotTrust.ComputeCase( InputQueue );
		printf( "Case #%d: %d\n", nCase + 1, BotTrust.m_nMovements );
	}

	return 0;
}