#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define eps 1e-9
typedef stringstream ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef complex<double> point;
typedef long long ll;
#define X real()
#define Y imag()
int oo=0x7FFFFFFF;
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("a.txt","rt",stdin);
    freopen("b.txt","wt",stdout);
    #endif
    vector<pair<ll,ll> > ps;
    int N;
    cin>>N;
    ll n,A,B,C,D,x,y,M;
    for(int nn=0;nn<N;nn++)
    {
        ps.clear();
        cin>>n>>A>>B>>C>>D>>x>>y>>M;
        pair<ll,ll> p(x,y);
        ps.pb(p);
        for(int i=0;i<n-1;i++)
        {
            p.first*=A;
            p.first+=B;
            p.first%=M;
            p.second*=C;
            p.second+=D;
            p.second%=M;
            ps.pb(p);
        }
        int cnt=0;
        rep(i,n)
            for(int j=i+1;j<n;j++)
                for(int k=j+1;k<n;k++)
                {
                    if((ps[i].first+ps[j].first+ps[k].first)%3==0 && (ps[i].second+ps[j].second+ps[k].second)%3==0)
                        cnt++;
                }
        cout<<"Case #"<<nn+1<<": "<<cnt<<endl;
    }
    return 0;
}
