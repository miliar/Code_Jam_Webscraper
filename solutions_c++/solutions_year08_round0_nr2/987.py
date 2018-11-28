#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <numeric>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <iomanip>
using namespace std;
const double EPS = 1.0e-9;

int getDateInt(string s)
{
    return ((s[0]-'0')*10+(s[1]-'0'))*60 + ((s[3]-'0')*10+(s[4]-'0'));
}

struct schedule {
    int leave, arrive;
    schedule(int _leave, int _arrive) : 
        leave(_leave), arrive(_arrive) {}
};

bool compSchedule(const schedule& x, const schedule& y)
{
    if (x.leave < y.leave) 
        return true;
    else if (x.leave > y.leave)
        return false;
    else {
        if (x.arrive < y.arrive)
            return true;
        else
            return false;
    }
}

int main(void)
{
    int N, turnaround, NA, NB;
    string dateLeave, dateArrive;
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> turnaround >> NA >> NB;
        vector<schedule> waitA, waitB;

        for (int j = 0; j < NA; j++) {
            cin >> dateLeave >> dateArrive;
            waitA.push_back(schedule(getDateInt(dateLeave),
                                     getDateInt(dateArrive)));
        }
        for (int j = 0; j < NB; j++) {
            cin >> dateLeave >> dateArrive;
            waitB.push_back(schedule(getDateInt(dateLeave),
                                     getDateInt(dateArrive)));
        }
        sort(waitA.begin(), waitA.end(), compSchedule);
        sort(waitB.begin(), waitB.end(), compSchedule);

        int numA=0, numB=0;
        int idxA=0, idxB=0;
        int numWaitA=0, numWaitB=0;
        vector<int> runA, runB;
        for (int time = 0; time < 60*24; time++) {
            for (int j = 0; j < runA.size(); j++)
                if (runA[j] == time)
                    numWaitB++;
            for (int j = 0; j < runB.size(); j++)
                if (runB[j] == time)
                    numWaitA++;
            while (idxA < NA && waitA[idxA].leave == time) {
                if (numWaitA > 0) 
                    numWaitA--;
                else 
                    numA++;
                runA.push_back(waitA[idxA].arrive+turnaround);
                idxA++;
            }
            while (idxB < NB && waitB[idxB].leave == time) {
                if (numWaitB > 0)
                    numWaitB--;
                else
                    numB++;
                runB.push_back(waitB[idxB].arrive+turnaround);
                idxB++;
            }
        }

        cout << "Case #" << (i+1) << ": " << numA << " " << numB << endl;
    }

    return 0;
}

