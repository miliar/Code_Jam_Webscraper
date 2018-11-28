#include <iostream>
#include <vector>
#include <string>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

int N, S, Q;
vector<string> searchEngines;
vector<string> queries;

int search(int sidx, int qidx)
{
    if (qidx == Q) 
        return 0;

    if (searchEngines[sidx] == queries[qidx]) {
        int minCount = 10000;
        for (int i = 0; i < S; i++)
            if (searchEngines[i] != queries[qidx])
                minCount = min(minCount, search(i, qidx+1));
        return minCount + 1;
    } else
        return search(sidx, qidx+1);
}

int main(void)
{
    string line;
    getline(cin, line);
    istringstream(line) >> N;

    for (int i = 0; i < N; i++) {
        searchEngines.clear();
        queries.clear();
        getline(cin, line);
        istringstream(line) >> S;
        for (int j = 0; j < S; j++) {
            getline(cin, line);
            searchEngines.push_back(line);
        }
        getline(cin, line);
        istringstream(line) >> Q;
        for (int j = 0; j < Q; j++) {
            getline(cin, line);
            queries.push_back(line);
        }
        int minSwitch = 10000;
        int mins[105][1005];
        memset(mins, 0, sizeof(mins));
        for (int qidx = Q-1; qidx >= 0; qidx--) {
            for (int sidx = 0; sidx < S; sidx++) {
                if (searchEngines[sidx] == queries[qidx]) {
                    int tmpMin = 10000;
                    for (int j = 0; j < S; j++)
                        if (j != sidx)
                            tmpMin = min(tmpMin, mins[j][qidx+1]);
                    mins[sidx][qidx] = 1 + tmpMin;
                } else 
                    mins[sidx][qidx] = mins[sidx][qidx+1];
            }
        }
        for (int j = 0; j < S; j++)
            minSwitch = min(minSwitch, mins[j][0]);
        cout << "Case #" << (i+1) << ": " << minSwitch << endl;
    }
    return 0;
}

