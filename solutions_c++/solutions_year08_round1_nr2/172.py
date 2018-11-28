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

#define sz(X) ((int)(X.size()))
#define ln(X) ((int)(X.length()))
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define rep(i,s,n) for(int i=s; i<n; i++)
#define rrep(i,s,n) for(int i=n-1; i>=s; i--)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define err 1E-15

using namespace std;

int main()
{
	int runs;
	cin>>runs;
	rep(k,1,runs+1)
	{
		int N,M;
		cin>>N>>M;
		
		vector<int> mo(M,-1),ch(M);
		vector<vector<int> > umo(M);
		
		rep(i,0,M)
		{
			int t;
			cin>>t;
			ch[i] = t;
			
			rep(j,0,t)
			{
				int x, y;
				cin>>x>>y;
				x--;
				if(y == 1) mo[i] = x;
				else umo[i].pb(x);
			}
		}
		//rep(i,0,M) {cout<<i<<" "; rep(j,0,sz(umo[i])) cout<<umo[i][j]<<" "; cout<<endl;}
		vector<int> done(M,false);
		vector<int> ans(N,0);
		rep(cnt,0,N)
		{
			rep(i,0,M)
			{
				bool can = false;
				rep(j,0,sz(umo[i]))
				{
					if(ans[umo[i][j]] == 0)
					{
						//cout<<i<<' '<<j<<endl;
						can = true;
						break;
					}
					
				}
				if(!can && mo[i] != -1) ans[mo[i]] = 1;
			}
		}
		//rep(i,0,N) cout<<ans[i]<<endl;
		rep(i,0,M)
		{
			if(mo[i] != -1 && ans[mo[i]] == 1) 
			{
				done[i] = true;
				continue;
			}
			rep(j,0,sz(umo[i]))
			{
				if(ans[umo[i][j]] == 0)
				{
					done[i] = true;
					break;
				}
			}
					
		}
		bool pos = true;
		rep(i,0,M)
			if(!done[i])
			{
				pos = false;
				break;
			}
		cout<<"Case #"<<k<<":";
		if(pos)
		{
			
			rep(i,0,N)
				cout<<" "<<ans[i];
			cout<<endl;
		}
		else cout<<" IMPOSSIBLE"<<endl;
	
	}
}