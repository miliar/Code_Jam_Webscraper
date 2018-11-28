//============================================================================
// Name        : cj_1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int main() {
	int cnt = 0;
	cin >> cnt;

    for(int i = 0 ; i < cnt; ++i)
    {
        unsigned g, s, p;
        unsigned sure = 0;
        unsigned poss = 0;

        cin >> g >> s >> p;
        // Load results
        for(unsigned gi = 0; gi < g; ++gi)
        {
            unsigned tmp;
            cin >> tmp;

            unsigned avg = tmp/3;
            unsigned rest = tmp%3;

            if(avg >= p || (avg == (p-1) && rest > 0))
            {
                ++sure;
            }else
            {
                if(tmp >= 2 && ((avg == (p-1) && rest == 0) || (avg == (p-2) && rest == 2)))
                {
                    ++poss;
                }
            }
        }

        cout << "Case #" << (i+1) << ": " << (sure + min(poss, s)) << endl;
    }

	return 0;
}
