#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

int pop(int n)
{
	int c=0;
	while(n) {
		if(n&1) ++c;
		n >>= 1;
	}
	return c;
}


bool sat( int mask, vector< vector< pair<int,bool> > >& cust )
{
	for(int i=0; i!=cust.size(); ++i)
	{
		vector< pair<int,bool> >& c = cust[i];
		bool ok = false;
		for(int j=0; j!=c.size(); ++j)
			if( c[j].second && (mask & (1<<c[j].first)) )
				ok = true;
			else
			if( !c[j].second && 0==(mask & (1<<c[j].first)) )
				ok = true;
		if(!ok)
			return false;
	}
	return true;
}


void solve( int N, vector< vector< pair<int,bool> > >& cust )
{
	int bestMask = 0x7fffffff;

	for(int mask=0; mask<(1<<N); ++mask)
	{
		if( pop(mask) < pop(bestMask)
		 && sat(mask, cust) )
			bestMask = mask;
	}

	if( pop(bestMask) > N ) {
		cout << " IMPOSSIBLE" << endl;
	} else {
		for(int i=0; i<N; ++i)
			cout << " " << ((bestMask>>i)&1);
		cout << endl;
	}
}

int main()
{
	int nCase; cin >> nCase;
	for(int T=1; T<=nCase; ++T)
	{
		cout << "Case #" << T << ":";

		int N, M; cin >> N >> M;
		vector< vector< pair<int,bool> > > cust(M);
		for(int i=0; i!=M; ++i) {
			int X; cin >> X;
			for(int j=0; j!=X; ++j) {
				int  p;
				bool um;
				cin >> p >> um;
				cust[i].push_back( make_pair(p-1,um) ); // 0-origin
			}
		}
		solve(N, cust);
	}
}
