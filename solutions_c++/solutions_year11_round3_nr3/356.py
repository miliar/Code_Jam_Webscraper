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
        int N,L,H;
        cin>>N>>L>>H;
        vector<int> v(N);
        rep(i,0,N) cin>>v[i];
        int ans = -1;
        rep(i,L,H+1)
        {
            bool pos = true;
            rep(j,0,N)
                if(i % v[j] != 0 && v[j] % i != 0)
                    pos = false;
            if(pos)
            {
                ans = i;
                break;
            }
        }
        if(ans == -1)
            cout<<"NO"<<endl;
        else cout<<ans<<endl;
        
    }
}

