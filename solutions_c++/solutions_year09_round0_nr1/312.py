#include <iostream>
#include <set>
#include <string>

std::set< std::string > prefixes;

int compute( int index, std::string &word, std::string current)
{
    if( index == word.length( ) ) return 1;
    else
    {
        if( word[ index ] != '(' )
        {
            current += word[ index++ ];
            if( prefixes.find( current ) != prefixes.end( ) ) return compute( index, word, current );
            else return 0;
        }
        else
        {
            int ret = 0;
            int temp = index;
            while( word[ temp ] != ')' ) ++temp;
            
            for( int i = index + 1 ; i < temp ; ++i )
            {
                std::string tCurr = current;
                tCurr += word[ i ];
                if( prefixes.find( tCurr ) != prefixes.end( ) )
                    ret += compute( temp + 1, word, tCurr );
            }
            
            
            return ret;
        }
    }
}

int main( )
{
    int k, d, n;
    std::cin >> k >> d >> n;
    while( d-- )
    {
        std::string word, copy;
        std::cin >> word;
        
        
        for( int i = 0 ; i < k ; ++i )
        {
            copy += word[ i ];
            prefixes.insert( copy );
        }
    }
    
    for( int i = 0; i < n ; ++i )
    {
        std::string word;
        std::cin >> word;
        
        int ret = compute( 0 , word , "" );
        std::cout << "Case #" << (i+1) << ": " << ret << std::endl;     
    }
}