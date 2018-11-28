#include <iostream>
#include <limits>
#include <string>

int main()
{
                           // abcdefghijklmnopqrstuvwxyz
    static std::string MAP = "yhesocvxduiglbkrztnwjpfmaq";

    int N;
    std::cin >> N;
    ++N;//test cases are indexed from 1

    //now ingore the rest of the line inc newline, eases some tests that
	//try to read a line at a time (and stick on this \n if not removed)
    std::cin.ignore( std::numeric_limits<std::streamsize>::max() , '\n' );

    for( int test_case=1 ; test_case<N ; ++test_case )
    {
    //Prep
        std::string line;
        std::getline(std::cin, line);

        for( auto& c : line )
        {
            if( 97 <= c && c <= 122) // a-z
                c = MAP[c-97];
        }

    //Work
        std::cout << "Case #" << test_case << ": " << line << std::endl;

    //Clean Up
    }
}
