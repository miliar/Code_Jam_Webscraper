#include <iostream>
#include <fstream>
#include <boost/lexical_cast.hpp>
#include <map>

std::string solveTestCase( std::ifstream& file )
{
    char buff[255];
    char board[4][4];

    std::map<char,unsigned int> counters[10];
    for( unsigned int row = 0; row < 4; row++ )
    {
        file.getline(buff, sizeof(buff) );
        board[row][0]=buff[0];
        board[row][1]=buff[1];
        board[row][2]=buff[2];
        board[row][3]=buff[3];

        counters[row]['O']=0;
        counters[row]['T']=0;
        counters[row]['X']=0;
	counters[row]['.']=0;

        counters[4+row]['O']=0;
        counters[4+row]['T']=0;
        counters[4+row]['X']=0;
	counters[4+row]['.']=0;

        counters[8+row/2]['O']=0;
        counters[8+row/2]['T']=0;
        counters[8+row/2]['X']=0;
	counters[8+row/2]['.']=0;
    }

    for( unsigned int row = 0; row < 4; row++ )
    {
        for( unsigned int col = 0; col < 4; col++ )
        {
	    counters[row][ board[row][col] ]++;
	    counters[4+row][ board[col][row] ]++;
	    if( row == col )
	    {
	      counters[8][ board[row][col] ]++;
	    }
	    else if( col == (3-row) )
	    {
	      
		counters[9][ board[row][col] ]++;
	    }
        }
    }

    std::string result = "Game has not completed";
    unsigned int sum = 0;
    for( unsigned int i = 0; i < 10; i++ )
    {
        sum += counters[i]['X'];
	sum += counters[i]['O'];
	sum += counters[i]['T'];
	if( counters[i]['O'] == 4 || ( counters[i]['O'] == 3 && counters[i]['T']  == 1) )
	{
	   return "O won";
	}
	
	if( counters[i]['X'] == 4 || ( counters[i]['X'] == 3 && counters[i]['T']  == 1) )
	{
	  return "X won";
	}
    }
    
    if( sum == 40 )
    {
      return "Draw";
    }
  
    return result;
}

int main(int argc, char **argv) {
    std::ifstream file( "input.txt" );
    if( file.good() )
    {
        char buff[255];
        file.getline( buff, sizeof(buff) );
        unsigned int numberOfTests = boost::lexical_cast<unsigned int>(buff);

        for( unsigned int i = 0; i < numberOfTests && file.good(); i++ )
        {
            std::string result = solveTestCase(file);
	    std::cout << "Case #" << i+1 << ": " << result << std::endl;
            if( file.good() )
            {
                file.getline(buff, sizeof(buff));
            }
        }
    }

    return 0;
}
