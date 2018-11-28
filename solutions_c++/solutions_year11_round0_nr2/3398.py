#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <climits>
#include <bitset>
#include <cctype>
#include <numeric>
#include <functional>
using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;
#define pb push_back
#define sz size()
#define all(x) (x).begin(), (x).end()
#define GI ( { int t; scanf("%d",&t); t; } )
#define dbg(x) cout << #x << "= " << x << endl;
#define dbgg(x) cout << #x << endl;
#define eps 1e-8
#define eps1 1e-5
#define pi 2*acos(0.0)
#define mp make_pair
#define ff first
#define ss second

int main()
{
	vector< pair< string, char > > com;
	vector<string> opp;
	int t;
	cin >> t;
	string tmp="", tmp1="", tmp2="", list="", in;
	bool flag = 0;
	
	for( int cas=1; cas<=t; cas++ )
	{
		com.clear();
		opp.clear();
		list = "";
	
		int c;
		cin >> c;
		for( int i=0; i<c; i++ )
		{
			cin >> tmp1;
			tmp2 = string(1,tmp1[0]) + string(1,tmp1[1]);
			com.pb( mp( tmp2, tmp1[2] ) );
			
			tmp2 = string(1,tmp1[1]) + string(1,tmp1[0]);
			com.pb( mp( tmp2, tmp1[2] ) );
		}
		
		int d;
		cin >> d;
		for( int i=0; i<d; i++ )
		{
			cin >> tmp1;
		
			tmp2 = string(1,tmp1[0]) + string(1,tmp1[1]);
			opp.pb( tmp2 );
			
			tmp2 = string(1,tmp1[1]) + string(1,tmp1[0]);
			opp.pb( tmp2 );
		}
		
		
		int n;
		cin >> n;
		cin >> in;
		list += string(1,in[0]);
		
		for( int i=1; i<n; i++ )
		{
			if( list.empty() )
			{
				list = string(1,in[i]);
				continue;
			}
			
			tmp = list[list.sz-1] + string(1,in[i]);
			flag = 0;
			for( int j=0; j<com.sz; j++ )
			{
				if( tmp == com[j].ff )
				{
					list[list.sz-1] = com[j].ss;
					flag = 1;
					break;
				}
			}
			
			if( flag )
				continue;
			
			for( int k=0; k<list.sz; k++ )
			{
				tmp = list[k] + string(1,in[i]);
				for( int m=0; m<opp.sz; m++ )
				{
					if( tmp == opp[m] )
					{
						list = "";
						flag = 1;
						break;
					}
				}
				
				if( flag )
					break;
			}
			
			if( !flag )
				list += string(1,in[i]);
		}
		
		printf("Case #%d: [", cas);
		for( int x=0; x<list.sz; x++ )
		{
			printf("%c", list[x]);
			if( x+1 < list.sz )
				printf(", ");
		}
		printf("]\n");
	}
	
	return 0;
}
