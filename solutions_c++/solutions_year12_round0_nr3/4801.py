#include <iostream>
#include <cassert>
#include <string>
#include <sstream>

using namespace std;

string toString(int i)
{
    ostringstream o;
    o << i;
    return o.str();
}

bool isRecycled(int i, int j)
{
    if (i == j)
        return false;

    string s1 = toString(i);
    string s2 = toString(j);

//     cout << s1 << "  " << s2 << "     " << s1 + s1 << endl;

    return (s1 + s1).find(s2) != string::npos;
}

int main()
{
    int numCases;
    cin >> numCases;

    for (int testCase = 1; testCase <= numCases; testCase++)
    {
        int a, b;
        cin >> a >> b;

        int answer = 0;

        for (int i = a; i <= b; i++)
        {
            for (int j = a; j < i; j++)
            {
                if (isRecycled(i, j))
                    answer++;
            }
        }

        cout << "Case #" << testCase << ": " << answer << endl;
    }

    return 0;
}
