#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>

using namespace std;

#define MAPITR(a,b)	map<a,b>::iterator
#define LISTITR(a)	list<a>::iterator

#define ITER(itr,a)	for( itr = (a).begin(); itr != (a).end(); ++itr )
#define ITERNI(itr,a)	for( itr = (a).begin(); itr != (a).end();  )
#define FORI(i,a,b)	for( int i(a), _b(b); i < _b; ++i )
#define FORD(i,a,b)	for( int i(a), _b(b); i > _b; --i )
#define FORLE(i,a,b)	for( int i(a), _b(b); i <= _b; ++i )
#define FORGE(i,a,b)	for( int i(a), _b(b); i >= _b; --i )

typedef list<char> lc;
typedef list<int> li;
typedef list<double> ld;
typedef list<string> ls;

typedef vector<char> vc;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;

vector< pair<unsigned long long, int> > vals;

void build_table( vi groups, int max )
{
	vals.clear();

	int size = groups.size();
	unsigned long long tmp;

	FORI( i, 0, size )
	{
		tmp = 0;

		int k( i );
		FORI( j, 0, size )
		{
			if( tmp + groups[k] > max )
			{
				break;
			}

			tmp += groups[k];

			++k;
			k %= size;
		}

		vals.push_back( pair< unsigned long long, int >( tmp, k ) );
	}
}

int main()
{
	bool loopFlag;
	int nCases, index;
	int R, k, N;
	unsigned long long sum, loopSum, tmp;
	int loopR;
	vi groups;

	cin >> nCases;

	FORLE( i, 1, nCases )
	{
		groups.clear();
		loopFlag = loopR = loopSum = index = sum = 0;

		cin >> R;
		cin >> k;
		cin >> N;

		FORI( j, 0, N )
		{
			cin >> tmp;
			groups.push_back( tmp );
		}

		build_table( groups, k );

		tmp = 0;

		FORI( j, 0, R )
		{
			sum += vals[tmp].first;
			tmp = vals[tmp].second;
		}

			cout << "Case #" << i << ": ";
			cout << sum << endl;
	}

	return 0;
}  
