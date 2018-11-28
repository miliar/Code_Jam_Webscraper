//DS includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<bitset>
#include<complex>

//Other Includes
#include<sstream>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>



#define oo 					(int)13e7
#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define fill(a,v) 				memset(a, v, sizeof a)
#define ull 					unsigned long long
#define ll 						long long
#define bitcount 			__builtin_popcount
#define all(x) 				x.begin(), x.end()
#define pb( z ) 				push_back( z )
#define gcd					__gcd
using namespace std;


int a[1024];
int next[1024];
ll weight[1024];
int vis[1024], vid;
int R, k, n;
int z;
ll go( int p, int runs )
{
	if( runs==0 ) return 0;
	if( vis[p] == vid )
	{
		int cycleLength = 1, cycleWeight = weight[p];
		int cur = next[p];
		vis[p] = ++vid;
		
		while( cur != p && vis[cur] != vid )
		{
			vis[cur] = vid;
			cycleLength++; 
			cycleWeight += weight[cur];
			cur = next[cur];
		}
		//if( z==11 ) cout<<"cycles at " << p << " to " << cur <<" and " << cycleWeight <<" is left with " << runs << " and extra " << runs%cycleLength << endl;
		++vid;
		int left = runs%cycleLength ;
		return ( (runs)/cycleLength )*(ll)cycleWeight + go( cur, left );
	}
	vis[p] = vid;
	return go( next[p], runs-1 ) + weight[p];
}
int mod( int x )
{
	return (n+x)%n;
}

int main()
{
	freopen( "C-small-attempt1.in", "r", stdin );
	freopen( "C-small-attempt1.out" ,"w", stdout );
	
	
	int t;
	cin>>t;
	for(z=1; z <= t; z++)
	{
		cin>>R>>k>>n;
		for(int i=0; i < n; i++)
			cin>>a[i];
		
		for(int i=0; i < n; i++)
		{
			ll &cur = weight[i];
			int &ni = next[i];
			ni = mod( i+1 );
			cur = a[i];
			//cout<< i <<"(" << cur<<","<<a[i] << ")"<< " se " ;
			while( cur <= k && ni != i )
			{
				
				cur += a[ni];
				//cout<< ni <<"(" << cur<<","<<a[ni] << ")" <<  " ";
				ni = mod( ni+1 );
				
				
			} //cout<<endl;
			if( cur > k )
			{
				ni = mod( ni-1 );
				cur -= a[ni];
				
			}
			//cout<< i << " to " << next[i] << " and " << weight[i] << endl;
		}
		++vid;
		printf("Case #%d: %lld\n", z, go( 0, R ) );
		
	}
	
	return 0;
}
