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
	int number[22];
	int digits[10];
	string tN;

	cin >> T;
	FOR(t,0,T)
	{
        cin >> tN;
        FOR(i,0,tN.size())
            number[i] = (tN[_n-i-1]-'0');
        FOR(i,tN.size(),22)
            number[i] = 0;

        FOR(i,0,10)
            digits[i] = 0;

        int i = 0, j = 0;
        do
        {
            digits[number[i++]]++;
        }
        while(number[i-1]<=number[i]);

        j=number[i]+1;
        while (j<10) if (digits[j]==0) j++; else break;
        digits[number[i]]++;
        digits[j]--;
        number[i]=j;
        i--;

        FOR(d,0,10)
            while(digits[d]-- > 0)
                number[i--]=d;


		cout << "Case #"<< t+1 << ": ";
		for(i=21; number[i]==0; i--);
		for(; i>=0; i--)
            cout << char(number[i] + '0');
        cout << endl;
        i++;


/*
		FOR(h,1,H+1)
		{
			cout << R[h][1];
			FOR(w,2,W+1)
				cout << " " << R [h][w];
			cout << endl;
		}
/**/
	}
	return 0;
}
