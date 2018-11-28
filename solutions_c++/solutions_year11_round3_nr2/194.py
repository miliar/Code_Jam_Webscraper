#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class dist_t
{
    public:
    int dist;
    int effDist;

    bool operator<(const dist_t& rhs) const;
};

bool dist_t::operator<(const dist_t& rhs) const
{
    return this->effDist < rhs.effDist; 
}

int main()
{
    int T;
    cin >> T;

    for(int caseIndex = 0; caseIndex < T; caseIndex ++)
    {
        cout << "Case #" << caseIndex + 1 << ": ";

        int L, N, C;
        unsigned long long t;


        cin >> L >> t >> N >> C;

        vector<int> a(C);

        for(int i = 0; i < C; i ++)
            cin >> a[i];

        vector<dist_t> d(N);
        
        for(int i = 0; i < N; i ++)
        {
            int j = i % C;
            // distance from Star i to Star i + 1
            d[i].dist = a[j];
        }

        unsigned long long buildDist = t >> 1;

        unsigned long long sumDist = 0;
        bool found = false;
        for(int i = 0; i < N; i ++)
        {
            if(found == false)
                sumDist += d[i].dist;
            
            if(sumDist < buildDist)
                d[i].effDist = 0;
            else if(found == false)
            {
                d[i].effDist = (sumDist - buildDist);
                found = true;
            }
            else
                d[i].effDist = d[i].dist;
        }

        sort(d.begin(), d.end());
        unsigned long long timecost = 0;
        for(int i = N - 1; i >= 0; i --)
        {
            if(L > 0)
            {
                if(d[i].effDist == d[i].dist)
                {
                    timecost += d[i].effDist;
                    L --;
                }
                else if(d[i].effDist > 0)
                {
                    timecost += d[i].effDist + ((d[i].dist - d[i].effDist) << 1);
                    L --;
                }
                else
                    timecost += (d[i].dist << 1);
            }
            else
                timecost += (d[i].dist << 1);
        }

        cout << timecost << endl;
    }
}
