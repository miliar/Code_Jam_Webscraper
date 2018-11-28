#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <utility>

using namespace std;

int main()
{
    int numTests = 0;
    cin >> numTests;
    for (int test = 1; test <= numTests; ++test)
    {
        size_t numCandies = 0;
        cin >> numCandies;
        vector<int> v(numCandies);
        for (size_t i = 0; i < numCandies; ++i)
            cin >> v[i];
        sort(v.begin(), v.end());

        int answer = -1;
        for (size_t i = 1; i < numCandies; ++i)
        {
            int s1 = 0, s2 = 0, curV1 = 0, curV2 = 0;
            for (size_t j = 0; j < i; ++j)
            {
                curV1 += v[j];
                s1 = s1 ^ v[j];
            }
            for (size_t j = i; j < numCandies; ++j)
            {
                curV2 += v[j];
                s2 = s2 ^ v[j];
            }
            
            if (s1 == s2)
                answer = max(answer, max(curV1, curV2));
        }

        string answerStr;
        if (answer == -1)
            answerStr = "NO";
        else
        {
            stringstream ss;
            ss << answer;
            answerStr = ss.str();
        }
        cout << "Case #" << test << ": " << answerStr << endl;
    }

    return 0;
}
