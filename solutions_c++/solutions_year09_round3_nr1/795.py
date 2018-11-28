#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <bitset>


/*
#include <cstdio>
#include <cstdlib>
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
	int T;
	int val[128];
	unsigned long long int rtrn;
	int max;
	string tN;
	int N[62];
	int tv;

	cin >> T;
	FOR(t,0,T)
	{
	    FOR(i,0,128)
            val[i]=-1;
        cin >> tN;
        tv=0;
        rtrn=0;
        max = 0;
        val[tN[0]]=N[0]=1;
        FOR(i,1,tN.size())
        {
            if (val[tN[i]]<0)
            {
                val[tN[i]] = max;
                if (max) max++; else max=2;
            }
            N[i]=val[tN[i]];
        }
        if (max==0) max=2;
//        max--;
        FOR(i,0,tN.size())
        {
            rtrn*=max;
            rtrn+=N[i];
        }

		cout << "Case #"<< t+1 << ": " << rtrn << endl;

	}
	return 0;
}
