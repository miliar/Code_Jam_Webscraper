#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
    int T; // testcases
    cin >> T;

    int N; // number of Googlers
    int S; // surprising triplets of scores
    int p; // maximum number of Googlers that could have had a best result of at least p
    int t[30]; // the total points of the Googlers

    for (int it = 0 ; it < T ; it++)
    {
        cin >> N;
        cin >> S;
        cin >> p;
        for (int i = 0 ; i < N ; i++)
            cin >> t[i];

        // solve it
        int solution = 0;
        for (int i = 0 ; i < N ; i++)
        {
            double value = t[i];

            value -= p;
            if (value < 0)
                continue;

            value /= 2;

            if (value >= p - 1)
            {
                solution++;
		continue;
            }

            if (S > 0) // some surprising scores still remaining :)
            {
                if (value >= p - 2)
                {
                    solution++;
		    S--;
                }

            }


        }

        printf("Case #%d: %d\n", it+1, solution);
    }

    return 0;
}