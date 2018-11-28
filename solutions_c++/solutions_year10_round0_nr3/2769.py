#include<iostream>
#include<vector>

using namespace std;

int main()
{

    int T; cin>>T;
    for(int t = 1; t <= T; ++t){
        int R, k, N;
        cin>>R>>k>>N;

        vector<int> groups(N, 0);
        long long tot = 0;
        for(int i = 0; i < N; ++i){
            cin>>groups[i];
            tot += groups[i];
        }

        if(tot < k){
            cout<<"Case #"<<t<<": "<<tot*R<<endl;
            continue;
        }

        vector<int> rides(N, -1),
                    people(N, -1);
        
        long long r = 0,
            gr = 0,
            pr = 0;

        int pos = 0;

        bool fast_forward = false;

        while(r < R){

            //new state or speed simulation is done
            if(rides[gr%N] == -1 || fast_forward){
                rides[gr%N] = r;
                people[gr%N] = pr;

                long long fill = 0;
                while(true){
                    int g = groups[pos];

                    if(g + fill > k) break;

                    pos = (pos+1)%N;
                    fill += g;
                    ++gr;
                }

                pr += fill;
                ++r;
            } 
            
            //old state
            else {
                fast_forward = true;

                long long _r = r - rides[gr%N],
                    _pr = pr - people[gr%N];

                int cycles = (R-r)/_r;

                r += cycles * _r;
                pr += _pr * cycles;
            }
        }

        cout<<"Case #"<<t<<": "<<pr<<endl;

    }

    return 0;
}
