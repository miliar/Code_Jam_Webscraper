#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <algorithm>
using namespace std;

int main(int argc, char **argv)
{
    ifstream fin(argv[1]);
    ofstream fout("output.txt");
    int T;
    fin>>T;
    for(int ii = 1; ii <= T; ii++)
    {

        int N,C,L;
        long long t;
        fin>>L>>t>>N>>C;
        int dis[1002];
        for(int i = 0; i < C; i++)
        {
            fin>>dis[i];
        }
        vector<int> gaps;
        for(int i = 0; i < N; i++)
        {
            gaps.push_back(dis[i%C]*2);
        }
        long long time = 0;
        for(int i = 0; i < N; i++)
        {
            if(time + gaps[i] > t)
            {
                int left = time+gaps[i] -t;
                gaps[i] = left;
                time = t;
                sort(gaps.begin(), gaps.end());
                reverse(gaps.begin(), gaps.end());
                for(int j = 0; j < gaps.size(); j++)
                {
                    if(j < L)
                    {
                        time+=(gaps[j]/2);
                    }
                    else
                    {
                        time+=gaps[j];
                    }
                }
                break;
            }
            else
            {
                time+=gaps[i];
                gaps[i] = 0;
            }
        }
        fout<<"Case #"<<ii<<": "<<time<<endl;
    }
    return 0;
}
