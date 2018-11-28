#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

bool checkWin( vector<string> b, char ch );
bool checkFull( vector<string> b );

int main ()
{
    vector<string> board;
	string row;
    
	ofstream out;
  	out.open ("a.out");
    
  	int T;
  	cin >> T;
    
  	for ( size_t t = 0; t < T; ++t)
  	{
        for ( size_t a = 0; a < 4; ++a )
        {
            cin >> row;
            board.push_back(row);
        }
        
        string output = "Game has not completed";
        
        if ( checkWin( board, 'X' ) )
            output = "X won";
        else if ( checkWin( board, 'O' ) )
            output = "O won";
        else if ( checkFull( board ) )
            output = "Draw";
        
		board.clear();
        
  		out << "Case #" << t + 1 << ": " << output << endl;
  		cout << "Case #" << t + 1 << ": " << output << endl;
  	}
	
  	return 0;
}

bool checkFull( vector<string> b )
{
    for (int x = 0; x < 4; ++x)
        for (int y = 0; y < 4; ++y)
            if ( b[x][y] == '.' ) return false;
    
    return true;
}

bool checkWin( vector<string> b, char ch )
{
    int i;
    
    for (i = 0; i < 4; ++i)
    {
        if ((b[i][0] == ch || b[i][0] == 'T') && (b[i][1] == ch || b[i][1] == 'T')
            && (b[i][2] == ch || b[i][2] == 'T') && (b[i][3] == ch || b[i][3] == 'T'))
        {
            return true;
        }
        
        if ((b[0][i] == ch || b[0][i] == 'T') && (b[1][i] == ch || b[1][i] == 'T')
            && (b[2][i] == ch || b[2][i] == 'T') && (b[3][i] == ch || b[3][i] == 'T'))
        {
            return true;
        }
    }
    
    int c1, c2;
    c1 = c2 = 0;
    for (i = 0; i < 4; ++i)
    {
        if (b[i][i] == ch || b[i][i] == 'T') c1++;
        if (b[i][3-i] == ch || b[i][3-i] == 'T') c2++;
    }
    
    if (c1 == 4 || c2 == 4)
        return true;
    
    return false;
}
