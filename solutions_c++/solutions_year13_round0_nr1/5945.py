#include <iostream>
#include <fstream>
#include <cstring>
#include <cmath>

bool countLineT ( char grid[4][4] , int i ) {

    int j;

    for ( j = 0 ; j < 4 ; ++j ) {

        if ( grid[i][j] == 'T' )
            return true;
    }

    return false;
}

bool countColT ( char grid[4][4] , int j ) {

    int i;

    for ( i = 0 ; i < 4 ; ++i ) {

        if ( grid[i][j] == 'T' )
            return true;
    }

    return false;
}

bool countDiag1T ( char grid[4][4] ) {

    int i , j;

    for ( i = 0 , j = 0 ; i < 4 , j < 4 ; ++i , ++j ) {

        if ( grid[i][j] == 'T' )
            return true;
    }

    return false;
}

bool countDiag2T ( char grid[4][4] ) {

    int i , j;

    for ( i = 0 , j = 3 ; i < 4 , j >= 0 ; ++i , --j ) {

        if ( grid[i][j] == 'T' )
            return true;
    }

    return false;
}

int countLineX ( char grid[4][4] , int i ) {

    int j;
    int n ( 0 );

    for ( j = 0 ; j < 4 ; ++j ) {

        if ( grid[i][j] == 'X' )
            n++;
    }

    return n;
}

int countColX ( char grid[4][4] , int j ) {

    int i;
    int n ( 0 );

    for ( i = 0 ; i < 4 ; ++i ) {

        if ( grid[i][j] == 'X' )
            n++;
    }

    return n;
}

int countDiag1X ( char grid[4][4] ) {

    int i , j;
    int n ( 0 );

    for ( i = 0 , j = 0 ; i < 4 , j < 4 ; ++i , ++j ) {

        if ( grid[i][j] == 'X' )
            n++;
    }

    return n;
}

int countDiag2X ( char grid[4][4] ) {

    int i , j;
    int n ( 0 );

    for ( i = 0 , j = 3 ; i < 4 , j >= 0 ; ++i , --j ) {

        if ( grid[i][j] == 'X' )
            n++;
    }

    return n;
}

int countLineO ( char grid[4][4] , int i ) {

    int j;
    int n ( 0 );

    for ( j = 0 ; j < 4 ; ++j ) {

        if ( grid[i][j] == 'O' )
            n++;
    }

    return n;
}

int countColO ( char grid[4][4] , int j ) {

    int i;
    int n ( 0 );

    for ( i = 0 ; i < 4 ; ++i ) {

        if ( grid[i][j] == 'O' )
            n++;
    }

    return n;
}

int countDiag1O ( char grid[4][4] ) {

    int i , j;
    int n ( 0 );

    for ( i = 0 , j = 0 ; i < 4 , j < 4 ; ++i , ++j ) {

        if ( grid[i][j] == 'O' )
            n++;
    }

    return n;
}

int countDiag2O ( char grid[4][4] ) {

    int i , j;
    int n ( 0 );

    for ( i = 0 , j = 3 ; i < 4 , j >= 0 ; ++i , --j ) {

        if ( grid[i][j] == 'O' )
            n++;
    }

    return n;
}

bool X ( char grid[4][4] ) {

    int i;

    for ( i = 0 ; i < 4 ; ++i ) {

        if ( countLineX ( grid , i ) == 4 ) {

            return true;
            break;
        }

        if ( countLineX ( grid , i ) == 3 && countLineT ( grid , i ) ) {

            return true;
            break;
        }

        if ( countColX ( grid , i ) == 4 ) {

            return true;
            break;
        }

        if ( countColX ( grid , i ) == 3 && countColT ( grid , i ) ) {

            return true;
            break;
        }

        if ( countDiag1X ( grid ) == 4 ) {

            return true;
            break;
        }

        if ( countDiag1X ( grid ) == 3 && countDiag1T ( grid ) ) {

            return true;
            break;
        }

        if ( countDiag2X ( grid ) == 4 ) {

            return true;
            break;
        }

        if ( countDiag2X ( grid ) == 3 && countDiag2T ( grid ) ) {

            return true;
            break;
        }
    }

    return false;
}

bool O ( char grid[4][4] ) {

    int i;

    for ( i = 0 ; i < 4 ; ++i ) {

        if ( countLineO ( grid , i ) == 4 ) {

            return true;
            break;
        }

        if ( countLineO ( grid , i ) == 3 && countLineT ( grid , i ) ) {

            return true;
            break;
        }

        if ( countColO ( grid , i ) == 4 ) {

            return true;
            break;
        }

        if ( countColO ( grid , i ) == 3 && countColT ( grid , i ) ) {

            return true;
            break;
        }

        if ( countDiag1O ( grid ) == 4 ) {

            return true;
            break;
        }

        if ( countDiag1O ( grid ) == 3 && countDiag1T ( grid ) ) {

            return true;
            break;
        }

        if ( countDiag2O ( grid ) == 4 ) {

            return true;
            break;
        }

        if ( countDiag2O ( grid ) == 3 && countDiag2T ( grid ) ) {

            return true;
            break;
        }
    }

    return false;
}

bool full ( char grid[4][4] ) {

    int i , j;

    for ( i = 0 ; i < 4 ; ++i ) {

        for ( j = 0 ; j < 4 ; ++j ) {

            if ( grid[i][j] == '.' )
                return false;
        }
    }

    return true;
}

char checkAll ( char grid[4][4] ) {

    if ( X ( grid ) )
        return 1;

    if ( O ( grid ) )
        return 2;

    if ( full ( grid ) )
        return 0;

    return -1;
}

int main ( int argc , char *argv[] ) {

    std::ifstream input ( "input.txt" );
    std::ofstream output ( "output.txt" );
    if ( !input ) std::cout << "failed to open file." << std::endl;
    else {

        char grid[4][4];
        char buff[8];
        int i , j , k , n , s , s1 , s2 , s3 , s4;

        input >> buff;

        s = strlen(buff);
        s4 = pow(10,s-1);
        s3 = s/10;
        s2 = s/10;
        s1 = s/10;

        n = ( ( buff[0] - '0' ) * s4 ) + ( ( buff [1] - '0' ) * s3 ) + ( ( buff [3] - '0' ) * s2 ) + ( ( buff [4] - '0' ) * s1 );

        for ( i = 0 ; i < n ; ++i ) {

            for ( j = 0 ; j < 4 ; ++j ){

                input >> buff;

                for ( k = 0 ; k < 4 ; ++k )
                    grid[j][k] = buff[k];
            }

            char gameState = checkAll ( grid );

            output << "Case #" << i+1 << ": ";
            if ( gameState == -1 ) output << "Game has not completed";
            if ( gameState == 1 ) output << "X won";
            if ( gameState == 2 ) output << "O won";
            if ( gameState == 0 ) output << "Draw";
            output << std::endl;
        }
    }
    return 0;
}
