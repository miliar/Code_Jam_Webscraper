#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <assert.h>

using namespace std;

string problem = "C";

int group[1000];
struct Round
{
    Round() : idx(0), len(0), cost(0)
    {}

    int idx;
    int len;
    int cost;
};
Round rounds[1000];

bool proc(Round rounds[], int group[], int N, int limit, 
          long long& roundNum1, long long& cost1,
          long long& roundNum2, long long& cost2, 
          int& repeatIdx,
          int R)
{
    vector<bool> flags(N, false);
    int i;
    for (i = 0; i < N; ++i)
    {
        rounds[i].idx = i;
        rounds[i].len = 0;
        rounds[i].cost = 0;
    }

    i = 0;
    while (!flags[i])
    {
        int j = i;
        while (rounds[i].cost < limit)
        {
            if (rounds[i].cost + group[j] <= limit)
            {
                rounds[i].cost += group[j];
                rounds[i].len ++;
                j = (j + 1) % N;
                if (j == i) break;
            }
            else break;
        }
        flags[i] = true;
        i = j;
    }

    repeatIdx = i;
    int j = rounds[0].idx;
    roundNum1 = 0;
    cost1 = 0;
    while (j != i)
    {
        roundNum1++;
        cost1 += rounds[j].cost;

        if (roundNum1 == R) return true;
        j = (rounds[j].idx + rounds[j].len) % N;
        assert(flags[j]);
    }

    roundNum2 = 1;
    cost2 = rounds[j].cost;
    j = (rounds[j].idx + rounds[j].len) % N;
    while (j != i)
    {
        roundNum2++;
        cost2 += rounds[j].cost;
        j = (rounds[j].idx + rounds[j].len) % N;
        assert(flags[j]);
    }
    return false;
}

int main(int argc, char** argv)
{
    if (argc == 2)
    {
        problem = argv[1];
        string last3 = problem.substr(problem.size() - 3, 3);
        if (last3 == ".in")
            problem = problem.substr(0, problem.size() - 3);
    }

    string inPath = problem + ".in";
    string outPath = problem + ".out";

    cout << "doing " << inPath << endl;
    cout << "to    " << outPath << endl;
    
    freopen(inPath.data(), "r", stdin);
    freopen(outPath.data(), "w", stdout);

    int Ti,T;
    cin >> T;

    int i,j;

    for (Ti = 0; Ti < T; ++Ti)
    {
        // if (Ti != 33) continue;
        int R,k,N;
        cin >> R >> k >> N;
        for (i = 0; i < N; ++i) 
            cin >> group[i];

        long long total = 0;

        long long roundNum1, roundNum2;
        long long cost1, cost2;
        int repeatIdx;
        bool ret = proc(rounds, group, N, k, roundNum1, cost1,
                        roundNum2, cost2, repeatIdx, R);

        if (ret) total = cost1;
        else
        {
            // cout << "roundNum1,cost1 , roundNum2,cost2 = " 
            //      << roundNum1 << "," << cost1 << "," << roundNum2 << "," << cost2 << endl;

            total = cost1;
            R -= roundNum1;
            int leftRound = R % roundNum2;
            int repeat = R / roundNum2;
            total += (long long)repeat  * (long long)cost2;
            
            int j = repeatIdx;
            for (i = 0; i < leftRound; ++i)
            {
                total += rounds[j].cost;
                j = (rounds[j].idx + rounds[j].len) % N;                
            }
        }
        
        cout << "Case #" << Ti+1 << ": " << total << endl;
    }
    return 0;
}
