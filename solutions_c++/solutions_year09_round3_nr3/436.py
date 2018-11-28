#include <iostream>
#include <cstring>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

#define NMAX 10100

int T, P, Q, ret;
char cell[NMAX];
vector<int> rel;

int main()
{
	int i, j, t, tmp;

	freopen("C.IN","r",stdin);
	freopen("C.out","w",stdout);

	cin >> T;

	for ( t = 1; t <= T; ++t )
	{
		cin >> P >> Q;
		
		rel.clear();
		for ( i = 1; i <= Q; ++i )
			cin >> tmp, rel.push_back(tmp);

		ret = -1;
		do
		{
			memset(cell,0,sizeof(cell));
			tmp = 0;
			for ( i = 0; i < rel.size(); ++i )
			{
				cell[ rel[i] ] = 1;

				for ( j = rel[ i ] - 1; cell[j] == 0 && j > 0; --j ) ++tmp;
				for ( j = rel[ i ] + 1; cell[j] == 0 && j <= P; ++j ) ++tmp;
			}

			
			if ( tmp < ret || ret == -1 )
				ret = tmp;

		} while ( next_permutation(rel.begin(),rel.end()) );

		cout << "Case #" << t << ": " << ret << endl;
	}

	return 0;
}