#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/io.hpp>

using namespace std;
// boost::numeric::ublas::matrix<double> m;

boost::numeric::ublas::matrix<int> m;
struct Coords{
	int i,j;
	operator int() { return i*10000 + j; }
	Coords(int _i,int _j ) { i = _i; j=_j; }
	Coords(int x) { i = x / 10000; j = x % 10000; }
	Coords() { i =j = 0; }
};

typedef list<Coords> CoordList;
typedef map<int,CoordList> HeigthMap;
typedef map<int,string> LabelMap;

Coords trydescent( Coords & pos, Coords & curbest, int di, int dj )
{
	Coords newpos = pos;
	newpos.i += di;
	newpos.j += dj;
	if (
		(newpos.i>=0) && (newpos.i<m.size1())
		&&
		(newpos.j>=0) && (newpos.j<m.size2())
		&&
		m(newpos.i,newpos.j) < m(curbest.i,curbest.j)
	)
		return newpos;
	else
		return curbest;
}

Coords explore(Coords & pos)
{
	Coords target = pos;

	target = trydescent( pos, target, -1,  0 ); // N
	target = trydescent( pos, target,  0, -1 ); // W
	target = trydescent( pos, target,  0,  1 ); // E
	target = trydescent( pos, target,  1,  0 ); // S

	return target;
}

typedef vector<int> IntVector;
typedef map<int,IntVector> LinkMap;

int main()
{
	int T;
	cin >> T;

	for(int t = 0; t<T; t++)
	{
		int R,C;
		cin >> R >> C;
		m = boost::numeric::ublas::zero_matrix<int>(R,C);
		HeigthMap h;
		for(int i = 0;i<R; i++)
		for(int j = 0;j<C; j++)
		{
			int elev;
			cin >> elev;
			m(i,j) = elev;
			Coords c;
			c.i = i;
			c.j = j;
			h[elev].push_back(c);
		}

		// Output
		cout << "Case #" << t+1<<":" << endl;

		LinkMap receivesfrom, basins;

		for(int i = 0;i<R; i++)
		for(int j = 0;j<C; j++)
		{
			Coords cur(i,j);
			Coords target = explore(cur);

			vector<int> & r = receivesfrom[target];

			if (target != cur)
			{
				r.push_back(cur);
			}
			else
			{
				// It's a basin endpoint
				basins[cur].push_back(cur);
			}

			// cout << "From: " << (int)c << " to " << (int)target << endl;
		}

		map<int,int> group,label;

		// For each basin endpoint (ie: foreach basin)
		for(LinkMap::iterator it = basins.begin(); it != basins.end(); it++)
		{
			Coords basin = it->first;
			IntVector sources = it->second;
			group[basin]=basin;

			for(int i = 0; i< sources.size(); i++)
			{
				IntVector & directsources = receivesfrom[ sources[i] ];

				sources.insert( sources.end(), directsources.begin(), directsources.end() );
				group[ sources[i] ] = basin;
			}

			// cout << it->first << endl;
		}

		for(LinkMap::iterator it = basins.begin(); it != basins.end(); it++)
		{
			Coords basin = it->first;
			IntVector sources = it->second;
			for(int i = 0; i< sources.size(); i++)
			{
				group[sources[i]]=basin;
			}
		}

		Coords root(0,0);
		Coords lastbasin = group[root];
		char lastLabel = 'a';
		label[lastbasin] = lastLabel;

		for(int i = 0;i<R; i++)
		{
			for(int j = 0;j<C; j++)
			{
				Coords cur(i,j);
				Coords curBasin = group[cur];
				if (label.find(curBasin)==label.end())
				{
					label[curBasin]= ++lastLabel;
				}

				if (j>0)
					cout << " ";

				cout << (char)label[curBasin];
			}
			cout << endl;
		}
		// From bottom to top
//		for(HeigthMap::iterator it = h.begin(); it != h.end(); it++)
//		{
//			CoordList coordlist = it->second;
//			for(CoordList::iterator it2 = coordlist.begin(); it2 != coordlist.end(); it2++)
//			{
////				Coords c = *it2;
//
//				// cout << "From: " << (int)c << " to " << (int)target << endl;
//			}
//		}

		// cout << m << endl;
	}

	return 0;
}
