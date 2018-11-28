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
        int L, t, N, C;
        scanf("%d %d %d %d",&L, &t, &N, &C);
        vector<int> given_distances;
        for(int i = 0; i < C; ++i)
        {
            int d;
            scanf("%d", &d);
            given_distances.push_back(d);
        }
        
        vector<int> actual_distances;
        for(int i = 0; i < N; ++i)
            actual_distances.push_back(2*given_distances[i%C]);
        
        /**
        vector< pair<int, int> > dists;
        for(int i = 0; i < N; ++i)
            dists.push_back(make_pair(actual_distances[i], i));
        sort(dists.begin(), dists.end());
        **/
        
        double ans = 100000000LL;
        if(L >= 0)
        {
            double c_ans = 0;
            for(int i = 0; i < N; ++i)
                c_ans += actual_distances[i];
            
            ans = min(ans, c_ans);
        }
        if(L >= 1)
        {
            for(int k = 0; k < N; ++k)
            {
                double c_ans = 0;
                
                for(int i = 0; i < N; ++i)
                {
                    if(i == k)
                    {
                        /// At the star where we built the thing
                        if(c_ans < t)
                        {
                            double time_to_completion = t - c_ans;
                            double time_spent = time_to_completion + (actual_distances[i] - time_to_completion)/2;
                            c_ans += time_spent;
                        }
                        else
                        {
                            c_ans += actual_distances[i]/2;
                        }
                    }
                    else
                    {
                        c_ans += actual_distances[i];
                    }
                }
                
                ans = min(ans, c_ans);
            }
        }
        
        if(L >= 2)
        {
            for(int k = 0; k < N; ++k)
            {
                for(int j = k + 1; j < N; ++j)
                {
                    double c_ans = 0;
                    
                    for(int i = 0; i < N; ++i)
                    {
                        if(i == k || i == j)
                        {
                            /// At the star where we built the thing
                            if(c_ans < t)
                            {
                                double time_to_completion = t - c_ans;
                                double time_spent = time_to_completion + (actual_distances[i] - time_to_completion)/2;
                                c_ans += time_spent;
                            }
                            else
                            {
                                c_ans += actual_distances[i]/2;
                            }
                        }
                        else
                        {
                            c_ans += actual_distances[i];
                        }
                    }
                    
                    ans = min(ans, c_ans);
                }
            }
        }
        
        printf("Case #%d: %lld\n", _, (long long)ans);
    }
    
    return 0;
}