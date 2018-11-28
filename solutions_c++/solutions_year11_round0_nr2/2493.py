#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;


#define DEBUGGING false

#define doubt if (DEBUGGING) cerr

#define foo(x) doubt << #x << ": " << x << endl;
#define loopfoo(x) for (int i2 = 0; i2 < x.size(); i2++) \
                          doubt << #x << "[" << i2 << "]: " << x[i2] << endl;
#define looploopfoo(x) for (int i2 = 0; i2 < x.size(); i2++) { \
                           for (int j2 = 0; j2 < x[i2].size(); j2++) \
                               doubt << '\t' << #x << "[" << i2 << "][" \
                                     << j2 << "]: " << x[i2][j2]; \
                           doubt << endl; }


int main(int argc, char** argv)
{
    int T;
    cin >> T;

    for (int caseNum = 1; caseNum <= T; caseNum++)
    {
        int C;
        cin >> C;

        vector<string> combiners(C);
        for (int i = 0; i < C; i++)
            cin >> combiners[i];

        int D;
        cin >> D;

        vector<string> bad(D);
        for (int i = 0; i < D; i++)
            cin >> bad[i];

        int N;
        cin >> N;

        vector<char> list;
        for (int j = 0; j < N; j++)
        {
            char c;
            cin >> c;
            list.push_back(c);
            int s = list.size()-1;

            if (list.size() <= 1)
                continue;

            for (int i = 0; i < C; i++)
            {
                if (list[s] == combiners[i][0] && list[s-1] == combiners[i][1] ||
                    list[s] == combiners[i][1] && list[s-1] == combiners[i][0])
                {
                    list.pop_back();
                    list[s-1] = combiners[i][2];
                    s--;
                    break;
                }
            }

            bool stop = list.size() <= 1;
            for (int i = 0; i < D && !stop; i++)
            {
                for (int k = 0; k < list.size()-1; k++)
                {
                    if (list[k] == bad[i][0] && list[s] == bad[i][1] ||
                        list[s] == bad[i][0] && list[k] == bad[i][1])
                    {
                        list.clear();
                        stop = true;
                        break;
                    }
                }
            }

            for (int i = 0; i < list.size(); i++)
            {
                if (i > 0)
                    doubt << ", ";
                doubt << list[i];
            }
            doubt << endl;
        }

        cout << "Case #" << caseNum << ": [";
        for (int i = 0; i < list.size(); i++)
        {
            if (i > 0)
                cout << ", ";
            cout << list[i];
        }
        cout << "]" << endl;
    }

    return 0;
}
