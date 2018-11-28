#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

const long long MOD = 10007;
using namespace std;
long long 	cg[20000];
long long 	noword ( string t )
{
	for ( long long i = 0; i < ( long long ) t . size (); i ++ )
	{
		if ( t[i] >= 'a' && t[i] <= 'z' )return false;
		if ( t[i] >= 'A' && t[i] <= 'Z' )return false;
	}
	return true;
}

string 	nc ( long long next = 1 )
{
	static 	long long 	number = 0;
	number += next;
	stringstream 	tmp;
	tmp << "Case #" << number << ": ";
	string 	str;
	getline ( tmp, str );
	return 	str;
}
		vector < pair < long long, long long > > 	a;
long long 	c ( long long a, long long  b )
{
	if ( a < 0 )
		return 0; 
	if ( b < 0 )
		return 0;
	if ( a < b )
		return 0;
	long long 	tm = 0;
	long long 	sum = 1;
	for ( long long i = a; i >= a - b + 1; i -- )
	{
		long long 	t = i;
		while ( t % MOD == 0 )
		{
			t /=  MOD;
			tm ++;
		}
			sum *= t;
			
		sum %= MOD;
	} 
	for ( long long i = 1; i <= b; i ++ )
	{
		
		long long 	t = i;
		while ( t % MOD == 0 )
		{
			t /=  MOD;
			tm --;
		}
		sum *= cg[t % MOD];
		sum %= MOD; 
	}
		
	if ( tm ) 
		return 0;
	return sum;
}

void 	 change ( long long t1, long long t2 )
{
	long long sum  = t1 + t2;
	sum -= 2;
	if ( sum % 3 )
		return; 
	sum /= 3; 
	//cerr << sum << " " << t1 - sum - 1 << endl;
	if ( t1 - sum - 1 >= 0 &&  t1 - sum - 1 <= sum )
	a . push_back ( make_pair ( sum, t1 - sum - 1 ) );
}


long long 	cmp ( pair < long long,long long> a, pair < long long,long long> b )
{
	if ( a . first < b . first ) return true;
	if ( a . first > b . first ) return false;
	
	if ( a . second < b . second ) return true;
	if ( a . second > b . second ) return false;
	return false;
	
}


int main ()
{
	for ( long long i = 1; i < MOD; i ++ )
	{
		for ( long long j = 1; j < MOD; j ++ )
		{
			if (  i * j % MOD == 1 )
			{
				cg[i] = j;
				break;
			}
		}
	}
	freopen ( "1.in", "r", stdin );
	freopen ( "1.out", "w", stdout );
	long long 	rr = 0;
	cin >> rr;
	while ( rr -- )
	{
		cerr << rr << endl;
		a . clear ();			//cout << nc () << endl;
		long long 	h, w, r;
		cin >> h >> w >> r;
		vector <long long > 	sum;
		 ( change ( h, w ) );
		 if ( a . empty () )
		 {
			 for ( long long i = 0; i < r; i ++ )
		{
			long long 	t1, t2 ;
			cin >> t1 >> t2;
			 }
			 cout << nc () << 0 << endl;
			continue;
		 }
		for ( long long i = 0; i < r; i ++ )
		{
			long long 	t1, t2 ;
			cin >> t1 >> t2;
			 ( change ( t1, t2 ) );
		}
		sort ( a . begin (), a . end (), cmp );
		long long 	n = a . size ();
		for ( long long i = 0; i < n ; i ++ )
		{
			sum. push_back ( 0 );
			sum[i] += c ( a[i] . first, a[i] . second );
			for ( long long j = 0; j < i; j ++ )
				sum[i] -= sum[j] * c ( -a[j] . first + a[i] . first, -a[j] . second + a[i] . second );
			
			sum[i]  %=MOD;
			sum[i] += MOD + MOD;
			sum[i]  %=MOD;
		}
			cout <<nc () <<  sum[n -1] << endl;
	
	
	
	
	
	
	
	
	}
//	cout << nc ( 100 ) << endl;
//	cout << nc () << endl;
}
