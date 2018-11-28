#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>

#include <boost/bind.hpp>

using namespace std;

const string W("welcome to code jam");

int main()
{
    string s;
    getline(cin, s);
    int N = strtol(s.c_str(), 0, 10 ); 

    for (int n = 0; n < N; ++n)
    {
        getline(cin, s);

        vector< int > v(W.size(), 0);

        for ( size_t i = 0; i != s.size(); ++i )
        {
            for ( size_t k = 0; k != W.size(); ++k )
            {
                if ( s.at(i) == W.at(k) )
                {
                    if (k == 0)
                        ++v[k];
                    else
                        v[k] = (v[k] + v.at(k - 1)) % 10000;
                }
            }
        }

        printf("Case #%d: %04d\n", n+1, v.back());
    }   
}

