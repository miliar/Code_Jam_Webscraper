// Google Code Jam - World Finals 2011 - Qualification Round -> Problem C
#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>
#include<sstream>
#include<iomanip>
#include<cstring>
#include<cmath>
#include<ctype.h>
using namespace std ;
#define foor(i,n,m) for( int i = (int) n ; i < (int) m ; i ++ )
#define foorit(it,v) for(__typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define pb(x) push_back(x)
#define makepair make_pair
int main ()
{
	freopen("input.txt" , "r" , stdin);
	freopen("output.txt" , "w" , stdout);
	int cases , n , sum , tmp , xor , MIN ;
	cin >> cases ;
	foor(c,1,cases+1)
	{
		xor = 0;
		sum = 0 ;
		MIN = INT_MAX ;
		cin >> n ;
		foor (i,0,n){cin>>tmp;sum+=tmp;xor^=tmp;MIN= min(MIN,tmp);}
		if (xor)
			cout << "Case #" << c << ": " << "NO" << endl ;
		else
			cout << "Case #" << c << ": " << sum-MIN << endl ;
	}
}