#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>

#include <boost/bind.hpp>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int n = 0; n < T; ++n)
    {
        string s;
        cin >> s;

        if (!next_permutation(s.begin(), s.end()))
        {
            sort(s.begin(), s.end());            
            s.insert(s.begin() + 1, '0');

            if ( s[0] == '0' )
            {
                int k = 1;
                while(s[k] == '0')
                    ++k;

                swap(s[0], s[k]);
            }
        }

        cout << "Case #" << (n + 1) << ": " << s << "\n";
    }   
}

