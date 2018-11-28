// codejam.cpp : Defines the entry point for the console application.
//
#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

int
main(int argc, char *argv[])
{
    unsigned T;
    cin >> T;
    for (unsigned iCase = 1; iCase <= T; ++iCase)
    {
        unsigned A, B;
        cin >> A >> B;
        unsigned cnt(0);

        unsigned nDigits(1);
        unsigned leading(1);
        unsigned X = A; while (X >= 10) {nDigits++; X -= X%10; X/= 10; leading*=10;}

        for (unsigned n = A; n <= B; ++n)
        {
            for (unsigned m = n+1; m <= B; ++m)
            {
                unsigned m_rotated = m;
                for (unsigned i = 1; i < nDigits; ++i)
                {
                    unsigned rem = m_rotated % 10;
                    m_rotated = (m_rotated - rem)/10;
                    m_rotated += leading * rem;
                    if (m_rotated == n)
                    {
                        cnt++;
                        i = nDigits;
                    }
                }
            }
        }
        std::cout << "Case #" << iCase << ": " << cnt << std::endl;
    }
}

