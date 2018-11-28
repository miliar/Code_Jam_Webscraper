#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int main()
{
    int C; cin>>C;
    for(int c = 1; c <= C; ++c){
        int N,K,B,T;
        cin>>N>>K>>B>>T;

        vector< pair<int,int> > chickens(N, pair<int,int>());

        for(int i = 0; i < N; ++i){
            cin>>chickens[i].first;
        }

        for(int i = 0; i < N; ++i){
            cin>>chickens[i].second;
        }

        sort(chickens.begin(), chickens.end());

        int in_front = 0,
            saved = 0,
            swaps = 0;

        for(int i = chickens.size()-1; i >= 0 && saved < K; --i){
            
            //makes it
            if(T*chickens[i].second >= B - chickens[i].first){
                ++saved;
                swaps += in_front;
            } else {
                ++in_front;
            }
        }

        if(saved < K) cout<<"Case #"<<c<<": IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<c<<": "<<swaps<<endl;
    }

    return 0;
}
