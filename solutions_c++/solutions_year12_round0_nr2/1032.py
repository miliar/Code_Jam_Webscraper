#include <string>
#include <vector>
#include <stdint.h>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <cassert>
#include <cstdio>
#include <list>
#include <cmath>
#include <climits>
#include <stack>

#define ASSERT(statement, obj) { typeof(obj) x=(statement); if(x!=(obj)){std::cout<<x<<std::endl;assert(false);}}
#define FOR(index, from, to) for (typeof(to) index=from; index<(to); ++index)
#define VFOR(index, v) for (typeof(v.size()) index=0; index<(v.size()); ++index)
#define ITER(it, list) for(typeof(list.begin()) it=list.begin(); it!=list.end();++it)
#define PRINT_VECTOR_INT(v) FOR(i, 0, v.size())cout<<v[i]<<" "
#define PBK push_back

using namespace std; 


int main()
{
	string line;
	int T=0;
	getline(cin, line);
	{
		stringstream ss(line);
		ss >> T;
	}

	FOR(i, 0, T)
	{
		getline(cin, line);
		stringstream ss(line);

		int N, S, p;
		ss >> N >> S >> p;
		vector<int> ggler;
		FOR(j, 0, N)
		{
			int to;
			ss >> to;
			ggler.PBK(to);
		}

		if (p == 0)
		{
			printf("Case #%d: %d\n", i+1, ggler.size());
			continue;
		}

		int C = 0;
		VFOR(j, ggler)
		{
			if (ggler[j] == 0)
			  continue;

			int th = p*3;
			if (th-2 <= ggler[j]) 
			{
  				C++;
				continue;
			}

			if (th - ggler[j] > 4)
			  continue;
			if (S > 0)
			{
				--S;
				C++;
			}
		}

		printf("Case #%d: %d\n", i+1, C);
	}
}
