#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> swaps_required;
    int natural_speed[51];
    int start_position[51];
    int B;
    int T;
    int C, c;
    double natural_time[51];
    bool on_time[51];
    int N, K;
    int i, j;
    int temp;

    cin>>C;
    for(c=1; c<=C; c++)
    {
        cin>>N>>K>>B>>T;
        for(i=1; i<=N; i++)
            cin>>start_position[i];
        for(i=1; i<=N; i++)
            cin>>natural_speed[i];
        for(i=1; i<=N; i++)
            natural_time[i] = (double)(B-start_position[i])/(double)natural_speed[i];
        for(i=1; i<=N; i++)
            on_time[i] = natural_time[i]<=T;
        swaps_required.clear();
        for(i=1; i<=N; i++)
            if(on_time[i])
            {
                temp = 0;
                for(j=i+1; j<=N; j++)
                    if(!on_time[j])
                        temp++;
                swaps_required.push_back(temp);
            }
        sort(swaps_required.begin(), swaps_required.end());
        cout<<"Case #"<<c<<": ";
        if(swaps_required.size()<K)
            cout<<"IMPOSSIBLE"<<endl;
        else
        {
            temp = 0;
            for(i=0; i<K; i++)
                temp += swaps_required[i];
            cout<<temp<<endl;
        }
    }

    return 0;
}

