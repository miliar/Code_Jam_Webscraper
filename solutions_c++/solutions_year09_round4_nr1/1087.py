#include <iostream>
#include <string>

#include <cassert>

#include <vector>
#include <map>
#include <set>
#include <list>
#include <numeric>
#include <functional>

#include <algorithm>

#include <boost/bind.hpp>
#include <boost/shared_ptr.hpp>
#include <boost/algorithm/string.hpp>
#include <boost/lexical_cast.hpp>

using boost::bind;
using boost::shared_ptr;
using boost::lexical_cast;
using namespace boost::algorithm;

using namespace std;

typedef vector<string> strings;
typedef vector<int>    ints;

// ---------------------- HEADER -----------------------------

int main(int argc, char ** argv)
{
    if (argc > 1)
        freopen(argv[1], "r", stdin);
    
    if (argc > 2)
        freopen(argv[2], "w", stdout);

    vector<string> v;
    for (int i = 0; i != 10; ++i)
        v.push_back(lexical_cast<string>(i*i));

    int T;
    cin >> T;
    for (int caseN = 0; caseN != T; ++caseN)
    {
        int N ;
        cin >> N;

        ints m(N);
        for (int i =0; i!= N; ++i)
        {
            string s;
            cin >> s;
            m[i] = s.find_last_of("1");
        }

        int res = 0;

        for (int i = 0; i != N; ++i)
        {
            ints::iterator now = m.begin() + i;
            ints::iterator it = find_if(now, m.end(), bind(less<int>(), _1, i+1));
            res += it - now;
            int v = *it;
            m.erase(it);
            m.insert(now, v);
        }

        // place your code here =)

        cout << "Case #" << (caseN + 1) << ": " << res << "\n";
    }   
} 

