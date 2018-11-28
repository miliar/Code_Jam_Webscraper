#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void genSubsets(vector<int> tmp, vector<int> &input, size_t start, int sum, vector<vector<int> >& results, vector<int> &sums)
{
    if(start >= input.size())
    {
        results.push_back(tmp);
        sums.push_back(sum);
        return;
    }
    genSubsets(tmp, input, start + 1, sum, results, sums);
    tmp.push_back(input[start]);
    genSubsets(tmp, input, start + 1, sum + input[start], results, sums);
}

void echoVec(vector<int> &a)
{
    for(size_t i = 0; i < a.size(); ++i)
    {
        cout << a[i] << " ";
    }
}

int main()
{
    int cnt = 0;
    cin >> cnt;

    for (int i = 0; i < cnt; ++i)
    {
        int liczb = 0;
        cin >> liczb;

        vector<int> zbior;
        long sume = 0;

        for (int j = 0; j < liczb; ++j)
        {
            int tmp = 0;
            cin >> tmp;
            sume += tmp;
            zbior.push_back(tmp);
        }

        vector<int> starter;
        vector<int> sums;
        vector<vector<int> > ress;
        genSubsets(starter, zbior, 0, 0, ress, sums);


        cout << "Case #" << (i + 1) << ":" << endl;

        bool done = false;
        for(size_t a = 0; a < sums.size(); ++a)
        {
            for(size_t b = a + 1; b < sums.size(); ++b)
            {
                if(sums[a] == sums[b])
                {
                    echoVec(ress[a]);
                    cout << endl;
                    echoVec(ress[b]);
                    done = true;
                    break;
                }
            }
            if(done)
            {
                break;
            }
        }
        if(!done)
        {
            cout << "Impossible";
        }
        cout << endl;
    }
    return 0;
}
