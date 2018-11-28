#include<fstream>
#include<iostream>
#include<vector>
#include<iomanip>
#include<algorithm>
#include<math.h>

using namespace std;

ifstream in("B-large.in");
ofstream out("output.txt");

int T;

int main()
{
    in >> T;
    for(int test = 0; test < T; test++)
    {
        long long L, N, C;
        long long t;
        in >> L >> t >> N >> C;
        vector<long long> stars(N);
        vector<long long> sum(N + 1);
        vector<long long> dists(C);
        long long nospeed = 0;
        for(int i = 0; i < C; i++)
            in >> dists[i];
        for(int i = 0; i < N; i++)
        {
            stars[i] = dists[i % C];
            nospeed += stars[i] * 2;
        }
        sum[0] = 0;
        for(int i = 1; i <= N; i++)
            sum[i] = sum[i - 1] + stars[i - 1];

        long long minspeed = nospeed;
        int current_star = (lower_bound(sum.begin(), sum.end(), t/2) - sum.begin());
        if(sum[current_star] > t/2)
            current_star--;

        long long to_next_star = sum[current_star + 1] - t/2;
        vector<long long> calcdist(1, to_next_star);
        for(int i = current_star + 1; i < N; i++)
            calcdist.push_back(stars[i]);
        sort(calcdist.rbegin(), calcdist.rend());
        for(int i = 0; (i < L && i < calcdist.size()); i++)
            minspeed -= calcdist[i];

        /*cout << "sum = [ ";
        for(int i = 0; i < sum.size(); i++)
            cout << sum[i] << " ";
        cout << "]" << endl;*/
        cout << "Current star is " << current_star << endl;
        /*if(L == 1)
        {
            for(int p1 = 0; p1 < N; p1++)
            {
                long long nspeed = nospeed;
                if(current_star == p1)
                    nspeed = nspeed - stars[current_star]*2 + (t/2 - sum[current_star])*2 + (sum[current_star + 1] - t/2);
                else if(current_star < p1)
                    nspeed = nspeed - stars[p1];
                minspeed = min(minspeed, nspeed);
            }
        }
        else if(L == 2)
        {
            cout << "L = 2" << endl;
            for(int p1 = 0; p1 < N; p1++)
                for(int p2 = 0; p2 < N; p2++)
                if(p1 != p2)
                {
                    long long nspeed = nospeed;
                    if(current_star == p1)
                        nspeed = nspeed - stars[current_star]*2 + (t/2 - sum[current_star])*2 + (sum[current_star + 1] - t/2);
                    else if(current_star < p1)
                        nspeed = nspeed - stars[p1];

                    if(current_star == p2)
                        nspeed = nspeed - stars[current_star]*2 + (t/2 - sum[current_star])*2 + (sum[current_star + 1] - t/2);
                    else if(current_star < p2)
                        nspeed = nspeed - stars[p2];
                    minspeed = min(minspeed, nspeed);
                }
        }*/
        out << "Case #" << (test + 1) << ": " << minspeed << endl;
    }
    return 0;
}
