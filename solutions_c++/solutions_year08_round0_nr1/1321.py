/* vim: set sw=4 sts=4 et foldmethod=syntax : */

#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
    int N;
    cin >> N;

    for (int n = 0 ; n < N ; ++n)
    {
        int S, Q;
        cin >> S;
        map<string, int> engines;

        int min = 0;
        int mins = S;

        int new_min;
        int new_mins;

        string s;

        getline(cin, s);

        for (int i = 0 ; i < S ; ++i)
        {
            getline(cin, s);
            engines.insert(make_pair(s, 0));
        }

        cin >> Q;
        getline(cin, s);

        while (Q--)
        {
            string s;
            getline(cin, s);

            new_min = min;
            new_mins = mins;

            for (map<string, int>::iterator i(engines.begin()), i_end(engines.end()) ; i != i_end ; ++i)
            {
                if (s == i->first)
                {
                    if (min == i->second)
                    {
                        if (mins == 1)
                            ++(i->second);
                        ++(i->second);
                        --new_mins;
                    }
                }
            }
            if (new_mins == 0)
            {
                ++new_min;
                new_mins = S - 1;
            }

            min = new_min;
            mins = new_mins;
            //cout << "Query: " << s << "\n";
            //cout << "    min " << min << " x " << mins << "\n";
            //for (map<string, int>::iterator i(engines.begin()), i_end(engines.end()) ; i != i_end ; ++i)
            //    cout << "    " << i->first << ": " << i->second << "\n";
        }
        cout << "Case #" << n + 1 << ": " << min << "\n";
    }

    return 0;
}
