#include <algorithm> 
#include <bitset> 
#include <cctype> 
#include <cmath> 
#include <cmath> 
#include <cstdio> 
#include <cstdio> 
#include <cstdlib> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <deque> 
#include <functional> 
#include <iomanip> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <string> 
#include <utility> 
#include <vector> 

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define rep(i,s,n) for(int i=s; i<n; i++)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define getint(c) (int)(c - 'a')

using namespace std;

int main()
{
    int T;
    cin>>T;
    for(int t = 0; t < T; t++)
    {
        cout<<"Case #"<<t+1<<": ";
        map<long long, long long> m;
        long long L,t,N,C;
        cin>>L>>t>>N>>C;
        //cout<<L<<' '<<t<<' '<<N<<' '<<C<<endl;
        vector<int> a(C);
        rep(i,0,C) cin>>a[i];
        int j = 0;
        long long ans = 0;
        rep(i,0,N)
        {
            m[a[j]]++;
            ans += (long long)a[j] * 2;
            j++;
            j %= C;
        }
        //cout<<ans<<endl;
        long long d = t / 2;
        j = 0;
        int k = 0;
        for(; k < N; k++)
        {
            if(a[j] >= d)
                break;
            d -= a[j];
            m[a[j]]--;
            j++;
            j %= C;
        }
        //cout<<ans<<endl;
        if(k < N)
        {
            m[a[j]]--;
            m[a[j] - d]++;
        }
        //tr(m,itr)
        //    cout<<itr->first<<' '<<itr->second<<endl;
        map<long long,long long>::reverse_iterator itr = m.rbegin();
        rep(i,0,L)
        {
            while(itr->second == 0) itr++;
            if(itr == m.rend()) break;
            ans -= itr->first;
            itr->second--;
        }
        cout<<ans<<endl;
    }
}

