#include<iostream>
#include<vector>

using namespace std;

int main()
{
    vector<int> ans(100, 1<<30);
    ans[0] = 0;

    for(int i = 1; i < ans.size(); ++i){
        for(int k = 0; k < i; ++k){
            ans[i] = min(ans[i], max(ans[k],ans[i-k-1]) + 1);
        }
    }

    int T; cin>>T;
    for(int t = 1; t <= T; ++t){
        int L,P,C;
        cin>>L>>P>>C;
        
        int a = P/C + (P%C != 0);
        int p = 0;
        while(a > L){
            ++p;
            a = a/C + (a%C != 0);
        }

        cout<<"Case #"<<t<<": "<<ans[p]<<endl;
    }

    return 0;
}
