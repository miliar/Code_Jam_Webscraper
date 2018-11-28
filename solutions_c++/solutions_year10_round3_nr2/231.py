#include<iostream>
#include<vector>
#include<string>

#define sz(X) ((int)(X.size())) 
#define rep(i,s,n) for(int i=s; i<n; i++) 

using namespace std;

int main()
{
    int T;
    cin>>T;
    rep(k,1,T+1)
    {
        long long L,P,T, temp;
        cin>>L>>P>>T;
        int cnt = 1;
        temp = L;
        while(true) 
        {
            temp *= T;
            cnt++;
            if(temp >= P) break;
        }

        int ans = 0, low = 1, high = cnt;
        while(true)
        {
            if(low + 1 == high)
                break;

            low = (low + high) / 2;
            ans++;
        }

        cout<<"Case #"<<k<<": "<<ans<<endl;
    }

    return 0;

}




