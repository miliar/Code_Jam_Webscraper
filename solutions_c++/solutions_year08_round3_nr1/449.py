// codejam p1.cpp

using namespace std;

#include<iostream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cctype>
#include<climits>
#include<cfloat>

#define GI ({int t;scanf("%d",&t);t;})
#define dbg(x) cout << #x << "->" << x << "	" << flush;
#define dbge(x) cout << #x << "->" << x << "	" << endl;
#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define FORZ(i,n) FOR(i,0,n)
#define EACH(i,v) FOR(i,(v).begin(),(v).end())
#define CS c_str()
#define PB push_back
#define SZ size()
#define INF (int)1e9+1

int main()
{
    int n;
    cin >> n;
    for( int nC = 1; nC <= n; nC++ )
    {
	int p, k, l;
	cin >> p >> k >> l;
	//vector< vector<int> > vvi( k,p );
	vector< int > vi;
	for( int i = 0; i < l; i++ )
	{
	    int x;
	    cin >> x;
	    vi.push_back( x );
	}
	sort( vi.begin(), vi.end() );
	reverse( vi.begin(), vi.end() );
	long long sum = 0;
	int index = 0;
	bool finish = false;
	for( int i = 1; i <= p; i++ )
	{
	   // cout << i << endl;
	    for( int j = 0; j < k; j++ )
	    {
	//	cout << j << endl;
		if( index == vi.size() )
		{
		    finish = true;
		    break;
		}
		sum += ( vi[index] * i );
	//	cout << vi[index] * i << endl;
		index++;
	    }	
	    if( finish )
		break;
	}

	    
        cout << "Case #" << nC << ": "<< sum << endl;;
    }
    return 0;
}
