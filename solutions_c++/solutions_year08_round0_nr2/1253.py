// Problem 2: Train time table

#include <algorithm>
#include <set>
#include <iostream>
#include <vector>
#include <utility>
#include <set>

using namespace std;

typedef  unsigned int Uint;
typedef  pair<unsigned int, unsigned int>   ResultPair;


struct Schedule {
    int stn;
    Uint dh, dm, ah, am;
    Schedule (int stn, Uint dh, Uint dm, Uint ah, Uint am)
    {
        this->stn = stn;
        this->dh = dh;
        this->dm = dm;
        this->ah = ah;
        this->am = am;
    }
};


bool
TimeTableLT (const Schedule& sch1, const Schedule& sch2) {
    if (sch1.dh < sch2.dh)
        return true;
    
    if (sch1.dh > sch2.dh)
        return false;
    
    if (sch1.dm < sch2.dm)
        return true;
    
    if (sch1.dm > sch2.dm)
        return false;

    return sch1.stn < sch2.stn;
}


bool
operator< (const ResultPair& res1, const ResultPair& res2)  {
    if (res1.first < res2.first)
        return true;
    
    if (res1.first > res2.first)
        return false;

    return res1.second < res2.second;
}


bool
BetweenTimes (Uint dh, Uint dm, Uint asdh, Uint asdm, Uint aedh, Uint aedm) {
    if (asdh < dh)
        return true;
    if (asdh > dh)
        return false;
    return asdm <= dm;
}


ResultPair
FindNumTrainsAtStns()
{
    vector<Schedule>  timeTable;

    char line[101];
    Uint tat;
    Uint ab;
    Uint ba;
   
    Uint dh, dm, ah, am;
    
    cin >> tat;
    cin.getline(line, 101);
    
    cin >> ab;
    cin >> ba;
    cin.getline(line, 101);

    for (Uint i = 0; i < ab; ++i) {
        cin.getline(line, 101);
        sscanf(line, "%u:%u %u:%u", &dh, &dm, &ah, &am);
        if ((am + tat) >= 60)
            ++ah;
        am = (am + tat) % 60;
        timeTable.push_back(Schedule(0, dh, dm, ah, am));
    }
    
    for (Uint i = 0; i < ba; ++i) {
        cin.getline(line, 101);
        sscanf(line, "%u:%u %u:%u", &dh, &dm, &ah, &am);
        if ((am + tat) >= 60)
            ++ah;
        am = (am + tat) % 60;
        timeTable.push_back(Schedule(1, dh, dm, ah, am));
    }
   
    sort(timeTable.begin(), timeTable.end(), TimeTableLT);

    Uint na = 0;
    Uint nb = 0;

    multiset<ResultPair>  waitingA;
    multiset<ResultPair>  waitingB;

    vector<Schedule>::iterator  begin = timeTable.begin();
    vector<Schedule>::iterator  end   = timeTable.end();
    for ( ; begin != end; ++begin) {
        if (begin->stn == 0) {
            if (waitingA.empty()) {
                ++na;
            } else {
                if (BetweenTimes(begin->dh, begin->dm, waitingA.begin()->first, 
                                                       waitingA.begin()->second,
                                                       waitingA.rbegin()->first,
                                                       waitingA.rbegin()->second))
                    waitingA.erase(waitingA.begin());
                else
                    ++na;
            }
            waitingB.insert(ResultPair(begin->ah, begin->am)); 
        }

        if (begin->stn == 1) {
            if (waitingB.empty()) {
                ++nb;
            } else {
                if (BetweenTimes(begin->dh, begin->dm, waitingB.begin()->first, 
                                                       waitingB.begin()->second,
                                                       waitingB.rbegin()->first,
                                                       waitingB.rbegin()->second))
                    waitingB.erase(waitingB.begin());
                else
                    ++nb;
            }
            waitingA.insert(ResultPair(begin->ah, begin->am)); 
        }
    }
    
    return ResultPair(na, nb);
}


int 
main()
{
    int numSequences;
    cin >> numSequences;
    for (size_t i = 0; i < numSequences; ++i) { 
        ResultPair  numTrains = FindNumTrainsAtStns();
        cout << "Case #" << i + 1 << ": " << numTrains.first << " " 
                                          << numTrains.second << endl;
    }
}
