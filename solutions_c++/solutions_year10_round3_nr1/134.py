#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    int T; cin>>T;
    for(int t = 1; t <= T; ++t){
        int N; cin>>N;

        vector< pair<int,int> > w(N, pair<int,int>());

        for(int i = 0; i < N; ++i){
            cin>>w[i].first>>w[i].second;
        }

        sort(w.begin(),w.end());

        int ans = 0;

        for(int i = 0; i < w.size(); ++i){
            for(int k = i+1; k < w.size(); ++k){
                if(w[i].second > w[k].second) ++ans;
            }
        }

        cout<<"Case #"<<t<<": "<<ans<<endl;
    }

    return 0;
}
