#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <map>
#include <vector>
#include <cstring>
#include <set>
using namespace std;

#define rev(x) reverse((x).begin(), (x).end())
#define sor(x) sort(x.begin(), x.end())
#define sz size()
#define pb push_back
#define vi vector<int>
#define vvi vector<vi>
#define vs vector<string>
#define ll long long
#define fill(var,val) memset(var, val, sizeof(var))
#define rep(i, n) for(i = 0; i < n; i++)
#define repa(i, a, n) for(i = a; i < n; i++)
#define s(n) scanf("%d", &n);
#define p(n) printf("%d\n", n);

int main()
{
	int t;
	s(t);
	int k = 0;
	while(t--)
	{
		k++;
		int L, N, C; ll t;
		s(L); cin>>t; s(N); s(C);
		vector<ll> path; int i;
		vector<ll> dist;
		dist.pb(0);
		for(i=0;i<C;i++)
		{ll a; cin>>a; path.pb(a); }
		repa(i,C,N+2) path.pb(path[i%C]);
		repa(i,1,N+2) dist.pb(path[i-1]+dist[i-1]);
		
		ll best = dist[N]*2;
		ll cur_pos = t/2;
		//Binary search to locate the position.
		int low = 0, high = N, mid = (low+high)>>1;
		//cout << "here" << endl;
		while(!(dist[mid] <= cur_pos && dist[mid+1] > cur_pos))
		{
			
			if(cur_pos > dist[mid])
				low = mid;
			else if(cur_pos < dist[mid])
				high = mid;
			mid=(low+high)>>1;
			
			if(low + 1 == high)
			{
				if(dist[mid] < dist[high]) { mid = low; break; }
				else { mid = high; break; }
			}
			//cout << low << " " << high << " " << mid << " " << dist[low] << " " << dist[high] << " " << cur_pos << endl;
		}
		//cout << "here" << endl;
		
		
		if(L > 0 && mid != N)
		{
			vector<ll> arr;
			arr.pb(min(dist[mid+1]-dist[mid], dist[mid+1] - cur_pos));
			//cout << best << " " << arr[0] << endl;
			for(i=mid+1;i<N;i++)	
				arr.pb(path[i]);
			
			sor(arr); rev(arr);
			
			if(L>0)
				for(i=1;i<=min(L,(int)arr.sz);i++)
					best-=arr[i-1];
			
		}
		
		cout << "Case #" << k << ": " << best << endl;
	}
	return 0;
}
