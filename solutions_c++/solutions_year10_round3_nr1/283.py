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
        vector<int> A,B;
        int a,b;
        int N;
        cin>>N;
        rep(i,0,N)
        {
            cin>>a>>b;
            A.push_back(a);
            B.push_back(b);
        }
        int ans = 0;
        rep(i,0,N)
            rep(j,i+1,N)
            {
                if(A[i] < A[j] && B[i] > B[j]) ans++;
                if(A[i] > A[j] && B[i] < B[j]) ans++;
            }


        cout<<"Case #"<<k<<": "<<ans<<endl;
    }

    return 0;

}
