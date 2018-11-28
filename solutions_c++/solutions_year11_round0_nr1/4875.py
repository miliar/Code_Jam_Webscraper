#include <iostream>
#include <fstream>
#include <queue>

int main(int argc, char* argv[])
{
    std::ifstream file( argv[1] );
    int tests;
    file >> tests;

    std::cerr << "tests: " << tests << std::endl;

    std::string line;
    for( int c = 0; c < tests; ++c )
    {
        std::queue<int> o, b;
        std::queue<char> y;
        int po = 1, pb = 1;
        int buttons = 0;
        file >> buttons;

        std::cerr << "test " << c << ", buttons: " << buttons << std::endl;

        for( int but = 0; but < buttons; ++but )
        {
            char R = '\0';
            int next_but = 0;
            do {
                file >> R;
            } while( std::isspace( R ) );
            file >> next_but;

            ( R == 'O' ? o : b ).push( next_but );
            y.push( R );

            std::cerr << R << " " << next_but << std::endl;
        }

        int count = 0;
        while(!y.empty())
        {
            std::queue<int>* to_pop = 0;
            // O
            if (y.front() == 'O' && po == o.front())
                to_pop = &o;
            else if( po < o.front() )
            {
                ++po;
                std::cerr << "O moves to " << po << std::endl;
            }
            else if( po > o.front() )
            {
                --po;
                std::cerr << "O moves to " << po << std::endl;
            }

            // B
            if (y.front() == 'B' && pb == b.front())
                to_pop = &b;
            else if( pb < b.front() )
            {
                ++pb;
                std::cerr << "B moves to " << pb << std::endl;
            }
            else if( pb > b.front() )
            {
                --pb;
                std::cerr << "B moves to " << pb << std::endl;
            }

            if( to_pop )
            {
                std::cerr << y.front() << " pushes " << to_pop->front() << std::endl;
                y.pop();
                to_pop->pop();
            }

            count++;
            std::cerr << "---" << count << "---" << std::endl;
        }

        std::cout << "Case #" << c+1 << ": " << count << std::endl;
    }
    return 0;
}
