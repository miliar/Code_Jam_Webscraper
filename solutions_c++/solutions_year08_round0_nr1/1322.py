//Author: Grzegorz Anielak

#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int T, n;
    cin >> T;
    for (int t = 0; t < T; ++t)
    {
        int S, Q;

        cin >> S;
        int best = 0;                       //minimal value
        int ebest = S;                      //how many engines with min. value
        vector<string> engines(S);
        vector<int> value(S, 0);            //values of engines

        cin.ignore(2, '\n');
        for (int s = 0; s < S; ++s)
            getline(cin, engines[s]);

        cin >> Q;
        cin.ignore(2, '\n');
        while (Q--)
        {
            string query;
            getline(cin, query);
            int s = 0;
            while (engines[s] != query)
                ++s;

            if (value[s] == best && --ebest == 0)
            {
                ++best;
                ebest = S - 1;
            }

            value[s] = best + 1;
        }
        cout << "Case #" << t + 1 << ": " << best << endl;
    }
    return 0;
}

