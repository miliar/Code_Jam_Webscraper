/*
 *  C.cpp
 *
 *  Created by Josh Deprez on 5/06/10.
 *
 */

#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <complex>
#include <ext/hash_set>
typedef long long ll;
typedef unsigned int uint;
using namespace std;
using namespace __gnu_cxx;
#define MAX_C 100
#define X real()
#define Y imag()

typedef complex<size_t> G;
typedef hash_set<G> H;

namespace __gnu_cxx {
	template<>
	struct hash<G>
	{
		size_t operator()(const G& x) const
		{
			return x.X * 1000000 + x.Y; 
		}
	};
}

int main()
{
	int C;
	cin >> C;
	
	for (int t=0; t<C; ++t) {
	 
		int R;
		cin >> R;
		H A,B;
		
		for (int r=0; r<R; ++r)
		{
			int x1, x2, y1, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for (int i=x1; i<=x2; ++i)
				for (int j=y1; j<=y2; ++j)
					B.insert(G(i,j));
		}
		
		int D=0;
		while (!B.empty())
		{
			A.swap(B);
			B.clear();
			for (H::iterator i=A.begin(), e=A.end(); i!=e; ++i)
			{
				if (A.find(G(i->X-1, i->Y)) != e || A.find(G(i->X, i->Y-1)) != e)
					B.insert(*i);
			
				if (A.find(G(i->X+1, i->Y-1)) != e) 
					B.insert(G(i->X+1, i->Y));
			
				//cout << *i << ", ";
			}
			//cout << endl;
			D++;
		}
		
		cout << "Case #" << (t+1) << ": " << D << endl;
	}
	 
	return 0;
}

