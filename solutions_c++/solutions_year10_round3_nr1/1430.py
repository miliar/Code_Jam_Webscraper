#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define repd(i,n) for (int i((n)-1); i >= 0; --i)
#define rep2(i,x,m) for(int i=x;i<m;i++)
#define rep2d(i,x,m) for(int i=x;i>=0;i--)
#define repit(i,c) for (typeof((c).end()) i=(c).begin(); i!=(c).end(); ++i)
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("o1.txt", "w+", stdout);

    int t;
    cin >> t;
    rep (tt, t)
    {
        
        int n;
        cin>>n;
        map<int,int> m;
        map<int,int>::iterator it;
        rep(i,n)
        {
            int a,b;
            cin>>a>>b;
            m[a]=b;  
        }   
        cout << "Case #" << (tt+1) << ": "; 
        if(n==1)
        {
            cout<<"0\n";
            
        }  
        else
        {
            int count=0;
            map<int,int>::iterator it1=m.begin();
            rep(i,n)
            {
                int b=(*it1).second;
                map<int,int>::iterator it2=it1;
                it2++;
                for ( it=it2; it != m.end(); it++ )
                {
                    if((*it1).second > (*it).second)
                    count++;
                } 
                it1++;   
            }  
            cout<<count<<"\n";    
        }
    }    
        

	return 0;
}
