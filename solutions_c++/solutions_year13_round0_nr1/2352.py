#include <iostream>
#include <string>

using namespace std;

class Solver
{	
	char m_table[4][4];

	bool IsC(char c, int i, int j) const { return  m_table[i][j] == c || m_table[i][j] == 'T'; }
	bool CheckPlayer(char c)
	{
		int x1cnt, x2cnt, x3cnt = 0, x4cnt = 0;
		for ( int i = 0; i < 4; ++i ) {
			x1cnt = x2cnt = 0;
			for ( int j = 0; j < 4 ; ++j ) {
				if ( IsC(c, i, j) ) ++x1cnt; // -
				if ( IsC(c, j, i) ) ++x2cnt; // |
			}
			if ( x1cnt == 4 || x2cnt == 4 )
				break;
			if ( IsC(c, i, i) ) ++x3cnt;
			if ( IsC(c, i, 3-i) ) ++x4cnt;
		}
		if ( x1cnt == 4 || x2cnt == 4 || x3cnt == 4 || x4cnt == 4 )
			return true;
		return false;
	}
public:
	string Solve()
	{
		int dotcnt = 0;
		for ( int i = 0; i < 4; ++i )
		{
			for ( int j = 0 ; j < 4; ++j ) {
				cin >> m_table[i][j];
				if ( m_table[i][j] == '.' ) ++dotcnt;
			}
			if ( cin.get() != '\n' ) {
				return "Parse error";
			}
		}

		bool xwon = CheckPlayer('X');
		bool owon = CheckPlayer('O');
		if ( xwon ) {
			if ( owon )		return "Draw";
			else			return "X won";
		} else {
			if ( owon )		return "O won";
			else {
				if ( dotcnt )	return "Game has not completed";
				else			return "Draw";
			}
		}
	}
};

int main()
{
	int T;
	cin >> T;
	for ( int t = 0; t < T; ++t )
	{
		if ( cin.get() != '\n' ) {
			return -1;
		}
		cout << "Case #" << (t+1) << ": " << Solver().Solve() << endl;
	}
	return 0;
}
