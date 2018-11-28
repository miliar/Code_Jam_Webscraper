#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

typedef struct {
    //Data
    std::vector<char> board;
} CaseData;

char isWinning( char l[4] ){
    char sq = l[0];
    if( sq == 'T' ) sq = l[1];
    if( sq != '.' ){
        int c = 1;
        for( int k = 1; k < 4 ; k++ ){
            if( l[k] == sq || l[k] == 'T' )
                ++c;
        }
        if( c == 4 )
            return sq;
    }
    return 0;
}

std::string solve( CaseData data ){
    std::stringstream result;
    //Code
    //naive search
    char winner = '.';
    for( int i = 0; i < 4; i++){
        char l[4];
        //Horizontals
        for( int j = 0; j<4; j++ ){
            l[j] = data.board[i*4+j];
        }
        char t = isWinning( l );
        //Verticals
        if( t ){
            winner = t;
            break;
        }
        for( int j = 0; j<4; j++ ){
            l[j] = data.board[i+j*4];
        }
        t = isWinning( l );
        if( t ){
            winner = t;
            break;
        }
        // Diag 1
        if( i == 0 ){
            for( int j = 0; j<4; j++ ){
                l[j] = data.board[i+j*4+j];
            }
            t = isWinning( l );
            if( t ){
                winner = t;
                break;
            }
        }
        if( i == 3 ){
            for( int j = 0; j<4; j++ ){
                l[j] = data.board[i+j*4-j];
            }
            t = isWinning( l );
            if( t ){
                winner = t;
                break;
            }
        }
    }
    //check board
    if( winner == '.' ){
        for( int i = 0; i < 16; i++ ){
            if( data.board[i] == '.' ){
                result << "Game has not completed";
                break;
            } else if( i == 15 )
                result << "Draw";
        }
    } else {
        result << winner << " won";
    }

    return result.str();
}

int main(int argc, const char *argv[])
{
    if( argc != 3 )
        return -1;

    std::ifstream infile( argv[1] );
    std::ofstream outfile( argv[2] );

    std::cerr << argv[1] << " -> " << argv[2] << std::endl;
   

    //Read Cases
    int numCases;
    if( infile.is_open() ){
        infile >> numCases;
    } else {
        std::cerr << "Failed to open input" << std::endl;
        return -1;
    }

    std::string garbage;
    std::getline( infile, garbage );

    for( int i = 1; i <= numCases; i++ ){
        CaseData data;
        //Populate data
        for ( int j = 0; j < 16; ++j ){
            //if(!(j%4)) std::cout << std::endl;
            char tmp;
            infile >> tmp;
            data.board.push_back( tmp );
            //std::cout << data.board[j];
        }
        outfile << "Case #" << i << ": " << solve( data ) << std::endl;
    }


    return 0;
}
