#include<iostream>
#include<vector>

using namespace std;

bool allMarked(const vector<bool>& vec){
    for(int i = 0; i < vec.size(); ++i) if(!vec[i]) return false;
    return true;
}

bool valid(const vector< vector<int> >& now, const vector<int>& test){
    for(int i = 0; i < now.size(); ++i){
        for(int k = 1; k < now[i].size(); ++k){
            //touched
            if(now[i][k] == test[k] || now[i][k-1] == test[k-1]) return false;

            //cross
            if(now[i][k] < test[k] && now[i][k-1] > test[k-1]) return false;
            if(now[i][k] > test[k] && now[i][k-1] < test[k-1]) return false;
        }
    }
    return true;
}

int main()
{
    int T;
    cin>>T;
    for(int t = 1; t <= T; ++t){

        //input
        int N,K;
        cin>>N>>K;

        vector< vector<int> > prices(N,vector<int>(K,0));

        for(int n = 0; n < N; ++n){
            for(int k = 0; k < K; ++k){
                cin>>prices[n][k];
            }
        }
        
        //compute
        int charts = 0;

        vector<bool> used(N,false);

        for(int k = 0; k < N; ++k){
            if(used[k]) continue;

            ++charts;
            vector< vector<int> > now;
            now.push_back(prices[k]);
            
            //find valid ones
            for(int i = 0; i < N; ++i){
                if(used[i]) continue;
                else if(valid(now,prices[i])){
                    used[i] = true;
                    now.push_back(prices[i]);
                }
            }
        }

        cout<<"Case #"<<t<<": "<<charts<<endl;

    }
    return 0;
}
