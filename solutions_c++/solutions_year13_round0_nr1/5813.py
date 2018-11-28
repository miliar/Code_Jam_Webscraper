#include <iostream>
#include <cstdlib>
#include <vector>


typedef std::vector<std::string>  Tablero;

bool verify( Tablero&, char );
bool emptyT( Tablero& );

int main()
{

    int n;
    std::string caseW = "Case #";
    std::string caseP = ": ";

    std::cin >> n;
    std::string line;
    std::cin.ignore();

    for( int c=1; c <= n; c++ )
    {
        Tablero table;

        for( int i=0; i < 4; i++ )
        {
            getline( std::cin, line );
            table.push_back( line );
        }

        bool ans = verify( table, 'X' );

        if( ans )
            std::cout << caseW << c << caseP << "X won" << std::endl;
        else{
            ans = verify( table, 'O' );
            if( ans )
                std::cout << caseW << c << caseP << "O won" << std::endl;
            else{
                ans = emptyT( table );
                if( ans )
                    std::cout << caseW << c << caseP << "Game has not completed" << std::endl;
                else
                    std::cout << caseW << c << caseP << "Draw" << std::endl;
            }
        }

        getline( std::cin, line );
    }



  return( 0 );
}

bool
verify( Tablero& table, char ToFind )
{
    int cont = 0;
    bool next = false;

    for( int i=0; i < 4; i++ )
    {
        if( (table[i][0] == ToFind || table[i][0] == 'T') && (table[i][1] == ToFind || table[i][1] == 'T') && (table[i][2] == ToFind || table[i][2] == 'T') && (table[i][3] == ToFind || table[i][3] == 'T') )
                return( true );
    }

    for( int i=0; i < 4; i++ )
    {
        if( (table[0][i] == ToFind || table[0][i] == 'T') && (table[1][i] == ToFind || table[1][i] == 'T') && (table[2][i] == ToFind || table[2][i] == 'T') && (table[3][i] == ToFind || table[3][i] == 'T') )
                return( true );
    }


    for( int i=0; i < 4 && !next; i++ )
    {
        if( table[i][i] == ToFind || table[i][i] == 'T' )
            cont++;
        else
            next = true;
    }

    if( cont == 4)
        return( true );

    cont = 0;
    next = false;

    for( int i=0; i < 4 && !next; i++ )
    {
        if( table[3-i][i] == ToFind || table[3-i][i] == 'T' )
            cont++;
        else
            next = true;
    }

    if( cont == 4)
        return( true );


    return( false );
}

bool emptyT( Tablero& table)
{
    for( int i=0; i<4; i++ )
    {
        if( table[i][0] == '.' || table[i][1] == '.' || table[i][2] == '.' || table[i][3] == '.' )
            return( true );
    }

    return( false );
}
