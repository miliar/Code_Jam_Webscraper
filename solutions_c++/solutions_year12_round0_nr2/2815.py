// codejam.cpp : Defines the entry point for the console application.
//
#include <cstdio>
#include <iostream>

using namespace std;

int
main(int argc, char *argv[])
{
    unsigned T;

    std::cin >> T;


    for (unsigned iCase = 1; iCase <= T; ++iCase)
    {
        unsigned N, S, p;

        cin >> N;
        cin >> S;
        cin >> p;


        unsigned borderline(0);
        unsigned above(0);

        for (unsigned iTotal = 0; iTotal < N; ++iTotal)
        {
            unsigned total;
            cin >> total;

            if (p == 0)
            {
                above++;
                continue;
            }

            unsigned rem = total % 3;
            unsigned best_unsurprising;
            unsigned best_surprising;
            if (rem == 0)
            {
                best_unsurprising = total / 3;
                if (total == 0) best_surprising = best_unsurprising;
                else if (total == 30) best_surprising = best_unsurprising;
                else best_surprising = best_unsurprising + 1;
            }
            else if (rem == 1)
            {
                best_unsurprising = (total + 2)/ 3;
                best_surprising = best_unsurprising;
            }
            else if (rem == 2)
            {
                best_unsurprising = (total + 1)/ 3;
                if (total == 29) best_surprising = best_unsurprising;
                else best_surprising = best_unsurprising + 1;
            }

            if (best_unsurprising >= p)
            {
                above++;
            }
            // definitely not >= p
            else if (best_surprising < p)
            {
                // do nothing
            }
            // possibly- has to be surprising
            else
            {
                borderline++;
            }
        }

        unsigned max = above + std::min(borderline, S);

        std::cout << "Case #" << iCase << ": " << max << std::endl;

    }
    return 0;
}

