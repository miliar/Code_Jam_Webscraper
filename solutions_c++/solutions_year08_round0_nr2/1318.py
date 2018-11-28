#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

void get_times(int n, vector<pair<int, int> > &stationA, vector<pair<int, int> > &stationB, int turnaround)
{
    while (n--)
    {
        int hour, minutes;
        scanf("%d:%d", &hour, &minutes);        //departure time
        stationA.push_back(make_pair(60 * hour + minutes, 1));

        scanf("%d:%d", &hour, &minutes);        //arrival time
        stationB.push_back(make_pair(60 * hour + minutes + turnaround, 0));
    }
}

int count(vector<pair<int, int> > &station)
{
    int c = 0, need = 0;
    for (int i = 0; i < station.size(); ++i)
    {
        if (station[i].second == 0)        //new train
            ++c;
        else                                //arrive
            --c;

        if (-c > need)
            need = -c;
    }
    return need;
}


int main()
{
    int T;
    scanf("%d" ,&T);
    for (int t = 1; t <= T; ++t)
    {
        int turnaround;
        int na, nb;
        vector<pair<int,int> > stationA, stationB;

        scanf("%d", &turnaround);
        scanf("%d %d", &na, &nb);
        get_times(na, stationA, stationB, turnaround);
        get_times(nb, stationB, stationA, turnaround);
        sort(stationA.begin(), stationA.end());
        sort(stationB.begin(), stationB.end());
        printf("Case #%d: %d %d\n", t, count(stationA), count(stationB));
    }
    return 0;
}

