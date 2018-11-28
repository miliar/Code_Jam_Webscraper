#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>


using namespace std;


//copy(sequence.begin(), sequence.end(), ostream_iterator<E>(cout, " "));
//cout << endl;


void RunTestCase(int testCaseIndex)
{
    string message;
    cin >> message;
    //cout << message << endl;

    map<char, int> m;
    int num = 0;

    m[message[0]] = 1;

    for (int i=1; i<message.size(); ++i)
    {
        if (m.find(message[i]) == m.end())
        {
            m[message[i]] = num;

            if (num == 0)
            {
                num = 2;
            }
            else
            {
                ++num;
            }
        }
    }

    //for (map<char, int>::iterator it=m.begin(); it!=m.end(); ++it)
    //{
        //cout << it->first << ": " << it->second << endl;
    //}

    long long base = 1;
    long long answer = 0;

    for (int i=message.size()-1; i>=0; --i)
    {
        answer += (base * m[message[i]]);

        if (m.size() == 1)
        {
            base *= 2;
        }
        else
        {
            base *= m.size();
        }
    }

    cout << "Case #" << (testCaseIndex + 1) << ": " << answer << endl;
}


int main()
{
    int N;

    cin >> N;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int testCaseIndex=0; testCaseIndex<N; ++testCaseIndex)
    {
        RunTestCase(testCaseIndex);
    }

    return 0;
}
