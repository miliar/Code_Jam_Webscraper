#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int main(int argc, char** argv)
{
    int T;
    scanf("%d", &T);
    
    for(int _ = 1; _ <= T; ++_)
    {
        int X, S, R, st, N;
        scanf("%d %d %d %d %d", &X, &S, &R, &st, &N);
        double t = st;
        
        vector< pair< int, pair<int, int> > > places;
        
        double length_remaining = X;
        double ans = 0;
        
        for(int i = 0; i < N; ++i)
        {
            int b, e, w;
            scanf("%d %d %d", &b, &e, &w);
            places.push_back(make_pair(w, make_pair(b, e)));
            length_remaining -= double(e - b);
        }
        places.push_back(make_pair(0, make_pair(0, (int)length_remaining)));
        sort(places.begin(), places.end());
//         reverse(places.begin(), places.end());
        double time_taken = 0;
        
        int i = 0;
        for(i = 0; i < places.size(); ++i)
        {
            double dist = places[i].second.second - places[i].second.first;
            double speed = places[i].first;
            
            double time_when_run = dist/(speed + R);
            
            if(time_when_run > t)
            {
                double d_ran = (speed + R)*t;
                double d_left = dist - d_ran;
                
                double total_time = t + d_left/(speed + S);
                
                ans += total_time;
                t = 0;
                ++i;
                break;
            }
            else
            {
                t -= time_when_run;
                ans += time_when_run;
            }
        }
        
//         printf("%lf\n", ans);
        
        while(i != places.size())
        {
            double dist = places[i].second.second - places[i].second.first;
            double speed = places[i].first;
            
            ans += (dist)/(speed + S);
            ++i;
        }
        /**
        double dist_ran = min(length_remaining, R*t);
        double dist_left = length_remaining - dist_ran;
        printf("FDFDDSFF %lf %lf %lf\n", length_remaining, dist_ran, dist_left);
        ans += (dist_ran)/double(R) + (dist_left)/double(S);
        **/
        printf("Case #%d: %lf\n", _, ans);
    }
    return 0;
}