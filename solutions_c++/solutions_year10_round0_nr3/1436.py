#include <iostream>
#include <map>
#include <deque>
#include <vector>

using namespace std;


template<class T> int cSize(const T& c) // returns the size of a container as an int
{
    return (int)c.size();
}




void solveC(int nCaseNo, int R, int k, const deque<int>& g)
{
    deque<int> vCrtQueue (g);
    vector<pair<deque<int>, int> > vAllQueues; // <queue, money made for that queue>
    map<deque<int>, int> mAllQueues; // "value" is position in vAllQueues
    int nRepeatPos (-1);
    while (0 == mAllQueues.count(vCrtQueue))
    {
        int nCrtPeople (0);

        for (int i = 0; i < cSize(vCrtQueue); ++i)
        {
            int nCrtGrp (vCrtQueue[i]);
            if (nCrtPeople + nCrtGrp <= k)
            {
                nCrtPeople += nCrtGrp;
            }
            else
            { // crt group doesn't fit; closing
                vAllQueues.push_back(make_pair(vCrtQueue, nCrtPeople));
                mAllQueues[vCrtQueue] = cSize(vAllQueues) - 1;

                vCrtQueue.insert(vCrtQueue.end(), vCrtQueue.begin(), vCrtQueue.begin() + i);
                vCrtQueue.erase(vCrtQueue.begin(), vCrtQueue.begin() + i);
                goto e1;
            }
        }

        // everybody could fit
        vAllQueues.push_back(make_pair(vCrtQueue, nCrtPeople));
        mAllQueues[vCrtQueue] = cSize(vAllQueues) - 1;

    e1:
        ;
    }

    // we have a repeat in vCrtQueue; need to know where the period begins
    int nPerBegin (mAllQueues[vCrtQueue]);
    int nPerSize (cSize(vAllQueues) - nPerBegin);
    long long nPerMoney (0); // money made in a full period
    for (int i = nPerBegin; i < cSize(vAllQueues); ++i)
    {
        nPerMoney += vAllQueues[i].second;
    }

    long long nTotalMoney (0);

    for (int i = 0; i < nPerBegin && R > 0; ++i, --R)
    {
        nTotalMoney += vAllQueues[i].second;
    }

    nTotalMoney += nPerMoney*(R/nPerSize);
    for (int i = 0; i < R%nPerSize; ++i)
    {
        nTotalMoney += vAllQueues[nPerBegin + i].second;
    }

    cout << "Case #" << nCaseNo << ": " << nTotalMoney << endl;
}



int main()
{
    int t, R, k, N, g;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        cin >> R >> k >> N;
        deque<int> v;
        for (int j = 0; j < N; ++j)
        {
            cin >> g;
            v.push_back(g);
        }
        solveC(i, R, k, v);
    }
}

