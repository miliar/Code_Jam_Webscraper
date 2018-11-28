#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

struct Way
{
    int start;
    int end;
    int speed;
    bool operator<(const Way& o) const
    {
        if (speed != o.speed)
            return speed < o.speed;
        else if (start != o.start)
            return start < o.start;
        else
            return end < o.end;
    }
};

int T, X;
double S, R, N, t;
int B, E, w;
vector<Way> walkway;

int main()
{
    ifstream in("A.in");
    ofstream out("A.out");
    out << setprecision(12);
    
    in >> T;
    for (int tc = 1; tc <= T; ++tc)
    {
        in >> X >> S >> R >> t >> N;
        walkway.clear();
        int loc = 0;
        
        for (int i = 0; i < N; ++i)
        {
            in >> B >> E >> w;
            Way way1, way2;
            way1.start = loc;
            way1.end = B;
            way1.speed = 0;
            way2.start = B;
            way2.end = E;
            way2.speed = w;
            walkway.push_back(way1);
            walkway.push_back(way2);
            loc = E;
        }
        Way way;
        way.start = loc;
        way.end = X;
        way.speed = 0;
        walkway.push_back(way);
        
        sort(walkway.begin(), walkway.end());
        double ans = 0.0, dt = 0.0;
        
        for (int i = 0; i < walkway.size(); ++i)
        {
            if (walkway[i].start >= walkway[i].end)
                continue;
            if (t <= 0)
            {
                dt = (walkway[i].end - walkway[i].start)/(S + walkway[i].speed);
                ans += dt;
            }
            else if ((R + walkway[i].speed)*t >= walkway[i].end - walkway[i].start)
            {
                dt = (walkway[i].end - walkway[i].start)/(R + walkway[i].speed);
                t -= dt;
                ans += dt;
            }
            else
            {
                dt = t + (walkway[i].end - walkway[i].start - (R + walkway[i].speed)*t)/(S + walkway[i].speed);
                t = 0;
                ans += dt;
            }
        }
        
        out << "Case #" << tc << ": " << ans << endl;
    }
}
