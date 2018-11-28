/*
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 */

/*
 * Includes
 */

#include <algorithm>
#include <bitset>
#include <deque>     /* Double ended queue */
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>     /* FIFO queue */
#include <set>
#include <sstream>
#include <stack>     /* LIFO stack */
#include <string>
#include <utility>
#include <vector>

using namespace std;


/*
 * Basic Types
 */

typedef long long int Int;
typedef double        Real;


/*
 * Shortcuts
 *
 * C -> Auxiliary iteration count (predefined variable)
 * I -> Container instance
 * L -> Limit
 * T -> Container type
 * V -> Variable name (In-loop defined)
 */

#define for_in(V, L)                   for(Int V = 0; V < (L); V++)
#define for_iter(V, T, I)              for(T::iterator V = I.begin(); V != I.end(); V++)
#define for_iter_rev(V, T, I)          for(T::reverse_iterator V = I.rbegin(); V != I.rend(); V++)
#define for_iter_count(V, T, I, C)     for(T::iterator V = I.begin(); V != I.end(); V++, C++)
#define for_iter_rev_count(V, T, I, C) for(T::reverse_iterator V = I.rbegin(); V != I.rend(); V++, C++)

#define iterator_of(V, T, I)     T::iterator V = I.begin()
#define rev_iterator_of(V, T, I) T::reverse_iterator V = I.rend()

#define ccin (cin >> ws)


/*
 * Types
 */

typedef vector<Int> VectorI;
typedef list<Int> ListI;
typedef map<char, Int> MapCI;
typedef map<Int, char> MapIC;
typedef priority_queue<Int> MaxQueueI;
typedef priority_queue<Int, vector<Int>, greater<Int> > MinQueueI;



/*
 * Problem
 */



int main()
{
    Int count; ccin >> count;
    for_in(n, count) {
    	cout << "Case #" << n + 1 << ": ";
    	/* Input */ /* Process */
    	Int P, K, L; ccin >> P >> K >> L;
    	if(L <= (P*K)) {
    		ListI F; Int res = 0;
    		for_in(i, L) {Int q; ccin >> q; F.push_back(q);}
    		F.sort();
    		for_in(i, P) for_in(j, K) {
    			if(F.empty()) break;
    			res += (i + 1) * F.back();
    			F.pop_back();
    		}

    		cout << res << endl;
    	}
    	else
    		cout << "Impossible" << endl;




        /* Output */

    }

    return 0;
}
