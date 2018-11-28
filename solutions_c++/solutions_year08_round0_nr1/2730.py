#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>

using namespace std;

int main()
{
    int N, S, Q;

    string t;
    getline(cin, t);
    istringstream iss;
    iss.str(t);
    iss >> N;
    for (int j = 1; j <= N; j++)
    {
        vector<string> eng;
        vector<string> qs;

        getline(cin, t);
        iss.clear();
        iss.str(t);
        iss >> S;
    //cout << "!!! " << S << endl;
        for (int i = 0; i < S; i++) 
        {
            getline(cin, t);
            eng.push_back(t);
        }

        //for (int x = 0; x < eng.size(); x++)
        //    cout << "!@#!@#!  " << eng[x] << " __ ";
        //cout << endl;

        getline(cin, t);
        iss.clear();
        iss.str(t);
        iss >> Q;
        for (int i = 0; i < Q; i++)
        {
            getline(cin, t);
            qs.push_back(t);
        }
        
        int ans = 0;
        for (int pos = 0; pos < qs.size(); )
        {
            int best = 0;
            for (int e = 0; e < eng.size(); e++)
            {
                int k = pos;
                for (; k < qs.size(); k++)
                    if (eng[e] == qs[k])
                        break;
                best = max(best, k);
            }
            pos = best;
            if (pos != qs.size())
                ans++;
        }

        cout << "Case #" << j << ": " << ans << endl;
    }

    return 0;
}

