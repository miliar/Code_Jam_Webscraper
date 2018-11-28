#include <iostream>
#include <string>
#include <sstream>
#include <vector>


/*
#include <cstdio>
#include <cstdlib>
#include <bitset>
#include <deque>
#include <queue>
#include <stack>
#include <valarray>
#include <vector>
#include <list>
#include <set> //set - multiset
#include <map> //map - multimap

#include <algorithm>
#include <functional>
#include <math.h>
#include <complex>
#include <numeric>
#include <limits>
#include <memory>
#include <utility>

#include <iomanip>
/**/
#define FOR(i, m, n) for (int i(m), _n(n); i<_n; ++i)
#define FORd(i, m, n) for (int i=(m), _n=(n); i>_n; --i)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

using namespace std;

int main(int argc, char *argv[])
{
	int L,D,N;
	char a [5000][15];
	bool tt[5000];
	bool ttt[5000];
	int i1, i2;
	cin >> L >> D >> N;
	FOR(i,0,D)
	{
		cin >> a[i] ;
	}
	FOR(i,0,N)
	{
//      string t;
	    char t[80004];
	    cin >> t;
	    FOR(d,0,D)
	    {
            tt[d]=true;
	    }

        int f=0;

	    FOR(j,0,L)
	    {

            FOR(d,0,D)
                ttt[d] = false;
	        if(t[j+f]=='(')
	        {
                f++;
                while (t[j+f]!=')')
                {
                    FOR(d,0,D)
                        if ( t[j+f]==a[d][j] )
                            ttt[d]=true;
                    f++;
                }
	        }
            else
            {
                FOR(d,0,D)
                    if ( t[j+f]==a[d][j] )
                        ttt[d]=true;
            }
            FOR(d,0,D)
                if (!ttt[d])
                    tt[d]=false;
	    }
	    f=0;
	    FOR(d,0,D)
            if (tt[d]) f++;
		cout << "Case #"<< i+1 << ": " << f << ("\n");
	}
	return 0;
}
