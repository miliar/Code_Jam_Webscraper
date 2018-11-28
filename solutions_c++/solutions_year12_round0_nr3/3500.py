#include <iostream>
#include <cmath>
#include <set>

unsigned long pow10( unsigned short exponent )
{
    unsigned long v = 10;
    for( unsigned short i=2 ; i<=exponent ; ++i ) { v*=10; }
    return v;
}

unsigned long trimNdigits( unsigned short value, short N )
{
    return (value / pow10(N));
}

unsigned long lastNdigits( unsigned short value, short N )
{
    return (value - (trimNdigits(value,N) * pow10(N)) );
}

unsigned long recycleLastNDigits( unsigned short value, short N, unsigned short digits )
{
    return (trimNdigits(value,N) + (lastNdigits(value,N) * pow10(digits-N)));
}

int main()
{
    int T;
    std::cin >> T;
    ++T;//test cases are indexed from 1

    for( int test_case=1 ; test_case<T ; ++test_case )
    {
    //Prep
        unsigned long A,B;
        std::cin >> A >> B;

        unsigned short digits = std::log10( A ) + 1;

        unsigned long count = 0;

    //Work
        for( unsigned long n=A   ; n<B  ; ++n )
        {
            std::set<unsigned long> matches;

            for( unsigned short d=1 ; d < digits ; ++d)
            {
                unsigned long n2 = recycleLastNDigits( n , d, digits );

                if( n2 > n && n2 <= B ) { matches.insert( n2 ); }
            }

            count += matches.size();
        }

    //Results
        std::cout << "Case #" << test_case << ": " << count << std::endl;
    }
}
