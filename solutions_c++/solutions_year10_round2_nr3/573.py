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


const int mod = 100003;
int R[32];
bool pure( const vector<int> a )
{
	if( a.size() == 0 )
		return 1;
	fill( R, -1 );
	for(int i=0; i < a.size(); i++)
	R[ a[i] ] = i+1;
	int cur = a[ a.size()-1];
	while( cur != 1 && cur != -1 )
	{
		cur = R[ cur ];
	}
	if( 0 )
	if( cur==1 )
	{
		cout<<"array : ";
		for(int i=0; i < a.size(); i++) 
			cout<< a[i] << " ";
		cout<<endl;
	}
	return cur==1;
}

int main()
{
	//freopen("ip.txt", "r", stdin );
	//freopen("C-small-attempt0.in", "r", stdin );
	freopen("C-small-attempt1.in", "r", stdin );
	//freopen("C-small-attempt2.in", "r", stdin );
	//freopen("C-large.in", "r", stdin );
	
	//freopen("C-small-attempt0.out", "w", stdout );
	freopen("C-small-attempt1.out", "w", stdout );
	//freopen("C-small-attempt2.out", "w", stdout );
	//freopen("C-large.out", "w", stdout );
	/*
	for(int n=1; n <= 25; n++)
	{
		
		int ans = 0;
		for(int i=0; i < (1<<(n-1)); i++)
		{
			vector<int> a;
			for(int j=0; j < n; j++)
			if( i & 1 << j )
				a.pb( j+2 );
			a.pb( n+1 );
			if( pure( a ) )
				ans++;
		}
		cout<< n+1 << " = " << ans << endl;
		
	}
	*/
	
	int precomp[] = {1,2,3,5,8,14,24,43,77,140,256,472,874,1628,
	3045,5719,10780,20388,38674,73562,140268,268066,
	513350,984911,1892875};
	
	int T;
	cin>>T;
	for(int t=1; t <= T; t++)
	{
		int n;
		cin>>n;
		printf("Case #%d: %d\n", t, precomp[n-2]%mod );
	}
	
	return 0;
}

