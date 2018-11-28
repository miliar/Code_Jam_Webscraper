/*
 * TrainTimetable.cpp
 *
 *  Created on: 17/Jul/2008
 *      Author: Joao Azevedo (joao.c.azevedo@gmail.com)
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Trip
{
    int from;
    int depTime;
    int arrTime;

    bool operator < (const Trip & t) const
    {
        return depTime < t.depTime;
    }
};

int main()
{
    int C;
    cin >> C;
    for (int i = 0; i < C; i++)
    {
        int T, N[2];
        int trains[2][24*60];
        memset(trains, 0, sizeof(trains));
        cin >> T;
        cin >> N[0] >> N[1];
        vector<Trip> trips;
        for (int k = 0; k <= 1; k++)
        {
            for (int j = 0; j < N[k]; j++)
            {
                int hd, md, ha, ma;
                scanf("%d:%d %d:%d", &hd, &md, &ha, &ma);
                Trip t;
                t.from = k;
                t.depTime = hd*60+md;
                t.arrTime = ha*60+ma;
                trips.push_back(t);
            }
        }
        sort(trips.begin(), trips.end());
        int D[2] = {0, 0};
        for (size_t j = 0; j < trips.size(); j++)
        {
            if (trains[trips[j].from][trips[j].depTime] <= 0)
                D[trips[j].from]++;
            else
                for (int k = trips[j].depTime; k < 24*60; k++)
                    trains[trips[j].from][k]--;
            for (int k = trips[j].arrTime+T; k < 24*60; k++)
                trains[trips[j].from^1][k]++;
        }
        cout << "Case #" << i+1 << ": " << D[0] << " " << D[1] << endl;
    }
    return 0;
}
