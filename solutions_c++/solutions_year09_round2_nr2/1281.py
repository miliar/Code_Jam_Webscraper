#include <algorithm>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;


void RunTestCase(int index)
{
    int i;
    int N;
    cin >> N;

    vector<int> v;

    while (N > 0)
    {
        v.push_back(N % 10);
        N /= 10;
    }

    for (i=0; i<20; ++i)
    {
        v.push_back(0);
    }

    reverse(v.begin(), v.end());
    next_permutation(v.begin(), v.end());

    //copy(v.begin(), v.end(), ostream_iterator<int>(cout, " "));
    //cout << endl;

    cout << "Case #" << (index + 1) << ": ";

    for (i=0; i<v.size(); ++i)
    {
        if (v[i] != 0)
        {
            break;
        }
    }

    for (; i<v.size(); ++i)
    {
        cout << v[i];
    }

    cout << endl;
}


int main()
{
    int T;

    cin >> T;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int i=0; i<T; ++i)
    {
        RunTestCase(i);
    }
}
