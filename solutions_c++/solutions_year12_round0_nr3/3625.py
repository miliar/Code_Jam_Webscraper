////////////////////////////////////////////////////////////////////////////////
// ProblemC.cc
////////////////////////////////////////////////////////////////////////////////
/*! @file
//        Solves Google Code Jam 2012 Qualifying Round Problem C
*/ 
//  Author:  Julian Panetta (jpanetta), julian.panetta@gmail.com
//  Company:  New York University
//  Created:  04/14/2012 17:43:19
////////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <sstream>
#include <string>
#include <tr1/unordered_map>
#include <list>
#include <vector>
#include <cassert>

using namespace std;
using namespace std::tr1;

unsigned int computeKey(const string &str)
{
    vector<int> freq(10, 0);
    for (unsigned int i = 0; i < str.length(); ++i) {
        int digit = str[i] - '0';
        assert((digit >= 0) && (digit < 10));
        ++freq[digit];
    }

    unsigned int result = 0;
    for (unsigned int i = 0; i < 10; ++i) {
        assert(freq[i] < 8);
        result |= freq[i] << (3 * i);
    }

    return result;
}

bool isCycle(const string &a, const string &b)
{
    assert(a.length() == b.length());

    unsigned int len = a.length();
    bool foundCycle = false;

    for (unsigned int offset = 1; offset < len; ++offset) {
        foundCycle = true;
        for (unsigned int i = 0; i < len; ++i) {
            if (a[(offset + i) % len] != b[i])
                foundCycle = false;
        }
        if (foundCycle) break;
    }

    // No leading 0s...
    assert((a[0] != '0') && (b[0] != '0'));
    assert(atoi(a.c_str()) < atoi(b.c_str()));

    return foundCycle;
}

////////////////////////////////////////////////////////////////////////////////
/*! Program entry point
//  @param[in]  argc    Number of arguments
//  @param[in]  argv    Argument strings
//  @return     status  (0 on sucess)
*///////////////////////////////////////////////////////////////////////////////
int main(int argc, const char *argv[])
{
    int T; cin >> T;
    for (int test = 1; test <= T; ++test)  {
        int A, B;
        cin >> A >> B;

        // Hash based on digit frequency historgram
        typedef list<string> strlist;
        typedef unordered_map<unsigned int, strlist> Hashtable;
        typedef Hashtable::iterator Hit;
        Hashtable hashtable;

        // Insert all numbers into the hashtable, which maps digit frequency to
        // a list of strings with that digit frequency (in increasing order)
        for (int i = A; i <= B; ++i) {
            stringstream ss;
            ss << i;
            string digits = ss.str();
            unsigned int key = computeKey(digits);
            Hit loc = hashtable.find(key);
            if (loc == hashtable.end())
                loc = (hashtable.insert(make_pair(key, strlist()))).first;
            loc->second.push_back(digits);
        }

        unsigned int recycledPairs = 0;
        for (Hit it = hashtable.begin(); it != hashtable.end(); ++it) {
            strlist &dList = (it->second);
            for (strlist::iterator first = dList.begin(); first != dList.end();
                    ++first) {
                strlist::iterator second = first;
                for (++second; second != dList.end(); ++second) {
                    if (isCycle(*first, *second)) {
                        ++recycledPairs;
                    }
                }
            }
        }

        cout << "Case #" << test << ": " << recycledPairs << endl;
    }

    return 0;
}
