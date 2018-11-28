#ifndef GOOGLECODEJAM_QUALIFICATION_A_H
#define GOOGLECODEJAM_QUALIFICATION_A_H

#include <string>

class TicTacToeTomek
{
public:
	TicTacToeTomek() {}
	~TicTacToeTomek() {}

	void Clear()
	{
		for( unsigned int i = 0; i < 16; ++i )
			m_Board[i] = '.';
	}

	void AddLine( unsigned int line, char cell1, char cell2, char cell3, char cell4 )
	{
		unsigned int offset = line * 4;
		m_Board[offset++] = cell1;
		m_Board[offset++] = cell2;
		m_Board[offset++] = cell3;
		m_Board[offset]   = cell4;
	}

	std::string GetResult()
	{
		std::string result;
		//char player;
		if( !DoesLineHaveWinner( m_Board[ 0], m_Board[ 1], m_Board[ 2], m_Board[ 3], result ) )
		if( !DoesLineHaveWinner( m_Board[ 4], m_Board[ 5], m_Board[ 6], m_Board[ 7], result ) )
		if( !DoesLineHaveWinner( m_Board[ 8], m_Board[ 9], m_Board[10], m_Board[11], result ) )
		if( !DoesLineHaveWinner( m_Board[12], m_Board[13], m_Board[14], m_Board[15], result ) )
		if( !DoesLineHaveWinner( m_Board[ 0], m_Board[ 4], m_Board[ 8], m_Board[12], result ) )
		if( !DoesLineHaveWinner( m_Board[ 1], m_Board[ 5], m_Board[ 9], m_Board[13], result ) )
		if( !DoesLineHaveWinner( m_Board[ 2], m_Board[ 6], m_Board[10], m_Board[14], result ) )
		if( !DoesLineHaveWinner( m_Board[ 3], m_Board[ 7], m_Board[11], m_Board[15], result ) )
		if( !DoesLineHaveWinner( m_Board[ 0], m_Board[ 5], m_Board[10], m_Board[15], result ) )
		if( !DoesLineHaveWinner( m_Board[ 3], m_Board[ 6], m_Board[ 9], m_Board[12], result ) )
		if( !DoesBoardHaveEmptyCells() )
			result = "Draw";
		else 
			result = "Game has not completed";

		return result;
	}

	bool DoesLineHaveWinner( char cell1, char cell2, char cell3, char cell4, std::string &result )
	{
		if( cell1 == '.' || cell2 == '.' || cell3 == '.' || cell4 == '.' )
			return false;

		char player = cell1 == 'T' ? cell2 : cell1;
		if( ( cell1 == player || cell1 == 'T' ) &&
			( cell2 == player || cell2 == 'T' ) &&
			( cell3 == player || cell3 == 'T' ) &&
			( cell4 == player || cell4 == 'T' ) )
		{
			result.append( &player, 1 );
			result.append( " won" );
			return true;
		}
		else return false;
	}

	bool DoesBoardHaveEmptyCells()
	{
		for( unsigned int i = 0; i < 16; ++i )
			if( m_Board[i] == '.' )
				return true;
		return false;
	}

private:
	char m_Board[16];
};

#endif